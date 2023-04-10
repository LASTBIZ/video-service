import pylivestream.api as pls
import pylivestream.base as base
def streamImage(music_path, image_file):
    s = pls.FileIn("../pylivestream.json", "youtube", infn=music_path, image=image_file, yes=True, timeout=50)
    s.golive()

def streamVideo(video_file):
    pls.stream_file("../pylivestream.json", "youtube", video_file=video_file, assume_yes=True)
