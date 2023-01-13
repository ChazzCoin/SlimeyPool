from __future__ import unicode_literals
import os
import subprocess
from SlimeManager import FFMPEG
import youtube_dl
from pytube import YouTube
from F import OS
completedFolder = f"{OS.get_cwd()}/completed"

def post_processor():
    for file in OS.get_files_in_directory(completedFolder):
        if str(file).endswith(".mp4"):
            newFile = str(file)[:-4]
            newFile = f"{newFile}-rs"
            file = f"{completedFolder}/{file}"
            post_process(file, newFile)
            OS.remove(file)


def post_process(fileIn, fileOutName=None):
    return FFMPEG.to_mp3(fileIn, removeOriginal=True)

def YoutubeDownloader(url):
    try:
        ytObj = YouTube(url)
        video = ytObj.streams.filter(only_audio=True).first()
        destination = 'completed'
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        mp4File = base + '.mp4'
        post_process(mp4File)
        newMp4File = str(mp4File).replace(" ", "-")
        OS.rename_file(mp4File, newMp4File)
        return mp4File, url
    except:
        return None

def GeneralDownloader(url):

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    if type(url) not in [list]:
        url = [url]
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
        return True, url
    except:
        return False, url

# from F import OS
# test = OS.get_cwd() + "/test.mp3"
# # post_process_two(test)
# post_processor()
# YoutubeDownloader("https://www.youtube.com/watch?v=cHHLHGNpCSA")