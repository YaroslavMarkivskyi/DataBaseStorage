from sqlalchemy import Sequence, Integer, Column, Date, ForeignKey

from model.base import Base


class MatchDate(Base):
    """
    MatchDay model class.
    """
    __tablename__ = "match_dates"
    id = Column(Integer, Sequence('match_date_id_seq'), primary_key=True)
    stage = Column(ForeignKey('stages.id'), nullable=False)
    date = Column(Date, nullable=False)
