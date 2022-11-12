from sqlalchemy.orm import Session

from . import models, schemas


def get_currency(db: Session, currency_id: int):
    return db.query(models.Currency).filter(models.Currency.id == currency_id).first()


def get_currency_by_country(db: Session, country: str):
    return db.query(models.Currency).filter(models.Currency.country == country).first()


def get_currency_by_isocode(db: Session, isocode: str):
    return db.query(models.Currency).filter(models.Currency.isocode == isocode).first()


def get_currency_by_symbol(db: Session, symbol: str):
    return db.query(models.Currency).filter(models.Currency.symbol == symbol).first()


def get_currencies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Currency).offset(skip).limit(limit).all()


def create_currency(db: Session, currency: schemas.CurrencyCreate):
    db_currency = models.Currency(
        country=currency.country,
        isocode=currency.isocode,
        symbol=currency.symbol
    )
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency


def get_black_market_rates(db: Session, skip: int = 0, limit: int = 24):
    return db.query(models.BlackMarketRate).offset(skip).limit(limit).all()


def get_recent_black_market_rates(db: Session):
    return db.query(models.BlackMarketRate).filter(BlackMarketRate.id ==
                                                   db.query(func.max(models.BlackMarketRate.id)))


def create_black_market_rates(db: Session, item: schemas.BlackMarketRateCreate, currency_id: int):
    db_black_market_rate = models.BlackMarketRate(
        **item.dict(), currency_id=currency_id)
    db.add(db_black_market_rate)
    db.commit()
    db.refresh(db_black_market_rate)
    return db_black_market_rate


def get_official_market_rates(db: Session, skip: int = 0, limit: int = 24):
    return db.query(models.OfficialMarketRate).offset(skip).limit(limit).all()


def get_recent_official_market_rates():
    return db.query(models.OfficialMarketRate).filter(OfficialMarketRate.id ==
                                                      db.query(func.max(models.OfficialMarketRate.id)))


def create_official_market_rates(db: Session, item: schemas.OfficialMarketRateCreate, currency_id: int):
    db_official_market_rate = models.OfficialMarketRate(
        **item.dict(), currency_id=currency_id)
    db.add(db_official_market_rate)
    db.commit()
    db.refresh(db_official_market_rate)
    return db_official_market_rate
