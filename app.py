from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
import requests
import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://myuser:mypassword@mysql:3306/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

db = SQLAlchemy(app)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), unique=True, nullable=False)
    product_id = db.Column(db.String(50), nullable=False)
    purchase_date = db.Column(db.DateTime, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __init__(self, user_id, product_id, purchase_date, expiry_date, status):
        self.user_id = user_id
        self.product_id = product_id
        self.purchase_date = purchase_date
        self.expiry_date = expiry_date
        self.status = status

@app.route('/verify_purchase', methods=['POST'])
def verify_purchase():
    token = request.json.get('receipt')
    user_id = request.json.get('user_id')
    if not token or not user_id:
        return jsonify({"error": "No receipt or user_id provided"}), 400

    try:
        response = requests.post(
            'https://sandbox.itunes.apple.com/verifyReceipt',  # 沙盒环境；生产环境使用 https://buy.itunes.apple.com/verifyReceipt
            json={'receipt-data': token, 'password': 'your_shared_secret'}
        )
        response_data = response.json()
        if response_data.get('status') == 0:
            # 假设响应包含 purchase_date 和 expiry_date
            purchase_date = datetime.datetime.strptime(response_data['purchase_date'], '%Y-%m-%d %H:%M:%S')
            expiry_date = datetime.datetime.strptime(response_data['expiry_date'], '%Y-%m-%d %H:%M:%S')
            new_subscription = Subscription(
                user_id=user_id,
                product_id=response_data['product_id'],
                purchase_date=purchase_date,
                expiry_date=expiry_date,
                status='active'
            )
            db.session.add(new_subscription)
            db.session.commit()
            return jsonify({"success": True, "data": response_data})
        else:
            return jsonify({"success": False, "error": response_data.get('exception', 'Unknown error')})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/apple_notifications', methods=['POST'])
def apple_notifications():
    data = request.json
    notification_type = data.get('notification_type')
    if notification_type:
        handle_apple_notification.delay(data)  # 使用 Celery 任务处理通知
        return jsonify({"success": True}), 200
    return jsonify({"error": "Invalid notification data"}), 400

@celery.task
def handle_apple_notification(data):
    notification_type = data['notification_type']
    if notification_type == 'DID_CHANGE_RENEWAL_STATUS':
        handle_renewal_status_change(data)
    elif notification_type == 'INITIAL_BUY':
        handle_initial_buy(data)
    else:
        print(f"Received notification: {notification_type}")

def handle_renewal_status_change(data):
    user_id = data['user_id']
    new_expiry_date = datetime.datetime.strptime(data['expiry_date'], '%Y-%m-%d %H:%M:%S')
    subscription = Subscription.query.filter_by(user_id=user_id).first()
    if subscription:
        subscription.expiry_date = new_expiry_date
        db.session.commit()
        print(f"Updated expiry date for user {user_id} to {new_expiry_date}")

def handle_initial_buy(data):
    user_id = data['user_id']
    product_id = data['product_id']
    purchase_date = datetime.datetime.strptime(data['purchase_date'], '%Y-%m-%d %H:%M:%S')
    expiry_date = datetime.datetime.strptime(data['expiry_date'], '%Y-%m-%d %H:%M:%S')
    new_subscription = Subscription(
        user_id=user_id,
        product_id=product_id,
        purchase_date=purchase_date,
        expiry_date=expiry_date,
        status='active'
    )
    db.session.add(new_subscription)
    db.session.commit()
    print(f"Created new subscription for user {user_id}")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 创建数据库表
    app.run(host='0.0.0.0', port=5000, debug=True)
