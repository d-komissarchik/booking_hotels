from fastapi import APIRouter


router = APIRouter(
    prefix="/bookings",
    tags=["Бронювання"],
)


@router.get("")
def get_bookings():
    pass



@router.get("/booking_id")
def get_bookings(booking_id):
    pass

