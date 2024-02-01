from datetime import datetime

from fastapi import Request, HTTPException, Depends, status
from jose import jwt, JWTError
from app.config import info
from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get("bookings_acces_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token


async def get_current_user(token:str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, info.secret_key, info.algorithm
        )
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await UsersDAO.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user