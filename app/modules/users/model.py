"""User ORM Model"""

from __future__ import annotations

from typing import TYPE_CHECKING
from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.common.mixins.base_model import BaseModel

if TYPE_CHECKING:
    from app.modules.roles.model import Role


class User(BaseModel):
    """
    Core authentication user.

    Stores only identity and authentication
    related information.
    """
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
    role_id: Mapped[int] = mapped_column(
        ForeignKey(
            "roles.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )
    role: Mapped["Role"] = relationship(
        back_populates="users",
        lazy="selectin",
    )


def __repr__(self) -> str:
    return (
        f"User(id={self.id}, "
        f"username='{self.username}', "
        f"email='{self.email}')"
    )