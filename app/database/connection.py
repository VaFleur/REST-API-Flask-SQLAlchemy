from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from flask import Flask
from sqlalchemy.engine.url import URL
from config import config


class PGContextSession:
    __engine = None

    def __int__(self):
        self.__session_instance: Session = None

    def __enter__(self) -> Session:
        self.__session_instance = self.__sessionmaker()
        return self.__session_instance

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session_instance.close()

    @classmethod
    def setup(cls, app: Flask):
        cls.__engine = create_engine(URL.create(**config["postgres"]))
        cls.__sessionmaker = sessionmaker(
            bind=cls.__engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
            class_=Session
        )
