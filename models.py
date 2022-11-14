from sqlalchemy import Column, ForeignKey, Integer, Float, DateTime, String
from sqlalchemy.orm import relationship
from .database import Base


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, unique=True, index=True)
    isocode = Column(String, unique=True)
    symbol = Column(String, unique=True)

    rates = relationship(
        "Rate", back_populates="currency")


class Rate(Base):
    __tablename__ = "rates"

    id = Column(Integer, primary_key=True, index=True)
    official_buy = Column(Float)
    official_sell = Column(Float)
    parallel_buy = Column(Float)
    parallel_sell = Column(Float)
    last_updated = Column(DateTime)
    currency_id = Column(Integer, ForeignKey("currencies.id"))

    currency = relationship("Currency", back_populates="rates")


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
