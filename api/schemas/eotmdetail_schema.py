from pydantic import BaseModel


class EOTMDetailBase(BaseModel):
    comment_detail: str
    commentor: int


class EOTMDetailInput(EOTMDetailBase):
    pass


class SAEOTMDetail(EOTMDetailBase):
    id: int

    class Config:
        from_attributes = True
