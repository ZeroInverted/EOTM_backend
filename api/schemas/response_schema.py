from pydantic import BaseModel
from .employee_schema import SAEmployee


class APIResponse(BaseModel):
    success: bool
    results: list[SAEmployee] | None = None
    messages: str | None = None
    status_code: int = 200
