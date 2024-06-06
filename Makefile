celery:
	celery -A celery_worker.celery worker --loglevel=info

app:
	python app.py

ngrok:
	ngrok http 5000

swagger:
	swagger2markdown -i swagger.yaml -o api_documentation.md
