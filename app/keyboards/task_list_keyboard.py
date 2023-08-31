from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.filters.none_callback import NoneCallbackData
from app.filters.simple_tasks_callbacks import (PrevSimpleList, NextSimpleList, CurrentSimpleTask)


async def tasks_keyboard(user_id: int, tasks: List,
                         current_page: int, last_page: int) -> InlineKeyboardMarkup:
    """
    Функция, предназначенная для создания клавиатуры,
    кнопки которой представляют собой заголовки задач,
    по котором можно перейти, чтобы посмотреть задачу
    более детально
    """

    kb_builder = InlineKeyboardBuilder()

    # наполнение клавиатуры кнопками с задачами
    for task in tasks[(current_page - 1) * 8:(current_page - 1) * 8 + 8]:
        kb_builder.row(InlineKeyboardButton(
            text=f'➖ {task.title}',
            callback_data=CurrentSimpleTask(user_id=user_id,
                                            task_id=task.id).pack()
        ))

    # добавление в клавиатуру кнопок для переключения страниц
    kb_builder.row(
        InlineKeyboardButton(
            text='<<',
            callback_data=PrevSimpleList(current_page=current_page,
                                         last_page=last_page).pack()),
        InlineKeyboardButton(
            text=f'{current_page}/{last_page}',
            callback_data=NoneCallbackData().pack()),
        InlineKeyboardButton(
            text='>>',
            callback_data=NextSimpleList(current_page=current_page,
                                         last_page=last_page).pack()),
        width=3)

    return kb_builder.as_markup()