from sqlalchemy import Column, Integer, Sequence, String, ForeignKey

from model.stage import Stage


class Round(Stage):
    """
    Round class for the tournament stage.
    """
    __tablename__ = 'rounds'
    id = Column(Integer, Sequence('round_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    team_1 = Column(ForeignKey('summaries.id'), nullable=False)
    team_2 = Column(ForeignKey('summaries.id'), nullable=False)
    games = Column(Integer, nullable=False, default=2)
