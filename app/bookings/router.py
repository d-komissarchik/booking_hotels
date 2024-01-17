from fastapi import APIRouter

from app.bookings.dao import BookingDAO


router = APIRouter(
    prefix="/bookings",
    tags=["Бронювання"],
)


@router.get("")
async def get_bookings():
    return BookingDAO.find_all()


# @router.get("")
# async def get_bookings():
#     async with async_session_maker() as session:
#         query = select(Bookings)
#         result = await session.execute(query)
#         return result.mappings().all()




