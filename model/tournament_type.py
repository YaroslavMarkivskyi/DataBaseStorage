from sqlalchemy import Integer, Column, Sequence, String

from model.base import BaseModel


class TournamentType(BaseModel):
    """
    TournamentType model class.
    """
    __tablename__ = "tournament_types"
    id = Column(Integer, Sequence('tournament_type_id_seq'), primary_key=True)
    name = Column(String)
    description = Column(String)
    teams = Column(Integer)
    groups = Column(Integer)
    rounds = Column(Integer)
    matches = Column(Integer)
    duration = Column(Integer)
