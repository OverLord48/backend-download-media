from fastapi import APIRouter, Response, status
from baseModels.yt_BaseModel import UrlVideo
from services.ytube import *

ryt = APIRouter()

@ryt.post("/download/video-to-mp3")
def download_video_converter(url):

    return download_music(url)

@ryt.post("/download/playlist-to-mp3")
def download_playlist_converter(url):
    
    return download_list(url)