from fastapi import APIRouter

from app.api.routes import tickers

api_router = APIRouter()
api_router.include_router(tickers.router)
