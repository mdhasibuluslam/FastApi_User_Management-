""" soft delete mixin"""

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean


class SoftDeleteMixin:
    is_delete:Mapped[bool] = mapped_column(Boolean, default=False,nullable=False)
    