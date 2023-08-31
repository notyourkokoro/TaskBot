from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.filters.not_completed_callback import NotCompleted
from app.filters.simple_tasks_callbacks import DeleteSimpleTask, BackToSimpleTaskList


async def current_task_keyboard(user_id: int, creator_id: int, task_id: int) -> InlineKeyboardMarkup:
    """Клавиатура, которая позволяет работать с отельно взятой задачей"""

    kb_builder = InlineKeyboardBuilder()

    # добавление кнопок "Удалить" и "Добавить пользователя" при наличии прав
    if user_id == creator_id:
        kb_builder.row(InlineKeyboardButton(text='Удалить',
                                            callback_data=DeleteSimpleTask(task_id=task_id).pack()),
                       InlineKeyboardButton(text='Добавить пользователя',
                                            callback_data=NotCompleted().pack()),
                       width=2)

    # добавление кнопки "Назад"
    kb_builder.row(InlineKeyboardButton(text='Назад',
                                        callback_data=BackToSimpleTaskList().pack()))

    return kb_builder.as_markup()