# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import FileServices_pb2 as FileServices__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class FileServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListFiles = channel.unary_unary(
                '/FileService/ListFiles',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=FileServices__pb2.FileList.FromString,
                )
        self.FindFile = channel.unary_unary(
                '/FileService/FindFile',
                request_serializer=FileServices__pb2.FileRequest.SerializeToString,
                response_deserializer=FileServices__pb2.FileList.FromString,
                )
        self.PutFile = channel.unary_unary(
                '/FileService/PutFile',
                request_serializer=FileServices__pb2.FileContent.SerializeToString,
                response_deserializer=FileServices__pb2.OperationStatus.FromString,
                )
        self.GetFile = channel.unary_unary(
                '/FileService/GetFile',
                request_serializer=FileServices__pb2.FileRequest.SerializeToString,
                response_deserializer=FileServices__pb2.FileContent.FromString,
                )


class FileServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PutFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=FileServices__pb2.FileList.SerializeToString,
            ),
            'FindFile': grpc.unary_unary_rpc_method_handler(
                    servicer.FindFile,
                    request_deserializer=FileServices__pb2.FileRequest.FromString,
                    response_serializer=FileServices__pb2.FileList.SerializeToString,
            ),
            'PutFile': grpc.unary_unary_rpc_method_handler(
                    servicer.PutFile,
                    request_deserializer=FileServices__pb2.FileContent.FromString,
                    response_serializer=FileServices__pb2.OperationStatus.SerializeToString,
            ),
            'GetFile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFile,
                    request_deserializer=FileServices__pb2.FileRequest.FromString,
                    response_serializer=FileServices__pb2.FileContent.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileService/ListFiles',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            FileServices__pb2.FileList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileService/FindFile',
            FileServices__pb2.FileRequest.SerializeToString,
            FileServices__pb2.FileList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PutFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileService/PutFile',
            FileServices__pb2.FileContent.SerializeToString,
            FileServices__pb2.OperationStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileService/GetFile',
            FileServices__pb2.FileRequest.SerializeToString,
            FileServices__pb2.FileContent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)