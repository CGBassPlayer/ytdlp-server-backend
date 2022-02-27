import platform

import fastapi
import jinja2
import yt_dlp.version
from fastapi import APIRouter

from backend.core.config import settings

router = APIRouter()


@router.get("/version")
def get_versions():
    return {
        "api": settings.PROJECT_VERSION,
        "Python": platform.python_version(),
        "fastAPI": fastapi.__version__,
        "yt-dlp": yt_dlp.options.__version__,
        "jinja2": jinja2.__version__
    }
