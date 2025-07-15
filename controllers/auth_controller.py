from fastapi import APIRouter, Depends
from schemas.auth_schema import Login, LoginResponse, Register, RegisterResponse
from usecases.auth_usecase import AuthUseCase

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_usecase():
    return AuthUseCase()

@router.post("/register", response_model=RegisterResponse)
def register_user(data: Register, auth_usecase: AuthUseCase = Depends(get_usecase)):
    return auth_usecase.register(data)

@router.post("/login", response_model=LoginResponse)
def register_user(user: Login, auth_usecase: AuthUseCase = Depends(get_usecase)):
    return auth_usecase.login(user)
