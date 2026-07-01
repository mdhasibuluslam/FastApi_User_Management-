from uuid import UUID
from pydantic import EmailStr
from app.modules.users.schemas.base import BaseSchema, IDSchema


class UserResponse(IDSchema):
    username: str
    email: EmailStr
    is_active: bool
    role_id: UUID | None


