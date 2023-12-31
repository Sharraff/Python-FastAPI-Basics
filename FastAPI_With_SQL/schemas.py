import pydantic as _pydantic
import datetime as _dt
from typing import List


class _PostBase(_pydantic.BaseModel):
    tittle: str
    content: str


class PostCreate(_PostBase):
    pass


class Post(_PostBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    class Config:
        from_attributes = True


class _UserBase(_pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    password: str

class User(_UserBase):
    id: int
    is_active: bool
    posts:List[Post] = []

    class Config:
        from_attributes = True
    