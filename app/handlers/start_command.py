from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.database.requests.user_requests import add_user
from app.filters.started import IsStarted
from app.lexicon.lexicon_commands import LEXICON_START_COMMAND

start_router = Router()


@start_router.message(CommandStart(), IsStarted())
async def next_start_command(message: Message):
    await message.answer(LEXICON_START_COMMAND['next'])


@start_router.message(CommandStart())
async def first_start_command(message: Message):
    await add_user(message.chat.id, message.chat.username)
    await message.answer(LEXICON_START_COMMAND['first'])