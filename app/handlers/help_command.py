from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.lexicon.lexicon_commands import LEXICON_HELP_COMMAND

help_router = Router()


@help_router.message(Command('help'))
async def create_task(message: Message):
    """Функция для обработки команды /help"""

    await message.answer(LEXICON_HELP_COMMAND['help'])