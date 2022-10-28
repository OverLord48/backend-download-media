import os, pwd
from pathlib import Path
from pytube import Playlist
from pytube import YouTube

BASE_DIR = Path(__file__).resolve().parent.parent
os.mkdir('musics')
def download_list(url):
    p = Playlist(url)

    for video in p.video_urls:
        try:
            yt = YouTube(video)
        except:    
            print("connection error")

        filemp4 = yt.streams.filter(only_audio=True)[0]
        filemp4.download(filename = f"{BASE_DIR}/musics/{yt.title}.mp3")

    return True

def download_music(url):
    yt = YouTube(url)

    filemp3 = yt.streams.filter(only_audio=True)[-1]
    filemp3.download(filename = f"{yt.title}.mp3")

    return True