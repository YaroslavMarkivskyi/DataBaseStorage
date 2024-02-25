from sqlalchemy import Sequence, Integer, Column, ForeignKey

from model.base import BaseModel


class RoundSummary(BaseModel):
    """
    Summary model class.
    """
    __tablename__ = "round_summaries"
    id = Column(Integer, Sequence('summary_id_seq'), primary_key=True, autoincrement=True)
    team = Column(ForeignKey('teams.id'), nullable=False)
    played = Column(Integer, nullable=False)
    goals_for = Column(Integer, nullable=False)
    goals_against = Column(Integer, nullable=False)
    goal_difference = Column(Integer, nullable=False)
