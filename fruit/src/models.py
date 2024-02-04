from __future__ import annotations

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from fruit.src.data import sql_alchemy_db as db

Base = declarative_base()


class Fruit(Base):
    __tablename__ = "fruits"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, nullable=False, unique=True)

    @classmethod
    async def create(cls, name: str) -> Fruit:
        fruit = await cls.get_by_name(name=name)
        if not fruit:
            fruit = cls(name=name)
            db.add(fruit)
            db.commit()
            db.refresh(fruit)
        return fruit

    @classmethod
    async def update(cls, id: int, name: str) -> Fruit:
        fruit = await cls.get_by_id(id=id)
        if fruit:
            fruit.name = name
            db.commit()
            db.refresh(fruit)
        return fruit

    @classmethod
    async def delete(cls, id: int) -> None:
        db.query(cls).filter(cls.id == id).delete()
        db.commit()

    @classmethod
    async def get_all(cls, filters: dict) -> list[Fruit]:
        query = db.query(cls)
        for key, value in filters.items():
            query = query.filter(getattr(cls, key) == value)
        return query.all()

    @classmethod
    async def get_by_id(cls, id: int) -> Fruit:
        return db.query(cls).filter(cls.id == id).first()

    @classmethod
    async def get_by_name(cls, name: str) -> Fruit:
        return db.query(cls).filter(cls.name == name).first()
