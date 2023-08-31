from typing import Any

from sqlalchemy import Select

from app.database.connect import async_session


async def select_one(stmt: Select) -> Any:
    async with async_session.begin() as session:
        result = await session.scalar(stmt)
    return result


async def create_one(obj: Any) -> None:
    async with async_session.begin() as session:
        session.add(obj)


# async def delete_one(obj: Any) -> None:
#     async with async_session.begin() as session:
#         await session.delete(obj)
