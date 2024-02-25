from sqlalchemy import Sequence, Integer, Column, ForeignKey, String

from models.base import BaseModel


class Match(BaseModel):
    """
    Match model class.
    """
    __tablename__ = "matches"
    id = Column(Integer, Sequence('match_id_seq'), primary_key=True, autoincrement=True)
    match_date = Column(ForeignKey('match_dates.id'), nullable=False)
    result = Column(ForeignKey('results.id'), nullable=False)
    referee = Column(String)