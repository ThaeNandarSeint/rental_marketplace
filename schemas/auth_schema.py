from pydantic import BaseModel, EmailStr
from schemas.user_schema import UserBase, UserOut

class Login(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    token: str
    user: UserOut

class Register(UserBase):
    pass

class RegisterResponse(BaseModel):
    token: str
    user: UserOut
