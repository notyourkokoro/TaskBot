from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.database.requests.task_requests import delete_task, select_task, add_task_in_user
from app.database.requests.user_requests import select_user_with_tasks
from app.filters.tasks_callbacks import (NextSimpleList, PrevSimpleList,
                                         CurrentSimpleTask, DeleteSimpleTask,
                                         BackToSimpleTaskList, AddUserInTask)
from app.keyboards.task_list_keyboard import tasks_keyboard
from app.keyboards.task_keyboard import current_task_keyboard
from app.lexicon.lexicon_commands import LEXICON_TASKS_COMMAND
from app.states.add_state import AddUserInTaskState
from app.utils.task_list import create_task_list

tasks_router = Router()


@tasks_router.message(Command('tasks'))
async def select_all_tasks(message: Message):
    """Функция, обрабатывающая команду /tasks"""
    await message.delete()
    await create_task_list(message.answer, message.chat.id)


@tasks_router.callback_query(NextSimpleList.filter())
async def next_task_list(callback: CallbackQuery, callback_data: NextSimpleList):
    """Функция, которая помогает переключиться на следующую страницу в списке задач"""

    current_page, last_page = callback_data.current_page + 1, callback_data.last_page

    if current_page <= last_page:
        user_with_tasks = await select_user_with_tasks(callback.message.chat.id)
        tasks: list = user_with_tasks.tasks_rel

        await callback.message.edit_text(
            text=LEXICON_TASKS_COMMAND['tasks'],
            reply_markup=await tasks_keyboard(user_id=user_with_tasks.id,
                                              tasks=tasks,
                                              current_page=current_page,
                                              last_page=last_page)
        )

    await callback.answer()


@tasks_router.callback_query(PrevSimpleList.filter())
async def prev_task_list(callback: CallbackQuery, callback_data: NextSimpleList):
    """Функция, которая помогает переключиться на предыдущую страницу в списке задач"""

    current_page, last_page = callback_data.current_page - 1, callback_data.last_page

    if current_page > 0:
        user_with_tasks = await select_user_with_tasks(callback.message.chat.id)
        tasks: list = user_with_tasks.tasks_rel

        await callback.message.edit_text(
            text=LEXICON_TASKS_COMMAND['tasks'],
            reply_markup=await tasks_keyboard(user_id=user_with_tasks.id,
                                              tasks=tasks,
                                              current_page=current_page,
                                              last_page=last_page)
        )

    await callback.answer()


@tasks_router.callback_query(CurrentSimpleTask.filter())
async def open_simple_task(callback: CallbackQuery, callback_data: CurrentSimpleTask):
    """
    Функция для обработки кнопки с заголовком задачи.
    При нажатии позволяет получить более подробную
    информацию о выбранной задаче
    """

    task = await select_task(callback_data.task_id)

    await callback.message.edit_text(
        text=task.title,
        reply_markup=await current_task_keyboard(user_id=callback_data.user_id,
                                                 creator_id=task.creator_id,
                                                 task_id=callback_data.task_id)
    )

    await callback.answer()


@tasks_router.callback_query(DeleteSimpleTask.filter())
async def delete_simple_task(callback: CallbackQuery, callback_data: DeleteSimpleTask):
    """Функция для обработки кнопки удаления задачи"""

    await delete_task(callback_data.task_id)
    await create_task_list(callback.message.edit_text, callback.message.chat.id)

    await callback.answer(LEXICON_TASKS_COMMAND['del_task'])


@tasks_router.callback_query(BackToSimpleTaskList.filter())
async def back_to_simple_task_list(callback: CallbackQuery):
    """Функция для возвращения по кнопке к списку задач"""

    await create_task_list(callback.message.edit_text, callback.message.chat.id)
    await callback.answer()


@tasks_router.callback_query(AddUserInTask.filter())
async def start_add_user_in_task(callback: CallbackQuery, callback_data: AddUserInTask,state: FSMContext):
    """
    Функция, которая начинает процесс
    добавления нового пользователя
    для выбранной задачи
    """

    # добавляем ID задачи в состояние
    await state.update_data(task_id=callback_data.task_id)

    await callback.message.edit_text(text=LEXICON_TASKS_COMMAND['start_add_user_in_task'])

    # устанавливаем состояние ожидания ввода ID
    await state.set_state(AddUserInTaskState.tg_id)


@tasks_router.message(StateFilter(AddUserInTaskState.tg_id), F.text.isdigit())
async def check_and_add_user(message: Message, state: FSMContext):
    tg_id = int(message.text)
    data = await state.get_data()

    result = await add_task_in_user(tg_id=tg_id, task_id=data['task_id'])
    if not result:
        await message.answer(text=LEXICON_TASKS_COMMAND['successful_add'].format(tg_id=tg_id))
        await state.clear()
    else:
        await message.answer(text=LEXICON_TASKS_COMMAND[result].format(tg_id=tg_id))


@tasks_router.message(StateFilter(AddUserInTaskState.tg_id))
async def error_add_user(message: Message):
    await message.answer(text=LEXICON_TASKS_COMMAND['add_user_err'])