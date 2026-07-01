from main import app
from app.modules.users.repository import UserRepository
from app.modules.users.service import UserService
from fastapi import Depends
from app.modules.users.dependencies import grt_user_service

@app.post("/register")
async def register(data:UserCreate, service: UserService = Depends(grt_user_service)):
    