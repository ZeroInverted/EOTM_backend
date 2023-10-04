from schemas.response_schema import CollectiveResponse
from sqlalchemy.orm import Session
from .employee_service import get_eotm_data
from .eotmdetail_service import get_eotmdetail_data


def get_collective_data(db: Session) -> CollectiveResponse:
    try:
        eotm = get_eotm_data(db)
        comments = get_eotmdetail_data(db)
        if eotm["success"] == True and comments["success"] == True:
            return CollectiveResponse(success=True, results={
                "employee": eotm,
                "comments": comments,
            })
        elif eotm["success"] == False:
            return CollectiveResponse(False, messages=eotm["messages"], status_code=eotm["status_code"])
        elif comments["success"] == False:
            return CollectiveResponse(False, messages=comments["messages"], status_code=comments["status_code"])
    except Exception as e:
        error = [f"An error has occurred {str(e)}"]
        return CollectiveResponse(success=False, messages=error, status_code=500)
