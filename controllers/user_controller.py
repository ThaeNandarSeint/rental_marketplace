from fastapi import APIRouter, Depends, Query 
from typing import Optional
from schemas.user_schema import CreateUser, GetUsersDto, GetUsersResponse, UpdateUser, User
from usecases.user_usecase import UserUseCase

router = APIRouter(prefix="/users", tags=["Users"])

def get_usecase():
    return UserUseCase()

def get_queries(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None)
) -> GetUsersDto:
    return GetUsersDto(skip=skip, limit=limit, search=search)

@router.get("/", response_model=GetUsersResponse)
def get_users(queries: GetUsersDto = Depends(get_queries),usecase: UserUseCase = Depends(get_usecase)):
    return usecase.get_users(queries)

@router.get("/{id}", response_model=User)
def get_user(id: int, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.get_user_by_id(id)

@router.post("/", response_model=User)
def create_user(data: CreateUser, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.create_user(data)

@router.patch("/{id}", response_model=User)
def update_user(id: int, data: UpdateUser, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.update_user(id, data)

@router.delete("/{id}", response_model=User)
def delete_user(id: int, usecase: UserUseCase = Depends(get_usecase)):
    return usecase.delete_user(id)
