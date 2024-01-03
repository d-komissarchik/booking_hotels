from fastapi import FastAPI
from typing import Optional
from datetime import date


app = FastAPI()


@app.get("/hotels")
async def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = None,
        ):
    return date_from, date_to


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}





#if __name__ == 'main':

