from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError 
from controllers import auth_controller, user_controller, tenant_controller, owner_controller, admin_controller, role_controller, category_controller, property_controller, location_controller, property_file_controller
from middlewares.auth_middleware import AuthMiddleware
from database import Base, engine

Base.metadata.create_all(bind=engine)

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

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    messages = []
    for err in errors:
        loc = err.get("loc", [])
        field = loc[-1] if loc else "field"
        msg = err.get("msg", "")
        messages.append(f"{field}: {msg}")

    return JSONResponse(
        status_code=400,
        content={
            "message": messages,
            "error": "Bad Request",
            "statusCode": 400
        }
    )

app.add_middleware(AuthMiddleware)

api_router = APIRouter(prefix="/api")
api_router.include_router(auth_controller.router)
api_router.include_router(user_controller.router)
api_router.include_router(tenant_controller.router)
api_router.include_router(owner_controller.router)
api_router.include_router(admin_controller.router)
api_router.include_router(role_controller.router)
api_router.include_router(category_controller.router)
api_router.include_router(property_controller.router)
api_router.include_router(location_controller.router)
api_router.include_router(property_file_controller.router)

app.include_router(api_router)
