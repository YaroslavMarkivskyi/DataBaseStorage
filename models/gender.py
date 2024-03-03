from sqlalchemy import Column, Integer, Sequence, String

from models.base_model import BaseModel


class Gender(BaseModel):
    """
    Models to describe gender for patient.
    """
    id = Column(Integer, Sequence('gender_id_seq'), primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    