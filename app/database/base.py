""" Base class for all SQLAlchemy models. Every ORM model will inherit from Base. """

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

