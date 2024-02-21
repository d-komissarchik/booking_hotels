from datetime import date

from sqlalchemy import delete, insert, select, and_, or_

from app.dao.base import BaseDAO
from app.bookings.models import Bookings


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(
        cls,
        room_id: int,
        date_from: date,
        date_to: date,
        ):
        booked_rooms = select(Bookings).where(
            and_(
                Bookings.room_id==1,
                or_(

                )
            )
        )