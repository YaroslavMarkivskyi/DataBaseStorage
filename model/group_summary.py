from sqlalchemy import Sequence, Integer, Column

from model.summary import Summary


class GroupSummary(Summary):
    """
    Group summary model class.
    """
    __tablename__ = "group_summaries"
    id = Column(Integer, Sequence('group_summary_id_seq'), primary_key=True)
    points = Column(Integer, nullable=False)
