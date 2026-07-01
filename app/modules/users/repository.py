from sqlalchemy import select
from app.common.database.repository.base import BaseRepository
from app.modules.users.model import User

class UserRepository(BaseRepository[User]):
    def __init__(self, db):
        super().__init__(User, db)
    
    async def get_by_email(self,email:str) -> User | None:
        stmt = (self.query().where(User.email == email))
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_by_username(self,username:str) -> User | None:
        stmt = (self.query().where(User.username == username))
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def email_exists(self,email:str) -> bool:
        return (await self.get_by_email(email)) is not None

    async def username_exists(self,username:str) -> bool:
        return (await self.get_by_username(username)) is not None
    
     