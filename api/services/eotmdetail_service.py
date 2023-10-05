from schemas.response_schema import GenericMultipleResponse
from schemas.eotmdetail_schema import EOTMDetailInput, SAEOTMDetail
from schemas.response_schema import GenericMultipleObjects, GenericMultipleResponse, GenericSingleObject, GenericSingleResponse
from models.eotmdetail_model import SQLAlchemyEOTMDetail
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException


def get_eotmdetail_data(db: Session) -> GenericMultipleResponse[SAEOTMDetail]:

    try:
        eotmdetail = db.query(SQLAlchemyEOTMDetail).all()
        data = GenericMultipleObjects[SAEOTMDetail](objects=eotmdetail)
        if eotmdetail:
            return GenericMultipleResponse[SAEOTMDetail](success=True, data=data)
        else:
            error = ["No comments found"]
            return GenericMultipleResponse[SAEOTMDetail](success=False, messages=error, status_code=404)
    except SQLAlchemyError as e:
        error = [f"Error occurred while querying database: {str(e)}"]
        return GenericMultipleResponse[SAEOTMDetail](success=False, messages=error, status_code=500)
    except HTTPException as e:
        error = [f"HTTP exception has occurred: {str(e)}"]
        return GenericMultipleResponse[SAEOTMDetail](success=False, messages=error, status_code=403)
    except Exception as e:
        error = [f"An error has occurred: {str(e)}"]
        return GenericMultipleResponse[SAEOTMDetail](success=False, messages=error, status_code=500)


def post_eotmdetail_data(db: Session, eotmdetail: EOTMDetailInput) -> GenericSingleResponse[SAEOTMDetail]:
    try:
        new_eotmdetail = SQLAlchemyEOTMDetail(**(eotmdetail.model_dump()))
        db.add(new_eotmdetail)
        db.commit()
        db.refresh(new_eotmdetail)
        data = GenericSingleObject[SAEOTMDetail](object=new_eotmdetail)
        return GenericSingleResponse[SAEOTMDetail](success=True, data=data)
    except SQLAlchemyError as e:
        error = [f"Error occurred while querying database: {str(e)}"]
        return GenericSingleResponse[SAEOTMDetail](success=False, messages=error, status_code=500)
    except HTTPException as e:
        error = [f"HTTP exception has occurred: {str(e)}"]
        return GenericSingleResponse[SAEOTMDetail](success=False, messages=error, status_code=403)
    except Exception as e:
        error = [f"An error has occurred: {str(e)}"]
        return GenericSingleResponse[SAEOTMDetail](success=False, messages=error, status_code=500)
