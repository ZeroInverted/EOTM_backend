from fastapi import APIRouter, Depends, Request
from schemas.response_schema import GenericMultipleResponse
from schemas.eotmdetail_schema import EOTMDetailInput, SAEOTMDetail
from services.collective_service import get_collective_data, post_collective_comment
from database import get_db
from sqlalchemy.orm import Session

collective_router = APIRouter()


@collective_router.get("/get_collective_data")
def get_collective_eotm(db: Session = Depends(get_db)):
    return get_collective_data(db)


@collective_router.post("/post_collective_comment", response_model=GenericMultipleResponse[SAEOTMDetail])
def create_collective_comment(eotm_detail: EOTMDetailInput, request: Request, db: Session = Depends(get_db)):
    return post_collective_comment(db=db, request=request, eotm_detail=eotm_detail)
