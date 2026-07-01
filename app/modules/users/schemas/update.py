from pydantic import EmailStr, Field
from app.modules.users.schemas.base import BaseSchema
from typing import Optional

class UserUpdate(BaseSchema):
    username:Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=30,
    )

    email: Optional[EmailStr] = None
    full_name: Optional[str] = None


    