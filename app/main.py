from fastapi import FastAPI, Body
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
