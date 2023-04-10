
import magic
from os import listdir
from os.path import isfile, join
import imagesize
from pymediainfo import MediaInfo
import stream
path = join("..", "files")

#Load files
files = [f for f in listdir(path) if isfile(join(path, f))]
videos = []
images = []

music = "../music/Shiro_Sagisu_Attack_of_Titans.mp3"

for file in files:
    type = magic.from_file(join(path, file), mime=True)
    if type == "image/jpeg" or type == "image/png":
        width, height = imagesize.get(join(path, file))
        if width == 1920 and height == 1080:
            images.append(join("..", "files", file))
    if type == "video/mp4" or type == "video/x-msvideo":
        media_info = MediaInfo.parse(join(path, file))
        for track in media_info.tracks:
            if track.track_type == 'Video':
                if track.width == 1920 and track.height == 1080:
                    videos.append(join(path, file))
print(images)
print(videos)

while True:
    for image in images:
        stream.streamImage(music, image)
    for video in videos:
        stream.streamVideo(video)

