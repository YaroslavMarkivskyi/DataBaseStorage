from sqlalchemy import Sequence, Integer, Column, ForeignKey, String

from model.base import Base


class Tournament(Base):
    """
    Tournament model class.
    """
    __tablename__ = "tournaments"
    id = Column(Integer, Sequence('tournament_id_seq'), primary_key=True)
    type = Column(ForeignKey('tournament_types.id'), nullable=False)
    name = Column(String)
    season = Column(ForeignKey('seasons.id'), nullable=False)
    final_stadium = Column(String)
