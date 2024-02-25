from sqlalchemy import Integer, Column, ForeignKey, String

from model.base import BaseModel


class Stage(BaseModel):
    """
    Base class for inheriting Group and Round classes .
    """
    __tablename__ = "stages"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    tournament = Column(ForeignKey('tournaments.id'), nullable=False)
