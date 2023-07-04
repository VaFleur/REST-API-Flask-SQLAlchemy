from sqlalchemy import ForeignKey, Integer, String, Text, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database.mixin import MixinCRUD
from hashlib import sha1

__all__ = [
    "Base",
    "User",
    "Article",
    "Comment"
]

Base = declarative_base()


class User(Base, MixinCRUD):
    __tablename__ = 'user_table'
    _hidden = {"password", "username"}

    id = Column(Integer, primary_key=True)
    username = Column(String,  unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)

    articles = relationship('Article', back_populates='user', uselist=True)

    @staticmethod
    def get_password_hash(password: str) -> str:
        hasher = sha1()
        hasher.update(password.encode("utf-8"))
        return hasher.hexdigest()


class Article(Base, MixinCRUD):
    __tablename__ = 'article_table'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_table.id'))
    header = Column(String, unique=True, nullable=False)
    body = Column(Text, nullable=False)

    user = relationship('User', back_populates='articles', foreign_keys='article_table.user_id')
    comments = relationship('Article', back_populates='article', uselist=True)


class Comment(Base, MixinCRUD):
    __tablename__ = 'comment_table'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('article_table.id'))
    body = Column(Text, nullable=False)

    article = relationship('Article', back_populates='comments', foreign_keys='comment_table.article_id')
