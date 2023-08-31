from aiogram import Router
from aiogram.types import CallbackQuery

from app.filters.not_completed_callback import NotCompleted

not_completed_router = Router()


@not_completed_router.callback_query(NotCompleted.filter())
async def not_completed_callback(callback: CallbackQuery):
    await callback.answer('Данная функция пока ещё не реализованна!')
