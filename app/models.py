from datetime import date
from enum import Enum
from pydantic import BaseModel
from sqlmodel import Field, Relationship, SQLModel


# Enum
class CountryEnum(Enum):
    USA = 1
    KOREA = 2


# Models
class TickerBase(SQLModel):
    name: str = Field(max_length=30)
    country: str = CountryEnum


class Ticker(TickerBase, table=True):
    id: int = Field(default=None, primary_key=True)


# class StockPrice(SQLModel, table=True):
#     date: date
#     # stock: Stock = Relationship()
#     price: float
