from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from services.collective_service import get_collective_data
from schemas.response_schema import APIResponse

collective_router = APIRouter()


@collective_router.get("/get_collective_data", response_model=APIResponse)
def get_collective(db: Session = Depends(get_db)):
    return get_collective_data(db)
