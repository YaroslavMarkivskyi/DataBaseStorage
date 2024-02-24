from sqlalchemy import Sequence, Integer, Column, ForeignKey

from model.base import Base


class Summary(Base):
    """
    Summary model class.
    """
    __tablename__ = "summaries"
    id = Column(Integer, Sequence('summary_id_seq'), primary_key=True)
    team = Column(ForeignKey('teams.id'), nullable=False)
    played = Column(Integer, nullable=False)
    won = Column(Integer, nullable=False)
    drawn = Column(Integer, nullable=False)
    lost = Column(Integer, nullable=False)
    goals_for = Column(Integer, nullable=False)
    goals_against = Column(Integer, nullable=False)
    goal_difference = Column(Integer, nullable=False)
