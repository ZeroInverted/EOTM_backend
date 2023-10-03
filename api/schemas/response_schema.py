from pydantic import BaseModel
from .employee_schema import SAEmployee
from .eotmdetail_schema import SAEOTMDetail
from typing import Union


class APIResponse(BaseModel):
    success: bool
    results: Union[list(SAEmployee), list(SAEOTMDetail)] | None = None
    messages: str | None = None
    status_code: int = 200
