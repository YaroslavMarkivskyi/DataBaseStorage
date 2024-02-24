from sqlalchemy import Column, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    """
    Base model for all models.
    """
    __abstract__ = True
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
