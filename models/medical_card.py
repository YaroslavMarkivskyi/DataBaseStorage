from sqlalchemy import Column, Integer, Sequence, ForeignKey

from models.base_model import BaseModel


class MedicalCard(BaseModel):
    """
    Models to describe a personal medical card of patients.
    """
    id = Column(Integer, Sequence('medical_card_id_seq'), primary_key=True, autoincrement=True)
    patient = Column(ForeignKey('users.id'), nullable=False)
