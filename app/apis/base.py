from fastapi import APIRouter

from app.apis.version1 import route_general, route_yt

api_router = APIRouter()
api_router.include_router(route_general.router, prefix="", tags=["General"])
api_router.include_router(route_yt.router, prefix="/yt", tags=["YouTube"])
