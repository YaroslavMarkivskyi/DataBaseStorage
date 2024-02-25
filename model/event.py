from sqlalchemy import Column, Integer, Sequence, String

from base import BaseModel


class Event(BaseModel):
    """
    Event model class.
    """
    __tablename__ = "events"

    id = Column(Integer, Sequence('event_id_seq'), primary_key=True)
    name = Column(String)
