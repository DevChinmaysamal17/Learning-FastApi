from typing import List
from pydantic import BaseModel
from typing import Optional


class BlogCreate(BaseModel):
    title: str
    body: str
    user_id: int


class Blog(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[ShowUser]

    class Config:
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None