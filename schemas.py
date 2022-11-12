from typing import List, Union

from pydantic import BaseModel
from datetime import datetime


class BlackMarketRateBase(BaseModel):
    buy: float
    sell: float
    time = datetime.now()


class OfficialMarketRateBase(BaseModel):
    buy: float
    sell: float
    time = datetime.now()


class BlackMarketRateCreate(BlackMarketRateBase):
    pass


class OfficialMarketRateCreate(OfficialMarketRateBase):
    pass


class BlackMarketRate(BlackMarketRateBase):
    id: int
    currency_id: int

    class Config:
        orm_mode = True


class OfficialMarketRate(OfficialMarketRateBase):
    id: int
    currency_id: int

    class Config:
        orm_mode = True


class CurrencyBase(BaseModel):
    country: str
    isocode: str
    symbol: str


class CurrencyCreate(CurrencyBase):
    pass


class Currency(CurrencyBase):
    id: int
    black_market_rates: List[BlackMarketRate] = []
    official_market_rates: List[OfficialMarketRate] = []

    class Config:
        orm_mode = True
