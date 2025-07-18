from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class RolesBase(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[int] = None
    

class RolesCreate(BaseModel):
    name: str
    description: str


class RolesResponse(BaseModel):
    status_code: int
    data: Optional[RolesBase] = None
    
class RolesListResponse(BaseModel):
    status_code: int
    data: List[RolesBase] = []