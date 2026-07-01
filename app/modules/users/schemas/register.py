from pydantic import EmailStr, Field
from app.modules.users.schemas.base import BaseSchema

class UserCreate(BaseSchema):
    username:str = Field(min_length=3,max_length=30)
    email:EmailStr
    password:str = Field(min_length=8,max_length=128)