from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime


class UserBase(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    email_verified_at: Optional[datetime] = None
    # password_hash: str
    profile: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None

    class Config:
        from_attributes = True


class UserCreateBase(BaseModel):
    username: str
    email: str
    password_hash: str


class UserBaseUpdate(UserBase):
    password_hash: Optional[str] = None


class UserResponse(BaseModel):
    status_code: int
    data: Optional[UserBase] = None


class UserListResponse(BaseModel):
    status_code: int
    data: List[UserBase] = []
