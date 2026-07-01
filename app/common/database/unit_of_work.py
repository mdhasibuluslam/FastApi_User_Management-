from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.users.repository import UserRepository
from app.modules.roles.repository import RoleRepository
from app.modules.permissions.repository import PermissionRepository

class UnitWork:
    def __init__(self,db:AsyncSession):
        self.db = db
        self.users = UserRepository(db)
        self.roles = RoleRepository(db)
        self.permissions = PermissionRepository(db)
    
    async def __aenter__(self):
            return self
    async def __aexit__(self, exc_type, exc, tb):
            if exc:
                await self.rollback()
            else:
                await self.commit()
            await self.db.close()

    async def commit(self) -> None:
        await self.db.commit()

    async def rollback(self) -> None:
        await self.db.rollback()

    async def refresh(self,obj) -> None:
        await self.db.refresh(obj)