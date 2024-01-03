from fastapi import FastAPI

app = FastAPI()


@app.get("/hotels/{hotel_id}")
async def get_hotels(hotel_id: int, date_from, date_to):
    return f"Hotel - {hotel_id}"


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


#if __name__ == 'main':

