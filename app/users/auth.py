from jose import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# from secrets import token_bytes
# from base64 import b64encode
# print(b64encode(token_bytes(32)).decode())


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, "eY/DJIfBCNnlAzuqPn/b5Ggdrw17KEdoIMZCcaWYfd4=", "HS256"
    )
    return encoded_jwt



