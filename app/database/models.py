from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import MixinCRUD
from hashlib import sha1

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

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)

    department = relationship("UserDepartment", back_populates='users')

    @staticmethod
    def get_password_hash(password: str) -> str:
        hasher = sha1()
        hasher.update(password.encode("utf-8"))
        return hasher.hexdigest()


class Email(Base, MixinCRUD):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True, autoincrement="auto")
    adress = Column(String, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', foreign_keys=[user_id], backref="emails")


class Department(Base, MixinCRUD):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String, nullable=False)

    users = relationship("UserDepartment", back_populates='department')


class UserDepartment(Base, MixinCRUD):
    __tablename__ = "users_departments"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship('User', foreign_keys=[user_id], back_populates="department")
    department = relationship("Department", foreign_keys=[department_id], back_populates="users")
