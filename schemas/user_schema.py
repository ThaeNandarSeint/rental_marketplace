from pydantic import BaseModel, EmailStr

class BaseUser(BaseModel):
    name: str
    email: EmailStr
    password: str

class CreateUser(BaseUser):
    pass

class UpdateUser(BaseUser):
    pass

class User(BaseUser):
    id: int

class GetUsersResponse(BaseModel):
    data: list[User]
    count: int

class GetUsersDto(BaseModel):
    skip: int
    limit: int
    search: str