from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

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
    sa_eotmdetails = relationship(
        "SQLAlchemyEOTMDetail", back_populates="sa_employee")


class SQLAlchemyEOTMDetail(Base):
    __tablename__ = "management_eotmdetail"
    id = Column(Integer, primary_key=True)
    comment_detail = String(length=600)
    number_of_likes = Integer()
    commentor_id = Column(Integer, ForeignKey("management_employee.id"))

    sa_employee = relationship(
        "SQLAlchemyEmployee", back_populates="sa_eotmdetails")
