from schemas.response_schema import APIResponse
from schemas.eotmdetail_schema import EOTMDetailInput, SAEOTMDetail
from models.eotmdetail_model import SQLAlchemyEOTMDetail
from sqlalchemy.orm import Session
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException


def get_eotmdetail_data(db: Session) -> APIResponse:

    try:
        eotmdetail = db.query(SQLAlchemyEOTMDetail).all()
        if eotmdetail:
            return APIResponse(success=True, results=eotmdetail)
        else:
            error = ["No comments found"]
            return APIResponse(success=False, messages=error, status_code=404)
    except SQLAlchemyError as e:
        error = [f"Error occurred while querying database: {str(e)}"]
        return APIResponse(success=False, messages=error, status_code=500)
    except HTTPException as e:
        error = [f"HTTP exception has occurred: {str(e)}"]
        return APIResponse(success=False, messages=error, status_code=403)
    except Exception as e:
        error = [f"An error has occurred: {str(e)}"]
        return APIResponse(success=False, messages=error, status_code=500)


def post_eotmdetail_data(db: Session, eotmdetail: EOTMDetailInput) -> APIResponse:

    new_eotmdetail = SAEOTMDetail(**(eotmdetail.model_dump()))
    try:
        db.add(new_eotmdetail)
        db.commit()
        db.refresh(new_eotmdetail)
        return APIResponse(success=True, results=new_eotmdetail)
    except SQLAlchemyError as e:
        error = [f"Error occurred while querying database: {str(e)}"]
        return APIResponse(success=False, messages=error, status_code=500)
    except HTTPException as e:
        error = [f"HTTP exception has occurred: {str(e)}"]
        return APIResponse(success=False, messages=error, status_code=403)
    except Exception as e:
        return APIResponse(success=False, messages=error, status_code=500)
