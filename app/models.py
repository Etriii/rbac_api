from sqlmodel import Field, SQLModel
from sqlalchemy import Column, JSON, String, DateTime, Enum as SAEnum, Boolean, Numeric
from datetime import datetime
from enum import Enum
from typing import Optional


class Roles(SQLModel, table=True):
    __tablename__ = "roles"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(100), unique=True, index=True))
    description: str = Field(sa_column=Column(String(1024), index=True))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )
    updated_by: int = Field(foreign_key="users.id", index=True, nullable=True)


class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column(String(255), unique=True, index=True))
    email: str = Field(sa_column=Column(String(255), unique=True, index=True))
    email_verified_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )
    hashed_password: str = Field(sa_column=Column(String(1024)))
    profile: str = Field(sa_column=Column(String(255), nullable=True))
    status: bool = Field(default=True, sa_column=Column(Boolean, nullable=False))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )
    updated_by: int = Field(foreign_key="users.id", index=True, nullable=True)


class UserRoles(SQLModel, table=True):
    __tablename__ = "user_roles"
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)
    role_id: int = Field(foreign_key="roles.id", index=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column=Column(DateTime, nullable=True)
    )
    updated_by: int = Field(foreign_key="users.id", index=True, nullable=True)


class LotsOfDataForPagination(SQLModel, table=True):
    _tablename_ = "lots_of_data_for_pagination"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(100)))
    created_at: datetime = Field(default_factory=datetime.now)
