from sqlalchemy import Column, Integer, Sequence, String

from models.base import BaseModel


class Team(BaseModel):
    """
    Team model class.
    """
    __tablename__ = "teams"
    id = Column(Integer, Sequence('team_id_seq'), primary_key=True, autoincrement=True)
    name = Column(String)
    stadium = Column(String)
    coach = Column(String)
    country = Column(String)
    city = Column(String)
