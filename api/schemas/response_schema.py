from pydantic import BaseModel
from .employee_schema import SAEmployee
from .eotmdetail_schema import SAEOTMDetail
from typing import Union, TypeVar, Generic, List, Dict

T = TypeVar("T", bound=BaseModel)


class GenericSingleObject(BaseModel, Generic[T]):
    object: T


class GenericMultipleObjects(BaseModel, Generic[T]):
    objects: list[T]


class BaseGenericResponse(BaseModel):
    success: bool
    messages: List[str] | None = None
    status_code: int = 200


class GenericSingleResponse(BaseGenericResponse, Generic[T]):
    data: GenericSingleObject[T] | None = None


class GenericMultipleResponse(BaseGenericResponse, Generic[T]):
    data: GenericMultipleObjects[T] | None = None


class APIResponse(BaseModel):
    success: bool
    results: list[BaseModel] | None = None
    messages: list[str] | None = None
    status_code: int = 200


class CollectiveResponse(BaseModel):
    success: bool
    results: dict[str, list[Union[SAEmployee, SAEOTMDetail]]] | None = None
    messages: list[str] | None = None
    status_code: int = 200
