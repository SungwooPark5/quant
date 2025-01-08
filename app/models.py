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


class Ticker(TickerBase, table=True):
    id: int = Field(default=None, primary_key=True)
    # back_populates를 이용해 이름으로 연결된된 정보를 받아올 수 있음
    prices: list["TickerPrice"] = Relationship(back_populates="ticker")


class TickerPriceBase(SQLModel):
    date: date
    price: float
    # 외래키 설정
    ticker_id: int = Field(foreign_key="ticker.id")


class TickerPrice(TickerPriceBase, table=True):
    id: int = Field(default=None, primary_key=True)
    ticker: Ticker = Relationship(back_populates="prices")
