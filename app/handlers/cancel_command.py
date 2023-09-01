from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.lexicon.lexicon_commands import LEXICON_CANCEL_COMMAND
from app.states.add_state import AddUserInTaskState

cancel_router = Router()


@cancel_router.message(Command('cancel'), StateFilter(AddUserInTaskState.tg_id))
async def cancel_command_successful(message: Message, state: FSMContext):
    """
    Функция для обработки команды /cancel,
    которая сбрасывает состояние до базового
    и данные в хранилище
    """

    # возвращение пользователя в начальное состояние
    # и удаление данных из временного хранилища
    await state.clear()

    await message.answer(LEXICON_CANCEL_COMMAND['cancel_successful'])


@cancel_router.message(Command('cancel'))
async def cancel_command_unsuccessful(message: Message):
    """
    Функция для обработки команды /cancel,
    которая срабатывает в том случае, если
    пользователь не использует FSM
    """

    await message.answer(LEXICON_CANCEL_COMMAND['cancel_unsuccessful'])