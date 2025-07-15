from fastapi import APIRouter, Depends, HTTPException
from schemas.user_schema import GetUsersResponse, UserCreate, UserOut, UserUpdate
from usecases.user_usecase import UserUseCase

router = APIRouter(prefix="/users", tags=["Users"])

def get_usecase():
    return UserUseCase()

@router.get("/", response_model=GetUsersResponse)
def get_users(usecase: UserUseCase = Depends(get_usecase)):
    return usecase.get_users()

@router.get("/{id}", response_model=UserOut)
def get_user(id: int, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.get_user_by_id(id)

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.create_user(user)

@router.put("/{id}", response_model=UserOut)
def update_user(id: int, user: UserUpdate, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.update_user(id, user)

@router.delete("/{id}", response_model=UserOut)
def delete_user(id: int, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.delete_user(id)
