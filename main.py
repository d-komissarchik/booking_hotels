from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel


app = FastAPI()


class SHotel(BaseModel):
    address: str
    name: str
    stars: int

list[SHotel]

@app.get("/hotels")
async def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
        ):
    hotels = [
        {
            "address": "вул. Наукова, 1",
            "name": "Super Hotel",
            "stars": 5
        },
    ]
    return date_from, date_to


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date



@app.post("/bookings")
def add_booking(booking: SBooking):
    pass






# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}





#if __name__ == 'main':

