from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, UniqueConstraint
from app.common.mixins.base_model import BaseModel
if TYPE_CHECKING:
    from app.modules.roles.model import Role
    from app.modules.roles.associations import role_permissions


class Permission(BaseModel):
    __tablename__ = "permissions"

    __table_args__ = (
        UniqueConstraint(
            "resource",
            "action",
            name = "uq_permission_resource_action"
        ),
    )

    resource:Mapped[str] = mapped_column(String(100),nullable=False,index=True)
    action:Mapped[str] = mapped_column(String(50),nullable=False)
    code:Mapped[str] = mapped_column(String(150),unique=True,nullable=True,index=True)
    describtion:Mapped[str | None] = mapped_column(String(255),nullable=True)
    roles:Mapped[list["Role"]] = relationship(
        secondary="role_permissions",
        back_populates="permissions",
        lazy="selection",
    )


    def __repr__(self) -> str:
        return (
            f"Permission("
            f"id={self.id}, "
            f"code='{self.code}'"
            f")"
        )