from typing import Union
from routes.route_yt import ryt
from fastapi import FastAPI

app = FastAPI()

app.include_router(ryt)

