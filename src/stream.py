import pylivestream.api as pls

sites = ["youtube"]
def streamImage(music_path, image_file):
    s = pls.FileIn("../pylivestream.json", sites, infn=music_path, image=image_file, yes=True, timeout=50)
    s.golive()

def streamVideo(video_file):
    pls.stream_file("../pylivestream.json", sites, video_file=video_file, assume_yes=True)
