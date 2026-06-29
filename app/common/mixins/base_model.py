"""
BaseModel

Every ORM model should inherit from this class.
"""

from app.database.base import Base

from app.common.mixins.id import IDMixin
from app.common.mixins.uuid import UUIDMixin
from app.common.mixins.timestamp import TimestampMixin
from app.common.mixins.soft_delete import SoftDeleteMixin


class BaseModel(
    Base,
    IDMixin,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
):
    """
    Abstract base class for all ORM models.
    """

    __abstract__ = True