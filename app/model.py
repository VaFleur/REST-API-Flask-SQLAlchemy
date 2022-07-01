from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config import pg_user, pg_password, pg_host, db_name

Base = declarative_base()
engine = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{db_name}')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))

    def __repr__(self):
        return f"<User {self.id} {self.username}>"

class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column(String(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', uselist=False, backref='phone')  # Один пользователь

    def __repr__(self):
        return f"<User {self.id} {self.phone}>"

class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', uselist=False, backref='email')  # Один пользователь

    def __repr__(self):
        return f"<User {self.id} {self.email}>"

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    department = Column(String(255), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', backref='department')  # Много пользователей

    def __repr__(self):
        return f"<User {self.id} {self.department}>"

Base.metadata.create_all(engine)