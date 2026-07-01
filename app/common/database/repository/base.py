from __future__ import annotations

from typing import Any, Generic, Type, TypeVar
from sqlalchemy import select, Select
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    def __init__(self,model:Type[ModelType],db:AsyncSession):
        self.model = model
        self.db = db

    def query(self) -> Select:
        return select(self.model)
    
    async def get_by_id(self,id:Any,) -> ModelType | None:
        return await self.db.get(self.model,id)
    
    async def exixts(self,id:Any) -> bool:
        return await self.get_by_id(id) is not None
    
    async def create(self,obj:ModelType) -> ModelType:
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj
    
    async def save(self) -> None:
        await self.db.commit()

    async def refresh(self,obj:ModelType) -> None:
        await self.db.refresh(obj)

        