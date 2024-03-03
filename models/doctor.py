from sqlalchemy import Column, Integer, Sequence, String, ForeignKey

from models.base_model import BaseModel


class Doctor(BaseModel):
    """
    Models to describe a doctor in clinic.
    """
    id = Column(Integer, Sequence('doctor_id_seq'), primary_key=True, autoincrement=True)
    user = Column(ForeignKey('users.id'), nullable=False)
    education = Column(String(50), nullable=False)
