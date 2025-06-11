FROM python:3.12.6-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip3 install -r requirements.txt

# 复制源代码
COPY . .

# 生成proto文件
RUN python3 -m grpc_tools.protoc -I ./protos --python_out=. --grpc_python_out=. ./protos/demo.proto

# 设置环境变量
ENV PORT=50051

EXPOSE 50051

# 启动服务
ENTRYPOINT [ "python3", "comment_server.py" ] 