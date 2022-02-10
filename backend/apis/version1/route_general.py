import platform

import fastapi
import yt_dlp.version
from fastapi import APIRouter

from backend.core.config import settings

router = APIRouter()


@router.get("/version")
def get_versions():
    return {
        "api version": settings.PROJECT_VERSION,
        "yt-dlp version": yt_dlp.options.__version__,
        "Python version": platform.python_version(),
        "fastAPI version": fastapi.__version__,
    }
