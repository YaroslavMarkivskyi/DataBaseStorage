from sqlalchemy import Column, Integer, Sequence, ForeignKey

from models.base_model import BaseModel


class DoctorService(BaseModel):
    """
    Models to connect one of clinic doctor and one of clinic service. Replace relationship many-to-many.
    """
    id = Column(Integer, Sequence('doctor_service_id_seq'), primary_key=True, autoincrement=True)
    service_type = Column(ForeignKey('servicetypes.id'), nullable=False)
    doctor = Column(ForeignKey('doctors.id'), nullable=False)
