from fastapi import APIRouter, Response, status
from pytube import Playlist
from pytube import YouTube



ryt = APIRouter()

@ryt.get("/download/video-to-mp3/{url}")
def download_video_converter(url:str):
    yt = YouTube(url)

    filemp3 = yt.streams.filter(only_audio=True)[-1]
    filemp3.download(filename = f"{yt.title}.mp3")

    return Response({"message":"descarga exitosa"}, status.HTTP_200_OK)

@ryt.get("/download/playlist-to-mp3/{url}")
async def download_playlist_converter(url:str):
    p = Playlist(url)

    for video in p.video_urls:
        try:
            yt = YouTube(video)
        except:    
            print("connection error")

        filemp4 = yt.streams.filter(only_audio=True)[0]
        await filemp4.download(filename = f"{yt.title}.mp3")

    return Response({"message":"descarga exitosa"}, status.HTTP_200_OK)