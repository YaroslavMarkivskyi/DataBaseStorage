from sqlalchemy import Sequence, Integer, Column, ForeignKey

from models.base import BaseModel


class GroupSummary(BaseModel):
    """
    Group summary model class.
    """
    __tablename__ = "group_summaries"
    id = Column(Integer, Sequence('summary_id_seq'), primary_key=True, autoincrement=True)
    team = Column(ForeignKey('teams.id'), nullable=False)
    played = Column(Integer, nullable=False)
    won = Column(Integer, nullable=False)
    drawn = Column(Integer, nullable=False)
    lost = Column(Integer, nullable=False)
    goals_for = Column(Integer, nullable=False)
    goals_against = Column(Integer, nullable=False)
    goal_difference = Column(Integer, nullable=False)
    points = Column(Integer, nullable=False)
