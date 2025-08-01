
from fastapi import HTTPException
from schemas.auth_schema import Register
from services.user_service import UserService
from services.tenant_service import TenantService
from services.owner_service import OwnerService
from services.password_service import PasswordService
from services.jwt_service import JWTService
from schemas.user_schema import RegisterUserType

class AuthUseCase:
    def __init__(self):
        self.user_service = UserService()
        self.tenant_service = TenantService()
        self.owner_service = OwnerService()
        self.password_service = PasswordService()
        self.jwt_service = JWTService()

    def register(self, data: Register):
        user = self.user_service.create_user(data)

        if data.type == RegisterUserType.TENANT:
            self.tenant_service.create_tenant({'user_id': user.id})

        if data.type == RegisterUserType.OWNER:
            self.owner_service.create_owner({'user_id': user.id})

        token = self.jwt_service.create_token({'user_id': user.id})
        return { "user": user, "token": token }
    
    def login(self, data: Register):
        user = self.user_service.get_user_by_email(data.email)
        if not user:
            raise HTTPException(status_code=400, detail="Wrong credentials.")
        
        is_correct_password = self.password_service.verify(data.password, user.password)
        if not is_correct_password:
            raise HTTPException(status_code=400, detail="Wrong credentials.")
        
        token = self.jwt_service.create_token({'user_id': user.id})
        return { "user": user, "token": token }
