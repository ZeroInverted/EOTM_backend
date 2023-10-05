from sqlalchemy import Column, Integer, String
from database import Base


class SQLAlchemyEOTMDetail(Base):
    __tablename__ = "management_eotmdetail"
    id = Column(Integer, primary_key=True)
    comment_detail = Column(String)
    commentor = Column(String)
