import os
from selenium import webdriver
import pylivestream.api as pls
import pylivestream.base as base

sites = ["youtube"]

# pls.stream_files(ini_file="pylivestream.json", websites=sites, loop=True, video_path="./videos", glob="*",
#                  assume_yes=True)
# stream = base.Livestream(site="youtube", inifn="pylivestream.json", image="./videos/vk.png", loop=True, vidsource="file", audio_chan="null")
# next(stream.startlive(sinks=["youtube"]))

s = pls.FileIn("pylivestream.json", "youtube", infn="./music/Shiro_Sagisu_Attack_of_Titans.mp3", loop=True, image="./videos/vk.png", yes=False)
s.golive()
# options = webdriver.FirefoxOptions()
# options.add_argument('--headless')
# driver = webdriver.Remote(
#     command_executor='http://192.168.0.3:4444',
#     options=options
# )
# driver.set_window_size(1920, 1165)
# driver.get("https://habr.ru/")
# driver.save_screenshot('vk.png')
# driver.quit()