import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from settings.settings import app_settings
from typing import Dict, Any

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(user_password: str) -> str:
    return pwd_context.hash(user_password)

def verify_hashed_password(user_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(user_password, hashed_password)


def create_jwt_access_token(data: Dict[str, Any], expire_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire_delta = (datetime.now() +
                    (expire_delta or timedelta(minutes=int(app_settings.jwt_expiry))))
    to_encode.update({
        "uid": data["uid"],
        "iss": "remainder_server",
        "exp": int(expire_delta.timestamp())
    })
    return jwt.encode(
        payload=to_encode,
        key=app_settings.jwt_secret_key,
        algorithm=app_settings.jwt_algorithm
    )


def decode_jwt_access_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(
            jwt=token,
            key=app_settings.jwt_secret_key,
            algorithms=[app_settings.jwt_algorithm]
        )
        decoded_token = {
            "status": "success",
            "message": "success",
            "payload": payload
        }
        return decoded_token

    except jwt.ExpiredSignatureError:
        decoded_token = {
            "status": "failed",
            "message": "Token has been expired",
            "payload": {}
        }
        return decoded_token

    except jwt.PyJWTError:
        decoded_token = {
            "status": "failed",
            "message": "Invalid Token",
            "payload": {}
        }
        return decoded_token
