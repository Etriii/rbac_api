from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session, select, or_

from ..db import get_db

from ..models import User, Roles, UserRoles
from ..schemas.auth_schema import UserData, UserLogin, Role


router = APIRouter(tags=["Auth"])


@router.post(
    "/login",
    response_model=UserData,
    summary="Login with email or username",
    description="Accepts either a username or email in the 'username' field and password to authenticate.",
)
async def login(form_data: UserLogin, db: Session = Depends(get_db)):
    user = db.exec(
        select(User).where(
            or_(User.username == form_data.username, User.email == form_data.username),
            User.hashed_password == form_data.password,
        )
    ).first()

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username")

    # user_role  = db.exec(select(UserRoles).where(UserRoles.user_id == user.id)).first()

    # role = db.exec(select(Roles).where(Roles.id == user_role.role_id)).first()

    role = db.exec(
        select(Roles)
        .join(UserRoles, UserRoles.role_id == Roles.id)
        .where(UserRoles.user_id == user.id)
    ).first()

    if not role:
        raise HTTPException(status_code=403, detail="User has no role")
    print(role)
    return UserData(user_id=user.id, role=Role(id=role.id, name=role.name))
