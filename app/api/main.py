from fastapi import APIRouter

from app.api.routes import ticker

api_router = APIRouter()
api_router.include_router(ticker.router)
