from pydantic import BaseModel
from typing import TypeVar, Generic, List

T = TypeVar("T", bound=BaseModel)


class GenericSingleObject(BaseModel, Generic[T]):
    object: T


class GenericMultipleObjects(BaseModel, Generic[T]):
    objects: List[T]


class BaseGenericResponse(BaseModel):
    success: bool
    messages: List[str] | None = None
    status_code: int = 200


class GenericSingleResponse(BaseGenericResponse, Generic[T]):
    data: GenericSingleObject[T] | None = None


class GenericMultipleResponse(BaseGenericResponse, Generic[T]):
    data: GenericMultipleObjects[T] | None = None
