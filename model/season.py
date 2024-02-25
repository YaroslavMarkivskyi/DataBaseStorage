from sqlalchemy import Sequence, Integer, Column, Date, String

from model.base import BaseModel


class Season(BaseModel):
    """
    Season model class.
    """
    __tablename__ = "seasons"
    id = Column(Integer, Sequence('season_id_seq'), primary_key=True, autoincrement=True)
    name = Column(String)
    start_year = Column(Date, nullable=False)
    end_year = Column(Date, nullable=False)
