from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    """
    Database class to handle all database operations.
    """
    def __init__(self, db_url: str, db_name: str, db_user: str, db_password: str):
        self.__db_url = db_url
        self.__db_name = db_name
        self.__db_user = db_user
        self.__db_password = db_password

        self.__engine = create_engine(f'{self.__db_url}://{self.__db_user}:{self.__db_password}@{self.__db_name}',
                                      echo=True)
        self.Session = sessionmaker(bind=self.__engine)
