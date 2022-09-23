import os

import subprocess
from F import OS

ff_AUDIO_192K = "-b:a 192k"
MP3 = ".mp3"
MP4 = ".mp4"

"ffmpeg -re -i <fileName> -c:v copy -c:a aac -ar 44100 -ac 1 -f flv rtmp://localhost/live/stream"

def clean_file_name(fileIn):
    cleanedFileIn = str(fileIn).replace(" ", "-").replace("(", "-").replace(")", "-")
    OS.rename_file(fileIn, cleanedFileIn)
    return cleanedFileIn

def to_mp3(fileIn, removeOriginal=False):
    fileIn = clean_file_name(fileIn)
    newFile = str(fileIn)[:-4]
    output = subprocess.run(f"ffmpeg -i {fileIn} -b:a 192k {newFile}{MP3}", shell=True)
    print(output)
    if removeOriginal:
        os.remove(fileIn)
    return f"{newFile}{MP3}"

def to_mp4(fileIn, removeOriginal=False):
    fileIn = clean_file_name(fileIn)
    newFile = str(fileIn)[:-4]
    output = subprocess.run(f"ffmpeg -i {fileIn} -codec copy {newFile}{MP4}", shell=True)
    print(output)
    if removeOriginal:
        os.remove(fileIn)
    return f"{newFile}{MP4}"