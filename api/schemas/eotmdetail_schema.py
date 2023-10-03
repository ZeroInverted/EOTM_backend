from pydantic import BaseModel


class EOTMDetailBase(BaseModel):
    comment_detail: str
    number_of_likes = int
    commentor_id = int


class EOTMDetailInput(EOTMDetailBase):
    pass


class SAEOTMDetail(EOTMDetailBase):
    id: int

    class Config:
        from_attributes = True
