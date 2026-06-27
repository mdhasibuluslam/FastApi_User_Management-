""" Database engine and session configuration. """

from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings



engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DBsession = Annotated[
    Session,
    Depends(get_db),
]