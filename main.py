from fastapi import FastAPI

app = FastAPI()


@app.get("/hotels")
async def get_hotels():
    return {"Hotel 5 stars"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


#if __name__ == 'main':

