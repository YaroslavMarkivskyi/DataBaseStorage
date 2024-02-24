from sqlalchemy import Sequence, Integer, Column, ForeignKey

from model.base import Base


class Stage(Base):
    """
    Base class for inheriting Group and Round classes .
    """
    tournament = Column(ForeignKey('tournaments.id'), nullable=False)
