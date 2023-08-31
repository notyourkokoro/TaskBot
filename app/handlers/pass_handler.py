from aiogram import Router
from aiogram.types import CallbackQuery

from app.filters.none_callback import NoneCallbackData

pass_router = Router()


@pass_router.callback_query(NoneCallbackData.filter())
async def pass_callback(callback: CallbackQuery):
    """Пропуск действия на кнопку"""

    await callback.answer()
