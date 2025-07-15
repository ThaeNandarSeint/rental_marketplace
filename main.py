from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from controllers import auth_controller, user_controller
from middlewares.auth_middleware import AuthMiddleware

app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={
                "message": f"Cannot {request.method} {request.url.path}",
                "error": "Not Found",
                "status_code": 404
            }
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
            "status_code": exc.status_code
        }
    )

app.add_middleware(AuthMiddleware)

api_router = APIRouter(prefix="/api")
api_router.include_router(auth_controller.router)
api_router.include_router(user_controller.router)

app.include_router(api_router)
