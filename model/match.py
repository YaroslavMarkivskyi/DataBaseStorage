from sqlalchemy import Sequence, Integer, Column, ForeignKey, String

from model.base import Base


class Match(Base):
    """
    Match model class.
    """
    __tablename__ = "matches"
    id = Column(Integer, Sequence('match_id_seq'), primary_key=True)
    match_date = Column(ForeignKey('match_dates.id'), nullable=False)
    result = Column(ForeignKey('results.id'), nullable=False)
    referee = Column(String)
