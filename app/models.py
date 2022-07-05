from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config import pg_user, pg_password, pg_host, db_name

Base = declarative_base()
engine = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{db_name}')

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))

    def __init__(self, user_id, username, password, first_name, last_name):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"<User id{self.user_id} {self.username}>"

class Phone(Base):
    __tablename__ = 'phones'
    phone_id = Column(Integer, primary_key=True, autoincrement="auto")
    phone = Column(String(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    user = relationship('User', uselist=False, backref='phone')  # Один пользователь

    def __init__(self, phone_id, phone, user_id):
        self.phone_id = phone_id
        self.phone = phone
        self.user_id = user_id

    def __repr__(self):
        return f"<User id{self.id} {self.phone}>"

class Email(Base):
    __tablename__ = 'emails'
    email_id = Column(Integer, primary_key=True, autoincrement="auto")
    email = Column(String(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    user = relationship('User', uselist=False, backref='email')  # Один пользователь

    def __init__(self, email_id, email, user_id):
        self.email_id = email_id
        self.email = email
        self.user_id = user_id

    def __repr__(self):
        return f"<User id{self.id} {self.email}>"

class Department(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True, autoincrement="auto")
    department = Column(String(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    user = relationship('User', backref='department')  # Много пользователей

    def __init__(self, department_id, department, user_id):
        self.department_id = department_id
        self.department = department
        self.user_id = user_id

    def __repr__(self):
        return f"<User id{self.id} {self.department}>"

Base.metadata.create_all(engine)
