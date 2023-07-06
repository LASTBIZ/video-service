import asyncio
import grpc

import proto.video_pb2_grpc
import app
from google.protobuf.empty_pb2 import Empty


class VideoServiceServicer(proto.video_pb2_grpc.VideoServicer):

    async def CreateVideo(self, request, context):
        app.filestream.AddVideo(request.path)
        return Empty()

    async def CreateScreenShoot(self, request, context):
        app.filestream.AddScreenshot(request.path, request.site_path)
        return Empty()

    async def UpdateScreenShoot(self, request, context):
        print(request)
        return Empty()

    async def DeleteScreenShoot(self, request, context):
        app.filestream.RemoveScreenshot(request.path)
        return Empty()

    async def UpdateVideo(self, request, context):
        print(request)
        return Empty()

    async def DeleteVideo(self, request, context):
        app.filestream.DeleteVideo(request.path)
        return Empty()


async def serve():
    print("asdasd")
    server = grpc.aio.server()
    proto.video_pb2_grpc.add_VideoServicer_to_server(
        VideoServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    await server.start()

    return server
    # await server.wait_for_termination()

