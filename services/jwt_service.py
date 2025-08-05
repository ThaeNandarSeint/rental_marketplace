import jwt
import datetime
import os

SECRET_KEY = os.getenv('JWT_SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
EXPIRE_TIME = int(os.getenv('JWT_EXPIRE_TIME'))

class JWTService:
    @staticmethod
    def create_token(data: dict, expires_in_minutes: int = EXPIRE_TIME) -> str:
        payload = data.copy()
        payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(expires_in_minutes)
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def verify_token(token: str) -> dict:
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return decoded
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")
