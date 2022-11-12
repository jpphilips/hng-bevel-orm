from sqlalchemy import Column, ForeignKey, Integer, Float, DateTime, String
from sqlalchemy.orm import relationship
from .database import Base


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, unique=True, index=True)
    isocode = Column(String, unique=True)
    symbol = Column(String, unique=True)

    black_market_rates = relationship(
        "BlackMarketRate", back_populates="currency")
    official_market_rates = relationship(
        "OfficialMarketRate", back_populates="currency")


class BlackMarketRate(Base):
    __tablename__ = "black_market_rates"

    id = Column(Integer, primary_key=True, index=True)
    buy = Column(Float)
    buy = Column(Float)
    time = Column(DateTime)
    currency_id = Column(Integer, ForeignKey("currencies.id"))

    currency = relationship("Currency", back_populates="black_market_rates")


class OfficialMarketRate(Base):
    __tablename__ = "official_market_rates"

    id = Column(Integer, primary_key=True, index=True)
    buy = Column(Float)
    buy = Column(Float)
    time = Column(DateTime)
    currency_id = Column(Integer, ForeignKey("currencies.id"))

    currency = relationship("Currency", back_populates="official_market_rates")
