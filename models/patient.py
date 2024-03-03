from sqlalchemy import Column, Integer, Sequence, Date, ForeignKey
from models.base_model import BaseModel


class Patient(BaseModel):
    """
    Models to describe a patient in clinic.
    """
    id = Column(Integer, Sequence('patient_id_seq'), primary_key=True, autoincrement=True)
    user = Column(ForeignKey('users.id'), nullable=False)
    gender = Column(ForeignKey('genders.id'), nullable=False)
    birth_day = Column(Date, nullable=False)
