from app.modules.users.model import User
from app.modules.users.repository import UserRepository


class UserService:
    def __init__(self,respository:UserRepository):
        self.repository = respository

    async def is_email_available(self,email:str) -> bool:
        return not await self.repository.email_exists(email)
    
    async def is_username_available(self,username:str) -> bool:
        return not await self.repository.username_exists(username)