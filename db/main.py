from typing import Final

import sqlalchemy as sql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from misc import SingletonMeta


class BaseModel(DeclarativeBase):
    id = sql.Column(sql.Integer, autoincrement=True, unique=True, primary_key=True)


class Database(metaclass=SingletonMeta):
    BASE: Final = declarative_base()

    def __init__(self, name: str):
        self.__engine = create_engine(f"sqlite:///{name}?check_same_thread=False")
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

        BaseModel.metadata.create_all(self.__engine)

    @property
    def session(self):
        return self.__session

    @property
    def engine(self):
        return self.__engine
