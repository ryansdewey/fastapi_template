from fastapi import HTTPException

from fruit.src.models import Fruit
from fruit.src.utils import FruitContract, FruitResponse


async def get_fruit_by_id(id: int) -> FruitResponse:
    fruit = await Fruit.get_by_id(id=id)
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")
    return FruitResponse.from_model(fruit=fruit)


async def get_fruits(filters: dict) -> list[FruitResponse]:
    fruits = await Fruit.get_all(filters=filters)
    return [FruitResponse.from_model(fruit=fruit) for fruit in fruits]


async def create_fruit(fruit: FruitContract) -> FruitResponse:
    fruit = await Fruit.create(name=fruit.name)
    print(fruit)
    return FruitResponse.from_model(fruit=fruit)

async def update_fruit(id: int, fruit: FruitContract) -> FruitResponse:
    fruit = await Fruit.update(id=id, name=fruit.name)
    return FruitResponse.from_model(fruit=fruit)

async def delete_fruit(id: int) -> FruitResponse:
    fruit = await Fruit.delete(id=id)
    return FruitResponse.from_model(fruit=fruit)