from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship,  declarative_base

Base = declarative_base()


class SQLAlchemyEmployee(Base):
    __tablename__ = "management_employee"
    id = Column(Integer, primary_key=True)
    username = String(length=150)
    password = String(length=128)
    is_superuser = Boolean()
    first_name = String(length=150)
    last_name = String(length=150)
    email = String(length=255)
    is_staff = Boolean()
    is_active = Boolean()
    job_title = String(length=128)
    total_recommends = Integer()
    current_month_recommends = Integer()
    eotm_wins = Integer()
    is_eotm = Boolean()
    image_url = String(length=200)
