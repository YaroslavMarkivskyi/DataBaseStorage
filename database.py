import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import *


class Database:
    """
    Database class to handle all database operations.
    """

    def __init__(self, db_url: str, db_name: str, db_user: str, db_password: str, port: int = 5432):
        self.__db_url = db_url
        self.__db_name = db_name
        self.__db_user = db_user
        self.__db_password = db_password
        self.__port = port
        self.__con = psycopg2.connect(
            database="postgres",
            user=self.__db_user,
            password=self.__db_password,
            host=self.__db_url,
            port=self.__port,
        )
        self.__engine = create_engine(self._compose_db_url(), echo=True)
        self.__con.autocommit = True
        self.__Session = sessionmaker(bind=self.__engine)

        BaseModel.metadata.create_all(self.__engine)

    def _compose_db_url(self):
        return f"postgresql://{self.__db_user}:{self.__db_password}@{self.__db_url}/{self.__db_name}"
