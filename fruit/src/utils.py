from __future__ import annotations

from pydantic import BaseModel

from fruit.src.models import Fruit


class FruitResponse(BaseModel):
    id: int
    name: str

    @staticmethod
    def from_model(fruit: Fruit) -> FruitResponse:
        return FruitResponse(
            id=fruit.id,
            name=fruit.name,
        )


class FruitContract(BaseModel):
    name: str
