""" soft delete mixin"""

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, DateTime


class SoftDeleteMixin:
    is_delete:Mapped[bool] = mapped_column(Boolean, default=False,nullable=False)
    deleted_at:Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)
