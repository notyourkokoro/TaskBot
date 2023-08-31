import asyncio

from sqlalchemy.orm import selectinload

from app.database.connect import async_session, engine
from app.database.models import Base, User, Task

from sqlalchemy import select


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with async_session.begin() as session:

        # создание пользователей
        usr1 = User(tg_id=1, username='sunshine')
        usr2 = User(tg_id=2, username='moonlight')

        session.add_all(
            [
                usr1,
                usr2,
            ]
        )

    async with async_session.begin() as session:

        # создание "простых" задач
        tsk1 = Task(creator_id=1, title='simp_tsk1')
        tsk2 = Task(creator_id=1, title='simp_tsk2')

        tsk3 = Task(creator_id=2, title='simp_tsk3')
        tsk4 = Task(creator_id=2, title='simp_tsk4')
        tsk5 = Task(creator_id=2, title='simp_tsk5')

        session.add_all(
            [
                tsk1,
                tsk2,
                tsk3,
                tsk4,
                tsk5,
            ]
        )

        # извлекаем пользователей из базы данных
        usr1 = await session.scalar(select(User).options(selectinload(User.tasks_rel)).where(User.id == 1))
        usr2 = await session.scalar(select(User).options(selectinload(User.tasks_rel)).where(User.id == 2))

        # присвоение "простых" задач пользователям
        usr1.simple_tasks_rel = [tsk1, tsk2, tsk5]
        usr2.simple_tasks_rel = [tsk3, tsk4, tsk5, tsk1]


if __name__ == '__main__':
    asyncio.run(main())