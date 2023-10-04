from pydantic import BaseModel
from .employee_schema import SAEmployee
from .eotmdetail_schema import SAEOTMDetail
from typing import Union, Generic


class APIResponse(BaseModel):
    success: bool
    results: Union[list[SAEmployee], list[SAEOTMDetail]] | None = None
    messages: list[str] | None = None
    status_code: int = 200


class CollectiveResponse(BaseModel):
    success: bool
    results: dict[str, list[Union[SAEmployee, SAEOTMDetail]]] | None = None
    messages: list[str] | None = None
    status_code: int = 200
