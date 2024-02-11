from fastapi import HTTPException, status


UserAlreadyExists = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Користувач вже існує"
)

