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

    def __repr__(self):
        return f"<User id{self.user_id} {self.username}>"

class Phone(Base):
    __tablename__ = 'phones'
    phone_id = Column(Integer, primary_key=True, autoincrement="auto")
    phone = Column(String(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    user = relationship('User', backref='phone', uselist=False)  # Один пользователь

    def __repr__(self):
        return f"{self.phone}"

class Email(Base):
    __tablename__ = 'emails'
    email_id = Column(Integer, primary_key=True, autoincrement="auto")
    email = Column(String(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    user = relationship('User', backref='email', uselist=False)  # Один пользователь

    def __repr__(self):
        return f"{self.email}"

class Department(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True, autoincrement="auto")
    department = Column(String(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    user = relationship('User', backref='department')  # Много пользователей

    def __repr__(self):
        return f"{self.department}"
