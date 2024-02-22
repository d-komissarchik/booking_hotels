from datetime import date

from sqlalchemy import delete, insert, select, and_, or_, func

from app.dao.base import BaseDAO
from app.bookings.models import Bookings
from app.rooms.models import Rooms


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
                Bookings.room_id == 1,
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_from <= date_to
                    ),
                    and_(
                        Bookings.date_from <= date_from,
                        Bookings.date_to > date_from
                    ),
                )
            )
        ).cte("booked_rooms")

        rooms_left = select(
            Rooms.quantity - func.count(booked_rooms.room_id)
                            ).select_from(Rooms)
