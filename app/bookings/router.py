from fastapi import APIRouter
from sqlalchemy import select


from app.bookings.models import Bookings


router = APIRouter(
    prefix="/bookings",
    tags=["Бронювання"],
)

@router.get("")
async def get_bookings():
    pass
    # result = BookingService.get_all_bookings()
    # return result


# @router.get("")
# async def get_bookings():
#     async with async_session_maker() as session:
#         query = select(Bookings)
#         result = await session.execute(query)
#         return result.mappings().all()




