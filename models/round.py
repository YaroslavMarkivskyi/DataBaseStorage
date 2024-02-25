from sqlalchemy import Column, Integer, Sequence, ForeignKey

from models.base import BaseModel


class Round(BaseModel):
    """
    Round class for the tournament stage.
    """
    __tablename__ = 'rounds'
    id = Column(Integer, Sequence('round_id_seq'), primary_key=True, autoincrement=True)
    stage = Column(ForeignKey('stages.id'), nullable=False)
    team_1 = Column(ForeignKey('round_summaries.id'), nullable=False)
    team_2 = Column(ForeignKey('round_summaries.id'), nullable=False)
    games = Column(Integer, nullable=False, default=2)
