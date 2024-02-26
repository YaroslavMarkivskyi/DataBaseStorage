from sqlalchemy import String, Column, Integer, Sequence

from models import BaseModel


class EventType(BaseModel):
    """
    EventType model class.
    """
    __tablename__ = "event_types"
    id = Column(Integer, Sequence('event_type_id_seq'), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
