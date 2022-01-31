from fastapi import FastAPI

from backend.apis.base import api_router
from backend.core.config import settings
from backend.db.base import Base
from backend.db.session import engine

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
app.include_router(api_router)
Base.metadata.create_all(bind=engine)
