from fastapi import APIRouter, Depends
from database import SessionLocal
from repositories.user_repository import UserRepository
from services.user_service import UserService
from schemas.auth_schema import Login, LoginResponse, Register, RegisterResponse
from usecases.auth_usecase import AuthUseCase
from services.password_service import PasswordService
from services.jwt_service import JWTService

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_usecase():
    db = SessionLocal()
    repo = UserRepository(db)
    password_service = PasswordService()
    jwt_service = JWTService()
    user_service = UserService(password_service, repo)
    return AuthUseCase(user_service, password_service, jwt_service)

@router.post("/register", response_model=RegisterResponse)
def register_user(data: Register, auth_usecase: AuthUseCase = Depends(get_usecase)):
    return auth_usecase.register(data)

@router.post("/login", response_model=LoginResponse)
def register_user(user: Login, auth_usecase: AuthUseCase = Depends(get_usecase)):
    return auth_usecase.login(user)
