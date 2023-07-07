import magic
from os import listdir, remove
from os.path import isfile, join
import imagesize
from pymediainfo import MediaInfo
import storage_video
import screenshot


class FileStream():
    def __init__(self):
        self.videos = []
        self.images = []
        self.storage = storage_video.StorageStream()
        # Load files
        path = join("..", "files")
        self.path = path
        files = [f for f in listdir(path) if isfile(join(path, f))]
        # Type files
        for file in files:
            type = magic.from_file(join(path, file), mime=True)
            if type == "image/jpeg" or type == "image/png":
                width, height = imagesize.get(join(path, file))
                if width == 1920 and height == 1080:
                    self.images.append(join("..", "files", file))
            if type == "video/mp4" or type == "video/x-msvideo":
                media_info = MediaInfo.parse(join(path, file))
                for track in media_info.tracks:
                    if track.track_type == 'Video':
                        if track.width == 1920 and track.height == 1080:
                            self.videos.append(join(path, file))

    def AddVideo(self, videos,  video: str):
        self.storage.download_video(video)
        videos.append(join(self.path, video))
        print(self.videos)

    def DeleteVideo(self, videos, video: str):
        remove(join(self.path, video))
        videos.remove(join(self.path, video))
        print(videos)

    def AddScreenshot(self, images, name, site):
        screenshot.screenshot(join(self.path, name), site)
        images.append(join(self.path, name+".png"))
        print(self.images)

    def RemoveScreenshot(self, images, name):
        remove(join(self.path, name+".png"))
        images.remove(join(self.path, name+".png"))
