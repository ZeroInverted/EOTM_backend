from schemas.response_schema import GenericMultipleResponse, GenericSingleResponse, GenericSingleObject, GenericMultipleObjects, GenericMultipleResponse
from schemas.employee_schema import SAEmployee
from models.employee_model import SQLAlchemyEmployee
from sqlalchemy.orm import Session
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException


def get_eotm_data(db: Session) -> GenericSingleResponse[SAEmployee]:
    try:
        eotm = db.query(SQLAlchemyEmployee).filter(
            SQLAlchemyEmployee.is_eotm == True).first()
        data = GenericSingleObject[SAEmployee](object=eotm)
        if eotm:
            return GenericSingleResponse[SAEmployee](success=True, data=data)
        else:
            error = ["Employee of The Month not found"]
            return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=404)
    except SQLAlchemyError as e:
        error = [f"Error occurred while querying database: {str(e)}"]
        return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=500)
    except HTTPException as e:
        error = [f"HTTP exception has occurred: {str(e)}"]
        return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=403)
    except Exception as e:
        error = [f"An error has occurred: {str(e)}"]
        return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=500)


def get_hof_data(db: Session, type: str = "wins", no_limit: int = 5) -> GenericMultipleResponse[SAEmployee]:
    try:
        if (type == "wins"):
            hof = db.query(SQLAlchemyEmployee).order_by(
                desc(SQLAlchemyEmployee.eotm_wins)).limit(no_limit)
            data = GenericMultipleObjects[SAEmployee](objects=hof)
            return GenericMultipleResponse[SAEmployee](success=True, data=data)
        elif (type == "recommends"):
            hof = db.query(SQLAlchemyEmployee).order_by(
                desc(SQLAlchemyEmployee.total_recommends)).limit(no_limit)
            data = GenericMultipleObjects[SAEmployee](objects=hof)
            return GenericMultipleResponse[SAEmployee](success=True, data=data)
        else:
            error = ["Bad request, please check your query parameters."]
            return GenericMultipleResponse[SAEmployee](success=False, messages=error, status_code=400)
    except SQLAlchemyError as e:
        error = [f"Error occurred while querying database: {str(e)}"]
        return GenericMultipleResponse[SAEmployee](success=False, messages=error, status_code=500)
    except HTTPException as e:
        error = [f"HTTP exception has occurred: {str(e)}"]
        return GenericMultipleResponse[SAEmployee](success=False, messages=error, status_code=403)
    except Exception as e:
        return GenericMultipleResponse[SAEmployee](success=False, messages=error, status_code=500)
