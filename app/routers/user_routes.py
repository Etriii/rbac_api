from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from ..db import get_db


from ..schemas.user_schema import UserBase, UserBaseUpdate, UserCreateBase, UserListResponse, UserResponse

router = APIRouter(tags=["Users"])

