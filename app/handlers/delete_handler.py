from aiogram import Router
from aiogram.types import Message

delete_router = Router()


@delete_router.message()
async def delete_message(message: Message):
    """Функция, которая удаляет "лишние" сообщения"""

    await message.delete()