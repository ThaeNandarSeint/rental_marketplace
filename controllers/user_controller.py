from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas.user_schema import UserCreate, UserUpdate, UserOut
from repositories.user_repository import UserRepository
from services.user_service import UserService
from usecases.user_usecase import UserUseCase

router = APIRouter(prefix="/users", tags=["Users"])

def get_usecase():
    db = SessionLocal()
    repo = UserRepository(db)
    service = UserService(repo)
    return UserUseCase(service)

@router.get("/", response_model=list[UserOut])
def get_users(usecase: UserUseCase = Depends(get_usecase)):
    return usecase.list_users()

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, usecase: UserUseCase = Depends(get_usecase)):
    user = usecase.retrieve_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.add_user(user)

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserUpdate, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.modify_user(user_id, user)

@router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: int, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.remove_user(user_id)
