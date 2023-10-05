from pydantic import BaseModel


class EOTMDetailBase(BaseModel):
    comment_detail: str
    commentor: str


class EOTMDetailInput(EOTMDetailBase):
    pass


class SAEOTMDetail(EOTMDetailBase):
    id: int

    class Config:
        from_attributes = True
