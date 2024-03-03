from sqlalchemy import Column, Integer, Sequence, ForeignKey, String

from models.base_model import BaseModel


class Service(BaseModel):
    """
    Models to describe a services in clinic.
    """
    id = Column(Integer, Sequence('service_id_seq'), primary_key=True, autoincrement=True)
    doctor_service = Column(ForeignKey('doctorservices.id'), nullable=False)
    visit = Column(ForeignKey('visits.id'), nullable=False)
    description = Column(String(100), nullable=False)
    conclution = Column(String(100), nullable=False)
