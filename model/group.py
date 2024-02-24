from sqlalchemy import Column, Integer, Sequence, String, ForeignKey

from model.stage import Stage


class Group(Stage):
    """
    Group model class.
    """
    __tablename__ = "groups"

    id = Column(Integer, Sequence('group_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    team_1 = Column(ForeignKey('group_summaries.id'), nullable=False)
    team_2 = Column(ForeignKey('group_summaries.id'), nullable=False)
    team_3 = Column(ForeignKey('group_summaries.id'), nullable=False)
    team_4 = Column(ForeignKey('group_summaries.id'), nullable=False)
