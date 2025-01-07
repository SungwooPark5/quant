from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Annotated

from datetime import datetime

from .models import CountryEnum, TickerBase, TickerCreate, TickerWithId

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


TICKERS = [
    {"id": 1, "name": "SPY", "country": CountryEnum.USA},
    {"id": 2, "name": "TLT", "country": CountryEnum.USA},
    {"id": 3, "name": "IWM", "country": CountryEnum.USA},
    {"id": 4, "name": "069500.KS", "country": CountryEnum.KOREA},
]


# def foo()-> bar는 foo의 출력값을 bar로 지정한 것
@app.get("/tickers")
async def get_tickers() -> list[TickerBase]:

    return [TickerBase(**t) for t in TICKERS]


@app.get("/tickers/{ticker_id}")
async def get_ticker_by_id(ticker_id: int) -> TickerWithId:
    ticker = next((TickerWithId(**t) for t in TICKERS if t["id"] == ticker_id), None)
    if ticker is None:
        raise HTTPException(status_code=404, detail="Ticker not found")
    return ticker


@app.post("/tickers")
async def create_ticker(ticker_data: TickerCreate) -> TickerWithId:
    id = TICKERS[-1]["id"] + 1
    ticker = TickerWithId(id=id, **ticker_data.model_dump()).model_dump()
    TICKERS.append(ticker)

    return ticker
