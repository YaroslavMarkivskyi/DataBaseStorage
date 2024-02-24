from sqlalchemy import Column, Integer, Sequence, String

from base import Base


class Event(Base):
    """
    Event model class.
    """
    __tablename__ = "events"

    id = Column(Integer, Sequence('event_id_seq'), primary_key=True)
    name = Column(String)
