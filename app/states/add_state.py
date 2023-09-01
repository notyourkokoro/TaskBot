from aiogram.fsm.state import StatesGroup, State


class AddUserInTaskState(StatesGroup):
    tg_id = State()
