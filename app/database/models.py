"""
Import all ORM models here.

Alembic imports this file so every model is
registered inside Base.metadata.
"""

from app.modules.users.model import User
from app.modules.roles.model import Role
from app.modules.permissions.models import Permission

__all__ = [
    "User",
    "Role",
    "Permission",
]