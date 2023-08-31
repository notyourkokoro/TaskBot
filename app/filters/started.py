from aiogram.filters import BaseFilter
from aiogram.types import Message

from app.database.requests.user_requests import select_user


class IsStarted(BaseFilter):
    """
    Фильтр, который помогает определить,
    начал пользователь использовать бота
    или нет для занесения нового юзера в БД
    """

    async def __call__(self, message: Message) -> bool:
        result = await select_user(message.chat.id)
        return bool(result)