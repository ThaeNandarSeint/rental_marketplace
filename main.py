from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from database import engine, Base
from controllers import auth_controller, user_controller

app = FastAPI()

Base.metadata.create_all(bind=engine)

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

app.include_router(auth_controller.router)
app.include_router(user_controller.router)
