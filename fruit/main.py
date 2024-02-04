from fastapi import FastAPI, Query

from fruit.src.data import destroy_database, initialize_database
from fruit.src.service import create_fruit, get_fruit_by_id, get_fruits
from fruit.src.utils import FruitContract, FruitResponse

app = FastAPI()


@app.on_event("startup")
async def startup_event() -> None:
    initialize_database()


@app.on_event("shutdown")
async def shutdown_event() -> None:
    destroy_database()


@app.get("/health/", status_code=200, include_in_schema=False)
async def get_health() -> dict:
    return {"response": "OK"}


@app.get("/fruits/{fruit_id:int}", response_model=None)
async def get_fruit_by_id_endpoint(fruit_id: int) -> FruitResponse:
    return await get_fruit_by_id(id=fruit_id)


@app.get("/fruits", response_model=None)
async def get_fruits_endpoint(
    name: str = Query(default=None, title="Fruit Name")
) -> list[FruitResponse]:
    filters = {}
    if name:
        filters["name"] = name
    return await get_fruits(filters=filters)


@app.post("/messages", response_model=None)
async def create_fruit_endpoint(fruit: FruitContract) -> FruitResponse:
    return await create_fruit(fruit=fruit)

@app.patch("/fruits/{fruit_id:int}", response_model=None)
async def update_fruit_endpoint(fruit_id: int, fruit: FruitContract) -> FruitResponse:
    return await update_fruit(id=fruit_id, fruit=fruit)

@app.delete("/fruits/{fruit_id:int}", response_model=None)
async def delete_fruit_endpoint(fruit_id: int) -> FruitResponse:
    return await delete_fruit(id=fruit_id)