import asyncio
import multiprocessing
import files
import grpc_video
from multiprocessing import Process, Value, Array

from concurrent.futures import ThreadPoolExecutor
import stream
from app import App

app = App()

executor = ThreadPoolExecutor()


# async def start_stream():
#     while True:
#         print("sdsd")
#         for image in app.file.images:
#             await asyncio.get_event_loop().run_in_executor(executor, stream.streamImage(music, image))
#         for video in app.file.videos:
#             await asyncio.get_event_loop().run_in_executor(executor, stream.streamVideo(video))

def start_stream(videos, images):
    music = "../music/Shiro_Sagisu_Attack_of_Titans.mp3"
    print(videos, images)
    while True:
        print("sdsd")
        for image in images:
            stream.streamImage(music, image)
        for video in videos:
            stream.streamVideo(video)


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    videos = manager.list(app.file.videos)
    images = manager.list(app.file.images)
    p1 = Process(target=start_stream, args=(videos, images))
    p2 = Process(target=grpc_video.serve, args=(videos, images))
    p2.start()
    p1.start()
    p2.join()
    p1.join()

# p.start()
# p.join()

# asyncio.get_event_loop().run_until_complete(grpc_video.serve())
# start_stream()

# # run stream
