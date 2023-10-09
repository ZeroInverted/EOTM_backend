from fastapi import APIRouter, Request
from services.auth_service import employee_login, employee_logout, employee_password_reset
from schemas.auth_schema import LoginModel, GeneralAuthResponse, LoginAuthResponse

auth_router = APIRouter()


@auth_router.post("/employee_login", response_model=LoginAuthResponse)
def auth_login(login_credentials: LoginModel):
    return employee_login(login_credentials=login_credentials)

@auth_router.post("/employee_logout", response_model=GeneralAuthResponse)
def auth_logout():
    return employee_logout()

@auth_router.post("/employee_password_reset", response_model=GeneralAuthResponse)
def auth_password_reset(password_reset_credentials: LoginModel, request: Request):
    return employee_password_reset(password_reset_credentials=password_reset_credentials, request=request)