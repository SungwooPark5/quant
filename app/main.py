from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select

from .models import CountryEnum, TickerBase, TickerCreate, Ticker
from .database import get_session


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# def foo()-> bar는 foo의 출력값을 bar로 지정한 것
@app.get("/tickers")
async def get_tickers(session: Session = Depends(get_session)) -> list[Ticker]:

    ticker_list = session.exec(select(Ticker)).all()

    return ticker_list


@app.get("/tickers/{ticker_id}")
async def get_ticker_by_id(
    ticker_id: int, session: Session = Depends(get_session)
) -> Ticker:

    ticker = session.get(Ticker, ticker_id)

    if ticker is None:
        # status code 404
        raise HTTPException(status_code=404, detail="Ticker not found")
    return ticker


@app.post("/tickers")
async def create_ticker(
    ticker_data: TickerCreate, session: Session = Depends(get_session)
) -> Ticker:
    ticker = Ticker(name=ticker_data.name, country=ticker_data.country)

    session.add(ticker)
    session.commit()
    session.refresh(ticker)

    return ticker
