from schemas.response_schema import GenericMultipleResponse, GenericSingleResponse, GenericSingleObject, GenericMultipleObjects, GenericMultipleResponse
from schemas.employee_schema import SAEmployee, EmployeeInput
from services.auth_service import SECRET_KEY
from models.employee_model import SQLAlchemyEmployee
from sqlalchemy.orm import Session
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, Request
import jwt


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


# mode = increment or decrement
def change_like_count(db: Session, mode: str, request: Request) -> GenericSingleResponse[SAEmployee]:
    try:
        access_token = request.headers.get("access_token")
        if not access_token:
            error = ["Unauthorized"]
            return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=401)
        else:
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])
            user_id: str = payload.get("id")
            if user_id is None:
                error = ["Unauthorized: Missing ID"]
                return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=401)   
            eotm = db.query(SQLAlchemyEmployee).filter(
                SQLAlchemyEmployee.is_eotm == True)
            if mode == "increment":
                eotm.update(
                    {SQLAlchemyEmployee.number_of_likes: SQLAlchemyEmployee.number_of_likes+1})
                db.commit()
            elif mode == "decrement":
                eotm.update(
                    {SQLAlchemyEmployee.number_of_likes: SQLAlchemyEmployee.number_of_likes-1})
                db.commit()
            else:
                error = [
                    "Unprocessable entity: query parameter query_mode should be increment or decrement"]
                return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=422)
            data = GenericSingleObject[SAEmployee](object=eotm.first())
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
    
def get_employee_data(db: Session, user_id: int) -> GenericSingleResponse[SAEmployee]:
    try:
        user = db.query(SQLAlchemyEmployee).filter(SQLAlchemyEmployee.id == user_id)
        data = GenericSingleObject[SAEmployee](object=user.first())
        return GenericSingleResponse[SAEmployee](success=True, data=data)
    except SQLAlchemyError as e:
        error = [f"Error occurred while querying database: {str(e)}"]
        return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=500)
    except HTTPException as e:
        error = [f"HTTP exception has occurred: {str(e)}"]
        return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=403)
    except Exception as e:
        error = [f"An error has occurred: {str(e)}"]
        return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=500)   
        
def put_employee_data(db: Session, user_id: int, employee_data: EmployeeInput) -> GenericSingleResponse[SAEmployee]:
    try:
        user = db.query(SQLAlchemyEmployee).filter(SQLAlchemyEmployee.id == user_id).first()
        if not user:
            error = [f"User with id: {user_id} is not found"]
            return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=404)
        else:
            for key, value in employee_data.model_dump().items():
                setattr(user, key, value)
        db.commit()
        db.refresh(user)
        data = GenericSingleObject[SAEmployee](object=user)
        return GenericSingleResponse[SAEmployee](success=True, data=data)
    except SQLAlchemyError as e:
        error = [f"Error occurred while querying database: {str(e)}"]
        return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=500)
    except HTTPException as e:
        error = [f"HTTP exception has occurred: {str(e)}"]
        return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=403)
    except Exception as e:
        error = [f"An error has occurred: {str(e)}"]
        return GenericSingleResponse[SAEmployee](success=False, messages=error, status_code=500) 