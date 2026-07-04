from fastapi import APIRouter, Depends

from app.modules.auth.dependencies import (
    get_auth_service,
    get_current_user,
)
from app.modules.auth.service import AuthService
from app.modules.users.schemas import (
    UserCreate,
    LoginRequest,
    UserResponse,
)
from app.modules.users.model import User

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
async def register(
    data: UserCreate,
    service: AuthService = Depends(get_auth_service),
):

    user = await service.register(
        username=data.username,
        email=data.email,
        password=data.password,
    )

    return user

@router.post("/login")
async def login(
    data: LoginRequest,
    service: AuthService = Depends(get_auth_service),
):

    tokens = await service.login(
        email=data.email,
        password=data.password,
    )

    if not tokens:
        return {"error": "Invalid credentials"}

    return tokens

@router.get("/me", response_model=UserResponse)
async def me(
    user: User = Depends(get_current_user),
):

    return user