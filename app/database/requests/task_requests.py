from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload

from app.database.connect import async_session
from app.database.models import Task, User
from app.database.requests.base_requests import select_one


async def add_task(tg_id: int, title: str):
    """Добавление новой задачи в базу данных"""

    async with async_session.begin() as session:
        user_with_tasks = await session.scalar(
            select(User).options(selectinload(User.tasks_rel)).where(User.tg_id == tg_id)
        )

        task = Task(creator_id=user_with_tasks.id, title=title)
        session.add(task)

        user_with_tasks.tasks_rel.append(task)


# async def all_tasks(tg_id: int) -> List:
#     user = await select_user_with_tasks(tg_id=tg_id)
#     return user.simple_tasks_rel


async def delete_task(task_id: int) -> None:
    """Удаление задачи из базы данных по ID задачи"""

    async with async_session.begin() as session:
        await session.execute(delete(Task).where(Task.id == task_id))


async def select_task(task_id: int) -> Task:
    """Выборка задачи из базы данных по ID задачи"""

    simple_task = await select_one(select(Task).where(Task.id == task_id))
    return simple_task
