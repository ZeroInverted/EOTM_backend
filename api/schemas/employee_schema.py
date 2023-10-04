from pydantic import BaseModel


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    job_title: str
    current_month_recommends: int
    total_recommends: int
    number_of_likes: int
    eotm_wins: int
    is_eotm: bool
    image_url: str | None


class EmployeeInput(EmployeeBase):
    pass


class SAEmployee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True
