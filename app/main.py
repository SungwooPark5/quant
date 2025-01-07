from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Annotated

from datetime import datetime

from .models import CountryEnum, TickerBase

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


TICKERS = [
    {"id": 1, "name": "SPY", "country": CountryEnum.USA},
    {"id": 2, "name": "TLT", "country": CountryEnum.USA},
    {"id": 3, "name": "IWM", "country": CountryEnum.USA},
]


@app.get("/tickers")
async def get_tickers() -> list[TickerBase]:

    return [TickerBase(**t) for t in TICKERS]


@app.get("/tickers/{ticker_id}")
async def get_ticker_by_id(ticker_id: int) -> TickerBase:
    ticker = next((TickerBase(**t) for t in TICKERS if t["id"] == ticker_id), None)
    if ticker is None:
        raise HTTPException(status_code=404, detail="Ticker not found")
    return ticker
