from sqlalchemy import Sequence, Integer, Column, ForeignKey

from model.base import Base


class Result(Base):
    """
    Result model class.
    """
    __tablename__ = "results"

    id = Column(Integer, Sequence('result_id_seq'), primary_key=True)
    match_id = Column(ForeignKey('matches.id'), nullable=False)
    home_team = Column(ForeignKey('teams.id'), nullable=False)
    away_team = Column(ForeignKey('teams.id'), nullable=False)
