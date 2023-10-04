from schemas.response_schema import CollectiveResponse, APIResponse
from models.employee_model import SQLAlchemyEmployee
from models.eotmdetail_model import SQLAlchemyEOTMDetail
from sqlalchemy.orm import Session
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from employee_service import get_eotm_data
from eotmdetail_service import get_eotmdetail_data


def get_collective_data(db: Session) -> CollectiveResponse:
    try:
        eotm = get_eotm_data(db)
        comments = get_eotmdetail_data(db)
        if not isinstance(eotm, APIResponse) and not isinstance(comments, APIResponse):
            return CollectiveResponse(success=True, results={
                "employee": eotm,
                "comments": comments,
            })
    except Exception as e:
        error = [f"An error has occurred {str(e)}"]
        return CollectiveResponse(success=False, messages=error, status_code=500)
