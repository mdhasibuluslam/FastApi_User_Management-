from fastapi import Depends
from app.database.session import DBsession
from app.modules.users.repository import UserRepository
from app.modules.users.service import UserService


def get_user_repository(db:DBsession) -> UserRepository:
    return UserRepository(db)

def grt_user_service(repository: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(repository)