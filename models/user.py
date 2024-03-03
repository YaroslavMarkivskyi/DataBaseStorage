from sqlalchemy import Column, Integer, Sequence, String

from models.base_model import BaseModel


class User(BaseModel):
    """
    Models to describe a patient in clinic.
    """
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, autoincrement=True)
    first_name = Column(String(20), nullable=False)
    name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(128), nullable=False)
