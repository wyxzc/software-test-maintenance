#!/usr/bin/python
import os
import time
import grpc
import pymongo
from concurrent import futures
from datetime import datetime

from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
from grpc_reflection.v1alpha import reflection

# 生成的proto文件
import demo_pb2
import demo_pb2_grpc

class CommentService(demo_pb2_grpc.CommentServiceServicer):
    def __init__(self):
        # 连接MongoDB数据库
        self.db_host = os.getenv("DB_HOST", "mongodb-comment")
        self.db_port = int(os.getenv("DB_PORT", "27017"))
        self.client = pymongo.MongoClient(f"mongodb://{self.db_host}:{self.db_port}/")
        self.db = self.client.commentdb
        self.comments = self.db.comments

    def AddComment(self, request, context):
        comment = {
            "product_id": request.product_id,
            "user_id": request.user_id,
            "comment_text": request.comment_text,
            "rating": request.rating,
            "created_at": datetime.utcnow()
        }
        
        result = self.comments.insert_one(comment)
        
        return demo_pb2.AddCommentResponse(
            success=True,
            comment_id=str(result.inserted_id)
        )

    def GetComments(self, request, context):
        comments = self.comments.find({"product_id": request.product_id})
        comment_list = []
        
        for comment in comments:
            comment_list.append(demo_pb2.Comment(
                comment_id=str(comment["_id"]),
                product_id=comment["product_id"],
                user_id=comment["user_id"],
                comment_text=comment["comment_text"],
                rating=comment["rating"],
                created_at=comment["created_at"].strftime("%Y-%m-%d %H:%M:%S")
            ))
            
        return demo_pb2.GetCommentsResponse(comments=comment_list)

def start_server(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # 添加评论服务
    service = CommentService()
    demo_pb2_grpc.add_CommentServiceServicer_to_server(service, server)
    
    # 添加健康检查
    health_servicer = health_pb2_grpc.HealthServicer()
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    # 添加反射服务
    service_names = (
        demo_pb2.DESCRIPTOR.services_by_name["CommentService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_names, server)
    
    # 启动服务器
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    
    print(f"Comment service starting on port {port}...")
    server.wait_for_termination()

if __name__ == "__main__":
    port = os.getenv("PORT", "50051")
    start_server(port) 