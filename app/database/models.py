from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.mixin import MixinCRUD
from hashlib import sha1
from typing import List

__all__ = [
    "Base",
    "User",
    "Email",
    "Department",
    "UserDepartment"
]

Base = declarative_base()


class User(Base, MixinCRUD):
    __tablename__ = 'users'
    _hidden = {"password", "username"}

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(unique=True, nullable=False)

    emails: Mapped[List["Email"]] = relationship(back_populates="user")
    department: Mapped["UserDepartment"] = relationship(back_populates="users")

    @staticmethod
    def get_password_hash(password: str) -> str:
        hasher = sha1()
        hasher.update(password.encode("utf-8"))
        return hasher.hexdigest()


class Department(Base, MixinCRUD):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    users: Mapped[List["UserDepartment"]] = relationship(back_populates="department")


class UserDepartment(Base, MixinCRUD):
    __tablename__ = "users_departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    department: Mapped["Department"] = relationship(back_populates="users", foreign_keys=[department_id])
    users: Mapped["User"] = relationship(back_populates="department", foreign_keys=[user_id])


class Email(Base, MixinCRUD):
    __tablename__ = 'emails'

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(unique=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    user: Mapped["User"] = relationship(back_populates="emails", foreign_keys=[user_id])
