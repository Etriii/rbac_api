from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

class UserRolesBase(BaseModel):
    id: Optional[int] = None
    user_id: int
    role_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    
class UserRolesCreate(BaseModel):
    user_id: int
    role_id: int
    
class UserRolesResponse(BaseModel):
    status_code: int
    data: Optional[UserRolesBase] = None
    
class UserRolesResponse(BaseModel):
    status_code: int
    data: List[UserRolesBase] = None
    