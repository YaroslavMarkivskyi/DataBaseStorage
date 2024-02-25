from sqlalchemy import Sequence, Integer, Column, ForeignKey, String

from model.base import BaseModel


class Tournament(BaseModel):
    """
    Tournament model class.
    """
    __tablename__ = "tournaments"
    id = Column(Integer, Sequence('tournament_id_seq'), primary_key=True)
    type = Column(ForeignKey('tournament_types.id'), nullable=False)
    name = Column(String)
    season = Column(ForeignKey('seasons.id'), nullable=False)
    final_stadium = Column(String)
