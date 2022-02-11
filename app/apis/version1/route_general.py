import platform

import fastapi
import jinja2
import yt_dlp.version
from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.core.config import settings

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/version")
def get_versions():
    return {
        "api": settings.PROJECT_VERSION,
        "Python": platform.python_version(),
        "fastAPI": fastapi.__version__,
        "yt-dlp": yt_dlp.options.__version__,
        "jinja2": jinja2.__version__
    }
