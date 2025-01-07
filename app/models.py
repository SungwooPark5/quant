from datetime import date
from enum import Enum
from pydantic import validator
from sqlmodel import Field, Relationship, SQLModel


# Enum
class CountryEnum(Enum):
    USA = "USA"
    KOREA = "KOR"


# Models
class TickerBase(SQLModel):
    name: str = Field(max_length=30)
    country: CountryEnum


# Properties to receive via API on creation(from full stack fastapi template)
class TickerCreate(TickerBase):
    @validator("country", pre=True)
    def upper_case_country(cls, value: str):
        return value.upper()


class TickerWithId(TickerBase):
    id: int


class Ticker(TickerBase, table=True):
    id: int = Field(default=None, primary_key=True)


# class StockPrice(SQLModel, table=True):
#     date: date
#     # stock: Stock = Relationship()
#     price: float
