from sqlalchemy import Sequence, Integer, Column, ForeignKey

from model.base import BaseModel


class Stage(BaseModel):
    """
    Base class for inheriting Group and Round classes .
    """
    tournament = Column(ForeignKey('tournaments.id'), nullable=False)
