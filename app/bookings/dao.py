from app.database import async_session_maker


class BookingDAO:

    @classmethod
    def find_all(cls):
        async with async_session_maker() as session:
            pass
