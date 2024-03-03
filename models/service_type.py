from sqlalchemy import Column, Integer, Sequence, String

from models.base_model import BaseModel


class ServiceType(BaseModel):
    """
    Models to describe a type of services in clinic.
    """
    id = Column(Integer, Sequence('service_type_id_seq'), primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)
    description = Column(String(100), nullable=False)
    price = Column(Integer)
