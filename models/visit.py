from sqlalchemy import Column, Integer, Sequence, ForeignKey, Date

from models.base_model import BaseModel


class Visit(BaseModel):
    """
    Models to create visit patient to doctor.
    """
    id = Column(Integer, Sequence('visit_id_seq'), primary_key=True, autoincrement=True)
    medical_card = Column(ForeignKey('medicalcards.id'), nullable=False)
    date = Column(Date, nullable=False)
