from fastapi import APIRouter
from services.auth_service import employee_login, employee_logout
from schemas.auth_schema import LoginModel, GeneralAuthResponse, LoginAuthResponse

auth_router = APIRouter()


@auth_router.post("/employee_login", response_model=LoginAuthResponse)
def auth_login(login_credentials: LoginModel):
    return employee_login(login_credentials=login_credentials)

@auth_router.post("/employee_logout", response_model=GeneralAuthResponse)
def auth_login():
    return employee_logout()

