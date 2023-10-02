from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from services.employee_service import get_eotm, get_hall_of_fame
from schemas.employee_schema import SAEmployee, EmployeeInput
from schemas.response_schema import APIResponse

employee_router = APIRouter()


@employee_router.get("/get_eotm", response_model=APIResponse)
def get_the_eotm(db: Session = Depends(get_db)):
    return get_eotm(db)


@employee_router.post("/get_hof", response_model=APIResponse)
def get_hof(db: Session = Depends(get_db), query_type: str = "wins", number_limit: int = 5):
    return get_hall_of_fame(db, type=query_type, no_limit=number_limit)
