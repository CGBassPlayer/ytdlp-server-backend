from fastapi import APIRouter

from backend.apis.version1 import route_general, route_yt

api_router = APIRouter(prefix="/v1")
api_router.include_router(route_general.router, prefix="", tags=["General"])
api_router.include_router(route_yt.router, prefix="/yt", tags=["YouTube"])
