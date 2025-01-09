from sqlmodel import Session, select

from app.models import Ticker, TickerPrice


def get_ticker_by_name(*, session: Session, name: str) -> Ticker | None:
    statement = select(Ticker).where(Ticker.name == name)
    ticker = session.exec(statement).first()

    return ticker


def get_ticker_price_by_ticker(
    *, session: Session, ticker: Ticker
) -> list[TickerPrice] | None:
    statement = select(TickerPrice).where(TickerPrice.ticker_id == ticker.id)
    ticker_price = session.exec(statement).all()

    return ticker_price
