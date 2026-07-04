from app.common.security.jwt import create_access_token, create_refresh_token
from app.common.security.password import verify_pass, hashed_pass
from app.modules.users.repository import UserRepository

class AuthService:
    def __init__(self,user_repo:UserRepository):
        self.user_repo = user_repo
    async def register(
        self,
        username:str,
        email:str,
        password:str
    ):
        existing = await self.user_repo.get_by_email(email)
        if existing:
            raise Exception("Email already exists")
        
        hashed_pass = hashed_pass(password)

        user = self.user_repo.model(
            username = username,
            email = email,
            password = hashed_pass,
            is_active = True
        )

        await self.user_repo.create(user)
        return user
    
    async def login(self,email:str,password:str):
        user = await self.user_repo.get_by_email(email)
        if not user:
            return None
        if not verify_pass(password,user.hashed_password):
            return None
        
        access = create_access_token(str(user.id))
        refresh = create_refresh_token(str(user.id))

        return {
            "access_token": access,
            "refresh_token": refresh,
            "token_type": "bearer",
        }