from fastapi import APIRouter, Depends, Request
from database import get_db
from sqlalchemy.orm import Session
from services.eotmdetail_service import get_eotmdetail_data, post_eotmdetail_data
from schemas.response_schema import GenericMultipleResponse, GenericSingleResponse
from schemas.eotmdetail_schema import EOTMDetailInput, SAEOTMDetail

eotmdetail_router = APIRouter()


@eotmdetail_router.get("/get_eotmdetail", response_model=GenericMultipleResponse[SAEOTMDetail])
def get_all_comments(db: Session = Depends(get_db)):
    return get_eotmdetail_data(db)


@eotmdetail_router.post("/add_eotmdetail", response_model=GenericSingleResponse[SAEOTMDetail])
def create_comment(eotmdetail: EOTMDetailInput, request: Request, db: Session = Depends(get_db)):
    return post_eotmdetail_data(db=db, request=request, eotmdetail=eotmdetail)
