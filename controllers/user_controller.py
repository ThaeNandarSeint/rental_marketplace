from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas.user_schema import GetUsersResponse, UserCreate, UserOut, UserUpdate
from repositories.user_repository import UserRepository
from services.user_service import UserService
from usecases.user_usecase import UserUseCase
from services.password_service import PasswordService

router = APIRouter(prefix="/users", tags=["Users"])

def get_usecase():
    db = SessionLocal()
    repo = UserRepository(db)
    password_service = PasswordService()
    service = UserService(password_service, repo)
    return UserUseCase(service)

@router.get("/", response_model=GetUsersResponse)
def get_users(usecase: UserUseCase = Depends(get_usecase)):
    return usecase.get_users()

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, usecase: UserUseCase = Depends(get_usecase)):
    user = usecase.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.create_user(user)

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserUpdate, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.update_user(user_id, user)

@router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: int, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.delete_user(user_id)
