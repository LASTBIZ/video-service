import stream
import files
import storage_video

filestream = files.FileStream()


class App:
    def __init__(self):
        self.file = filestream

    def start_stream(self):
        music = "../music/Shiro_Sagisu_Attack_of_Titans.mp3"
        while True:
            # print("sdsd")
            for image in self.file.images:
                stream.streamImage(music, image)
            for video in self.file.videos:
                stream.streamVideo(video)
