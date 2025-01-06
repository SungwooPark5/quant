from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class StockPrice(BaseModel):
    datetime: Annotated[datetime, Body()]
    ticker: str
    price: float


@app.get("/stockprice", response_model=StockPrice)
async def get_stock_price(ticker: str):

    data = {
        "datetime": datetime.now(),
        "ticker": ticker,
        "price": 1000,
    }

    stockprice = StockPrice(**data)

    return stockprice
