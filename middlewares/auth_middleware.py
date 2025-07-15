from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from services.jwt_service import JWTService

PUBLIC_ROUTES = ["/api/auth/register", "/api/auth/login"]

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        if path in PUBLIC_ROUTES:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=401,
                content={"status_code": 401, "message": "Unauthorized"},
            )

        token = auth_header.split(" ")[1]

        try:
            user = JWTService.verify_token(token)
            request.state.user = user
        except Exception as e:
            return JSONResponse(
                status_code=401,
                content={"status_code": 401, "message": "Unauthorized"},
            )

        return await call_next(request)
