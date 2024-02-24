
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey

from model.base import Base


class Player(Base):
    """
    Player model class.
    """
    __tablename__ = "players"

    id = Column(Integer, Sequence('player_id_seq'), primary_key=True)
    name = Column(String)
    age = Column(Integer)
    team = Column(ForeignKey('teams.id'), nullable=True, default=None)
    position = Column(String)
