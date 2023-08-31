from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from app.database.requests.task_requests import add_task
from app.lexicon.lexicon_commands import LEXICON_TASK_COMMAND

task_router = Router()


@task_router.message(Command('task'))
async def create_task(message: Message, command: CommandObject):
    """
    Функция, обрабатывающая команду /task
    За командой должен следовать заголовок задачи,
    чтобы команда успешно сработала
    """

    if command.args:
        await add_task(tg_id=message.chat.id, title=command.args)
        await message.answer(LEXICON_TASK_COMMAND['successful_add'].format(title=command.args))
    else:
        await message.answer(LEXICON_TASK_COMMAND['unsuccessful_add'])