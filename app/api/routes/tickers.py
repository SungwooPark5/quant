from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select

from app.models import TickerCreate, Ticker, TickerPrice
from app.database import get_session
from app import crud

router = APIRouter(tags=["tickers"])


# def foo()-> bar는 foo의 출력값을 bar로 지정한 것
@router.get("/tickers")
async def get_tickers(session: Session = Depends(get_session)) -> list[Ticker]:

    ticker_list = session.exec(select(Ticker)).all()

    return ticker_list


@router.get("/tickers/{ticker_id}")
async def get_ticker_by_id(
    ticker_id: int, session: Session = Depends(get_session)
) -> Ticker:

    ticker = session.get(Ticker, ticker_id)

    if ticker is None:
        # status code 404
        raise HTTPException(status_code=404, detail="Ticker not found")
    return ticker


@router.post("/tickers")
async def create_ticker(
    ticker_data: TickerCreate, session: Session = Depends(get_session)
) -> Ticker:
    ticker = Ticker(name=ticker_data.name, country=ticker_data.country)

    session.add(ticker)
    session.commit()
    session.refresh(ticker)

    return ticker


@router.get("/tickers/price/{ticker_name}")
async def get_ticker_price(
    ticker_name: str, session: Session = Depends(get_session)
) -> list[TickerPrice]:
    ticker_name = ticker_name.upper()
    ticker = crud.get_ticker_by_name(session=session, name=ticker_name)
    ticker_price = crud.get_ticker_price_by_ticker(session=session, ticker=ticker)

    if ticker is None:
        # status code 404
        raise HTTPException(status_code=404, detail="Ticker not found")

    elif ticker_price is None:
        # status code 404
        raise HTTPException(status_code=404, detail="Ticker price not found")

    return ticker_price
