import grpc
import sys
from google.protobuf.empty_pb2 import Empty
import FileServices_pb2 as FileServicesStub
import FileServices_pb2_grpc as FileServices_pb2_grpc

SERVER_ADDRESS = '54.198.28.222:50051'

class FileClient:
    def __init__(self, address):
        self.channel = grpc.insecure_channel(address)
        self.stub = FileServices_pb2_grpc.FileServiceStub(self.channel)

    def list_files(self):
        request = Empty()
        response = self.stub.ListFiles(request)
        return response

    def find_file(self, name):
        request = FileServicesStub.FileRequest(name=name)
        response = self.stub.FindFile(request)
        return response

    def get_file(self, name):
        request = FileServicesStub.FileRequest(name=name)
        response = self.stub.GetFile(request)
        return response

    def put_file(self, name, data):
        request = FileServicesStub.FileContent(name=name, data=bytes(data))
        response = self.stub.PutFile(request)
        return response


grpc_client = FileClient(SERVER_ADDRESS)
