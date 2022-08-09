from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    phone = Column(String(255), unique=True, nullable=False)

    email = relationship('Email', backref='User', cascade="all, delete-orphan", single_parent=True)


class Department(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True, autoincrement="auto")
    department = Column(String(255), nullable=False)
    user_department = relationship('UserDepartment')


class UserDepartment(Base):
    __tablename__ = "user_department"
    department_id = Column(ForeignKey("departments.department_id"), primary_key=True)
    user_id = Column(ForeignKey("users.user_id"), primary_key=True)
    extra_data = Column(String(50))
    user = relationship("User")


class Email(Base):
    __tablename__ = 'emails'
    email_id = Column(Integer, primary_key=True, autoincrement="auto")
    email = Column(String(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))

