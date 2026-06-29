from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.common.mixins.base_model import BaseModel
from app.modules.roles.associations import role_permissions

if TYPE_CHECKING:
    from app.modules.users.model import User
    from app.modules.permissions.models import Permission


class Role(BaseModel):
    __tablename__ = "roles"

    name:Mapped[str] = mapped_column(String(100),unique=True,nullable=False,index=True)
    describtion:Mapped[str | None] = mapped_column(String(255),nullable=False)
    users:Mapped[list["User"]] = relationship(secondary=role_permissions,back_populates="role",lazy="selection")
    permissions:Mapped[list["Permission"]] = relationship(secondary=role_permissions,back_populates="role",lazy="selection")




def __repr__(self):

    return (
        f"Role("
        f"id={self.id}, "
        f"name='{self.name}')"
    )