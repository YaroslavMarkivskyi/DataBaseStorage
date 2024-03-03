import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


class Database:
    """
    Database class to handle all database operations.
    """

    def __init__(self, db_type: str, db_host: str, db_name: str, db_user: str, db_password: str, port: int = 5432):
        self.__db_type = db_type
        self.__db_host = db_host
        self.__db_name = db_name
        self.__db_user = db_user
        self.__db_password = db_password
        self.__port = port
        self.__con = psycopg2.connect(
            database=self.__db_type,
            user=self.__db_user,
            password=self.__db_password,
            host=self.__db_host,
            port=self.__port,
        )
        self.__con.autocommit = True
        self.__engine = create_engine(self._compose_db_url(), echo=True)
        self.__Session = sessionmaker(bind=self.__engine)

        BaseModel.metadata.create_all(self.__engine)

    def add_record(self, model_instance):
        """Method to add a record to the database."""
        with self.__Session() as session:
            session.add(model_instance)
            session.commit()
            session.refresh(model_instance)

    def get_all_records(self, model):
        """Method to get all records of a given model."""
        with self.__Session() as session:
            return session.query(model).all()

    def get_record_by_condition(self, model, condition):
        """Method to get a record by a given condition."""
        with self.__Session() as session:
            return session.query(model).filter(condition).first()

    def update_record(self, model_instance):
        """Method to update a record in the database."""
        with self.__Session() as session:
            session.merge(model_instance)
            session.commit()
            session.refresh(model_instance)

    def delete_record(self, model_instance):
        """Method to delete a record from the database."""
        with self.__Session() as session:
            session.delete(model_instance)
            session.commit()
            session.refresh(model_instance)


    def _compose_db_url(self):
        return f"{self.__db_type}ql://{self.__db_user}:{self.__db_password}@{self.__db_host}/{self.__db_name}"
