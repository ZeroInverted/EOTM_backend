from fastapi import APIRouter, Depends, Request
from database import get_db
from sqlalchemy.orm import Session
from services.employee_service import get_eotm_data, get_hof_data, change_like_count, get_employee_data, put_employee_data
from schemas.response_schema import GenericSingleResponse, GenericMultipleResponse
from schemas.employee_schema import SAEmployee, EmployeeInput

employee_router = APIRouter()


@employee_router.get("/get_eotm", response_model=GenericSingleResponse[SAEmployee])
def get_eotm(db: Session = Depends(get_db)):
    return get_eotm_data(db)


@employee_router.get("/get_hof", response_model=GenericMultipleResponse[SAEmployee])
def get_hof(db: Session = Depends(get_db), query_type: str = "wins", number_limit: int = 5):
    return get_hof_data(db, type=query_type, no_limit=number_limit)

@employee_router.get("/get_employee", response_model=GenericSingleResponse[SAEmployee])
def get_employee_by_id(user_id: int, db: Session = Depends(get_db)):
    return get_employee_data(db=db, user_id=user_id)

@employee_router.put("/update_employee", response_model=GenericSingleResponse[SAEmployee])
def put_employee_by_id(user_id: int, employee_data: EmployeeInput, db: Session = Depends(get_db)):
    return put_employee_data(db=db, user_id=user_id, employee_data=employee_data)

@employee_router.patch("/patch_like_count", response_model=GenericSingleResponse[SAEmployee])
def patch_like_count(query_mode: str, request: Request, db: Session = Depends(get_db)):
    return change_like_count(db, request=request, mode=query_mode)
