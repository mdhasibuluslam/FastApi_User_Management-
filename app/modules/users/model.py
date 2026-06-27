"""User ORM Model"""

from __future__ import annotations

import uuid
from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.base import Base


class User(Base):
    __tablename__ = "Users"
    
    id:Mapped[int] = mapped_column(primary_key=True,index=True) #primary key
    uuid:Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4,unique=True,nullable=False)    #public UUID
    username:Mapped[str] = mapped_column(String(50),unique=True,nullable=False) #Basic Information
    email:Mapped[str] = mapped_column(String(255),unique=True,nullable=False,index=True)
    hash_password:Mapped[str] = mapped_column(String(255),nullable=False)
    is_active:Mapped[bool] = mapped_column(Boolean,default=True)
    is_superuser:Mapped[bool] = mapped_column(Boolean,default=False)
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())
    role_id:Mapped[int] = mapped_column(ForeignKey("roles_id"),nullable=ForeignKey)
    role = relationship("Role",back_populates="users")

    
