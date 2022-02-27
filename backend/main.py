from fastapi import FastAPI

from backend.apis.base import api_router
from backend.db.base import Base
from backend.db.session import engine

app = FastAPI()
app.include_router(api_router)
Base.metadata.create_all(bind=engine)
