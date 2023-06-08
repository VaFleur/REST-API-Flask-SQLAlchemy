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
]

Base = declarative_base()


class User(Base, MixinCRUD):
    __tablename__ = 'user_table'
    _hidden = {"password", "username"}

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(unique=True, nullable=False)
    department_id: Mapped[int] = mapped_column(ForeignKey("department_table.id"))

    emails: Mapped[List["Email"]] = relationship(back_populates="user")
    department: Mapped["Department"] = relationship(back_populates="users")

    @staticmethod
    def get_password_hash(password: str) -> str:
        hasher = sha1()
        hasher.update(password.encode("utf-8"))
        return hasher.hexdigest()


class Email(Base, MixinCRUD):
    __tablename__ = 'email_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(unique=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))

    user: Mapped["User"] = relationship(back_populates="emails")


class Department(Base, MixinCRUD):
    __tablename__ = 'department_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    department: Mapped[str] = mapped_column(unique=True, nullable=False)

    users: Mapped[List["User"]] = relationship(back_populates="department")
