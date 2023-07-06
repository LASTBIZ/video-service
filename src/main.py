import asyncio

import grpc_video

from concurrent.futures import ThreadPoolExecutor
import stream
from app import App

app = App()

music = "../music/Shiro_Sagisu_Attack_of_Titans.mp3"

executor = ThreadPoolExecutor()


async def start_stream():
    while True:
        print("sdsd")
        for image in app.file.images:
            await asyncio.get_event_loop().run_in_executor(executor, stream.streamImage(music, image))
        for video in app.file.videos:
            await asyncio.get_event_loop().run_in_executor(executor, stream.streamVideo(video))


async def main():
    server = await grpc_video.serve()
    tasks = [
        asyncio.create_task(start_stream())
    ]

    await asyncio.gather(*tasks)
    await server.wait_for_termination()


asyncio.run(main())
# asyncio.get_event_loop().run_until_complete(grpc_video.serve())
# start_stream()

# # run stream
