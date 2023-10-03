from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from services.employee_service import get_eotm_data, get_hof_data
from schemas.response_schema import APIResponse

employee_router = APIRouter()


@employee_router.get("/get_eotm", response_model=APIResponse)
def get_eotm(db: Session = Depends(get_db)):
    return get_eotm_data(db)


@employee_router.get("/get_hof", response_model=APIResponse)
def get_hof(db: Session = Depends(get_db), query_type: str = "wins", number_limit: int = 5):
    return get_hof_data(db, type=query_type, no_limit=number_limit)
