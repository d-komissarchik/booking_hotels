from fastapi import Request, HTTPException, Depends


def get_token(request: Request):
    token = request.cookies.get("bookings_acces_token")
    if not token:
        raise HTTPException(status_code=401)
    return token


def get_current_user(token:str = Depends(get_token)):
    return  "user"