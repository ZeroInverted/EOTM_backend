from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, Request
from models.employee_model import SQLAlchemyEmployee
from models.eotmdetail_model import SQLAlchemyEOTMDetail
from schemas.response_schema import GenericMultipleObjects, GenericMultipleResponse
from schemas.eotmdetail_schema import EOTMDetailInput, SAEOTMDetail
from services.auth_service import SECRET_KEY
import jwt

# API architecture as per request of Daniel Habib[Frontend dev]

# As per Daniel's request, this API service returns eotm details and comments

def get_collective_data(db: Session):
    try:
        eotm = db.query(SQLAlchemyEmployee).filter(
            SQLAlchemyEmployee.is_eotm == True).first()
        comments = db.query(SQLAlchemyEOTMDetail).all()
        collective_dict = {
            "success": True,
            "employee": eotm,
            "comments": comments
        }
        return collective_dict
    except Exception as e:
        error = [f"An error has occurred {str(e)}"]
        error_dict = {
            "success": False,
            "messages": error
        }
        return error_dict


# As per Daniel's request, when posting a comment, this service returns all comments.

def post_collective_comment(db: Session, request: Request, eotm_detail: EOTMDetailInput) -> GenericMultipleResponse[SAEOTMDetail]:
    try:
        access_token = request.headers.get("access_token")
        if not access_token:
            error = ["Unauthorized"]
            return GenericMultipleResponse[SAEOTMDetail](success=False, messages=error, status_code=401)
        else:
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
            user_id: str = payload.get("id")
            if user_id is None:
                error = ["Unauthorized: Missing ID"]
                return GenericMultipleResponse[SAEOTMDetail](success=False, messages=error, status_code=401)
        new_eotm_detail = SQLAlchemyEOTMDetail(**(eotm_detail.model_dump()))
        db.add(new_eotm_detail)
        db.commit()
        db.refresh(new_eotm_detail)
        all_comments = db.query(SQLAlchemyEOTMDetail).all()
        data = GenericMultipleObjects[SAEOTMDetail](objects=all_comments)
        return GenericMultipleResponse[SAEOTMDetail](success=True, data=data)
    except SQLAlchemyError as e:
        error = [f"Error occurred while querying database: {str(e)}"]
        return GenericMultipleResponse[SAEOTMDetail](success=False, messages=error, status_code=500)
    except HTTPException as e:
        error = [f"HTTP exception has occurred: {str(e)}"]
        return GenericMultipleResponse[SAEOTMDetail](success=False, messages=error, status_code=403)
    except Exception as e:
        error = [f"An error has occurred: {str(e)}"]
        return GenericMultipleResponse[SAEOTMDetail](success=False, messages=error, status_code=500)
