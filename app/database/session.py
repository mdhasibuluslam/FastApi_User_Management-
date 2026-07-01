""" Database engine and session configuration. """

from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings

engine = create_async_engine(

    settings.DATABASE_URL,
    echo=settings.DEBUG,
    future=True,
    pool_pre_ping=True,
    pool_size = 10,
    max_overflow = 20,
    pool_recycle = 3600,
)

AsyncSessionLocal = async_sessionmaker(

    bind=engine,

    class_=AsyncSession,

    expire_on_commit=False,
)

async def get_db():

    async with AsyncSessionLocal() as session:

        try:

            yield session

        finally:

            await session.close()

DBsession = Annotated[
    AsyncSession,
    Depends(get_db),
]