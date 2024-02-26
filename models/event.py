from sqlalchemy import Column, Integer, Sequence, String, ForeignKey

from models.base import BaseModel


class Event(BaseModel):
    """
    Event model class.
    """
    __tablename__ = "events"
    id = Column(Integer, Sequence('event_id_seq'), primary_key=True, autoincrement=True)
    match_id = Column(ForeignKey('matches.id'), nullable=False)
    event_type = Column(ForeignKey('event_types.id'), nullable=False)
    event_minute = Column(Integer, nullable=False)
    player_id = Column(ForeignKey('players.id'), nullable=False)
