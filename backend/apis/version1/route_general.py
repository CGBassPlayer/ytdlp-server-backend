import platform

import fastapi
import yt_dlp.version
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.core.config import settings
from backend.db.models.versions import Version
from backend.db.session import get_db

router = APIRouter()


@router.get("/software")
def get_software():
    return {
        "api": settings.PROJECT_VERSION,
        "Python": platform.python_version(),
        "fastAPI": fastapi.__version__,
        "yt-dlp": yt_dlp.options.__version__
    }


@router.get("/version")
def get_revisions(db: Session = Depends(get_db)):
    return db.query(Version).order_by(Version.updated.desc()).all()


@router.get("/version/{version}")
def get_revisions(version: str, db: Session = Depends(get_db)):
    if version == "current":
        return db.query(Version).filter(Version.id == settings.PROJECT_VERSION).first()
    return db.query(Version).filter(Version.id == version).first()
