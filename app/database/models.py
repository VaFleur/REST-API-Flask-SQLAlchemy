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

    articles = relationship('Article', order_by='desc(Article.id)', primaryjoin='User.id == Article.user_id')

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

    comments = relationship('Comment', order_by='desc(Comment.id)', primaryjoin='Article.id == Comment.article_id')


class Comment(Base, MixinCRUD):
    __tablename__ = 'comment_table'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('article_table.id'))
    body = Column(Text, nullable=False)
