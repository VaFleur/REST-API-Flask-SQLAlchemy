from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    phone = Column(String(255), unique=True, nullable=False)

    emails = relationship('Email', backref='User', cascade="all, delete-orphan", single_parent=True)
    departments = relationship('Department', secondary='user_department_link')

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone
        }


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), nullable=False)
    users = relationship('User', secondary='user_department_link')


class UserDepartmentLink(Base):
    __tablename__ = "user_department_link"
    department_id = Column(Integer, ForeignKey("departments.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)


class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    adress = Column(String(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

