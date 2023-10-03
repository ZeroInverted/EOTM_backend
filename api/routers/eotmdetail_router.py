from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from services.eotmdetail_service import get_eotmdetail_data, post_eotmdetail_data
from schemas.response_schema import APIResponse
from schemas.eotmdetail_schema import EOTMDetailInput

eotmdetail_router = APIRouter()


@eotmdetail_router.get("/get_eotmdetail", response_model=APIResponse)
def get_eotm(db: Session = Depends(get_db)):
    return get_eotmdetail_data(db)


@eotmdetail_router.post("/add_eotmdetail", response_model=APIResponse)
def get_hof(eotmdetail: EOTMDetailInput, db: Session = Depends(get_db)):
    return post_eotmdetail_data(db, eotmdetail)
