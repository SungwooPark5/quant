from datetime import date
from enum import Enum
from pydantic import BaseModel
from sqlmodel import Field, Relationship, SQLModel


# Enum
class CountryEnum(Enum):
    USA = "USA"
    KOREA = "KOR"


# Models
class TickerBase(SQLModel):
    name: str = Field(max_length=30)
    country: CountryEnum


class Ticker(TickerBase, table=True):
    id: int = Field(default=None, primary_key=True)


# class StockPrice(SQLModel, table=True):
#     date: date
#     # stock: Stock = Relationship()
#     price: float
