from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class SQLAlchemyEOTMDetail(Base):
    __tablename__ = "management_eotmdetail"
    id = Column(Integer, primary_key=True)
    comment_detail = String(length=600)
    number_of_likes = Integer()
    commentor_id = Column(Integer, ForeignKey("management_employee.id"))

    sa_employee = relationship(
        "SQLAlchemyEmployee", back_populates="sa_eotmdetails")
