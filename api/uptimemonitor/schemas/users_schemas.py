from pydantic import BaseModel, PositiveInt, ConfigDict, Field, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    email: EmailStr = Field(min_length=3, max_length=255)
    password: str = Field(min_length=12, max_length=128)


class UserResponse(BaseModel):
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)
    user_id: PositiveInt
    created_at: datetime
    email_verified_at: datetime | None
    role_id: int