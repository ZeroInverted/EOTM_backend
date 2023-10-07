from pydantic import BaseModel


class LoginModel(BaseModel):
    username: str
    password: str

class LoginAuthResponse(BaseModel):
    access_token: str | None
    
class LogoutAuthResponse(BaseModel):
    success: bool