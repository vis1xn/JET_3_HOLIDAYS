from pydantic import BaseModel, EmailStr, constr
from datetime import date

class UserSignUp(BaseModel):
    username: constr(min_length=3, max_length=10)
    name: constr(max_length=10)
    email: EmailStr
    password: constr(min_length=4)
    DOB: date

class UserLogin(BaseModel):
    email: EmailStr
    password: constr