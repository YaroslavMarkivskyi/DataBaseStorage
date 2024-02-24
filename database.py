import psycopg2
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker

from model.base import Base


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
        self.__engine = create_engine(self._compose_db_url())
        self.__con.autocommit = True
        self._create_database()

    def _create_database(self):
        try:
            self.__con.cursor().execute(f"CREATE DATABASE {self.__db_name}")
        except (exc.ProgrammingError, psycopg2.errors.DuplicateDatabase):
            pass
        finally:
            self.__con.close()

    def _compose_db_url(self):
        return f"postgresql://{self.__db_user}:{self.__db_password}@{self.__db_url}/{self.__db_name}"
