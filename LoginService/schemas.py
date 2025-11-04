from pydantic import BaseModel, EmailStr, constr, Field
from datetime import date
from typing import Optional

class UserSignUp(BaseModel):
    username: constr(min_length=3, max_length=10)
    name: constr(max_length=10)
    email: EmailStr
    password: constr(min_length=4)
    dateofbirth: date
   
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: constr(min_length=4)