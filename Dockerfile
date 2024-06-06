# 使用官方的 Python 映像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制所有必要的文件
COPY . /app

# 安装依赖项
RUN pip install -r requirements.txt

# 启动 Flask 应用
CMD ["flask", "run", "--host=0.0.0.0"]
