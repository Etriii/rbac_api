from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from ..db import get_db

from ..models import User
from ..schemas.user_schema import (
    UserBase,
    UserBaseUpdate,
    UserCreateBase,
    UserListResponse,
    UserResponse,
)


router = APIRouter(tags=["Users"])


@router.get("/", response_model=UserListResponse)
async def get_all_users(
    db: Session = Depends(get_db),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    try:
        users = db.exec(select(User).offset(offset).limit(limit)).all()
        return UserListResponse(status_code=200, data=users)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error {e}")
