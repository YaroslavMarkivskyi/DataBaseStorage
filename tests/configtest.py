import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from business.core.config import Config


@pytest.fixture(scope="session")
def database_url():
    db_type = Config.DB_TYPE
    db_host = Config.DB_HOST
    db_name = Config.DB_NAME
    db_user = Config.DB_USER
    db_pass = Config.DB_PASS
    return f"{db_type}://{db_user}:{db_pass}@{db_host}/test_database"


@pytest.fixture(scope="session")
def engine(database_url):
    engine = create_engine(database_url)
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def session(engine):
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()
