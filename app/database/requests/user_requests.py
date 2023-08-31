from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database.models import User
from app.database.requests.base_requests import select_one, create_one


async def select_user(tg_id: int) -> User:
    """Выборка пользователя из базы данных по ID в Телеграм"""

    user = await select_one(select(User).where(User.tg_id == tg_id))
    return user


async def select_user_with_tasks(tg_id: int) -> User:
    """Выборка пользователя из базы данных по ID в Телеграм вместе с задачами"""

    user_with_tasks = await select_one(
        select(User).options(selectinload(User.tasks_rel)).where(User.tg_id == tg_id)
    )
    return user_with_tasks


async def add_user(tg_id: int, username: str) -> None:
    """Добавление нового пользователя в базу данных"""

    user = User(tg_id=tg_id, username=username)
    await create_one(user)