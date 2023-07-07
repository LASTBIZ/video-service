import asyncio
from concurrent import futures

import grpc

import proto.video_pb2_grpc
import app
from google.protobuf.empty_pb2 import Empty


class VideoServiceServicer(proto.video_pb2_grpc.VideoServicer):
    def __init__(self, videos, images):
        print("")
        self.videos = videos
        self.images = images
        # print(file.videos)

    def CreateVideo(self, request, context):
        app.filestream.AddVideo(self.videos, request.path)
        return Empty()

    def CreateScreenShoot(self, request, context):
        app.filestream.AddScreenshot(self.images, request.path, request.site_path)
        return Empty()

    def UpdateScreenShoot(self, request, context):
        print(request)
        return Empty()

    def DeleteScreenShoot(self, request, context):
        app.filestream.RemoveScreenshot(self.images, request.path)
        return Empty()

    def UpdateVideo(self, request, context):
        print(request)
        return Empty()

    def DeleteVideo(self, request, context):
        app.filestream.DeleteVideo(self.videos, request.path)
        return Empty()


def serve(videos, images):
    print("asdasd")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto.video_pb2_grpc.add_VideoServicer_to_server(
        VideoServiceServicer(videos, images), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
    # await server.wait_for_termination()

