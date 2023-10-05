from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session

collective_router = APIRouter()


@collective_router.get("/get_collective_data")
def get_collective(db: Session = Depends(get_db)):
    # TODO: implement service
    pass
