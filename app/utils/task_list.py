from math import ceil

from app.database.requests.user_requests import select_user_with_tasks
from app.keyboards.task_list_keyboard import tasks_keyboard
from app.lexicon.lexicon_commands import LEXICON_TASKS_COMMAND


async def create_task_list(func, td_id: int):
    """
    Универсальная функция для создания списка задач
    при вызове команды /tasks или при возвращении к
    этому списку при помощи соответсвующий кнопки
    """

    # получение данных о пользователе и его задачах
    user_with_tasks = await select_user_with_tasks(td_id)
    tasks: list = user_with_tasks.tasks_rel

    # определение наличия клавиатуры
    if tasks:
        await func(text=LEXICON_TASKS_COMMAND['tasks'],
                   reply_markup=await tasks_keyboard(user_id=user_with_tasks.id,
                                                     tasks=tasks,
                                                     current_page=1,
                                                     last_page=ceil(len(tasks) / 8))
                   )
    else:
        await func(text=LEXICON_TASKS_COMMAND['no_one_task'])