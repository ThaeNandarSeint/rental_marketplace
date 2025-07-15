from pydantic import BaseModel, EmailStr
from schemas.user_schema import BaseUser, User

class Login(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    token: str
    user: User

class Register(BaseUser):
    pass

class RegisterResponse(BaseModel):
    token: str
    user: User
