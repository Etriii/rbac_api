from pydantic import BaseModel
from typing import List


class Role(BaseModel):
    id: int
    name: str


class UserData(BaseModel):
    user_id: int
    role: Role
    
    


class UserLogin(BaseModel):
    username: str
    password: str
