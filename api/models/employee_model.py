from sqlalchemy import Column, Integer, Column, String, Boolean
from database import Base


class SQLAlchemyEmployee(Base):
    __tablename__ = "management_employee"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    job_title = Column(String)
    description = Column(String)
    current_month_recommends = Column(Integer)
    total_recommends = Column(Integer)
    number_of_likes = Column(Integer)
    eotm_wins = Column(Integer)
    is_eotm = Column(Boolean)
    image_url = Column(String, nullable=True)
