from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.main import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронювання"],
)


@router.get("")
async def get_bookings() -> SBooking:
    return await BookingDAO.find_one_or_none(room_id=3)


# @router.get("")
# async def get_bookings():
#     async with async_session_maker() as session:
#         query = select(Bookings)
#         result = await session.execute(query)
#         return result.mappings().all()




