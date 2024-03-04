from fastapi import HTTPException, status


class BookingExceptions(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingExceptions):
    status_code = status.HTTP_409_CONFLICT,
    detail = "Користувач вже існує"


class IncorrectEmailOrPasswordException(BookingExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Пошта або пароль не вірний"


class TokenExpireException(BookingExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Токен минув"


class TokenAbsentException(BookingExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Токен відсутній"


class IncorrectTokenFormatException(BookingExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Неправильний формат токена"


class UserIsNotPresentException(BookingExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED


class RoomCannotBeBooked(BookingExceptions):
    status_code = status.HTTP_409_CONFLICT,
    detail = "Не залишилось свободних номерiв"
