from aiogram.filters.callback_data import CallbackData


class PrevSimpleList(CallbackData, prefix='prev_simple_list'):
    current_page: int
    last_page: int


class NextSimpleList(CallbackData, prefix='next_simple_list'):
    current_page: int
    last_page: int


class CurrentSimpleTask(CallbackData, prefix='current_simple_task'):
    user_id: int
    task_id: int


class DeleteSimpleTask(CallbackData, prefix='delete_simple_task'):
    task_id: int


class BackToSimpleTaskList(CallbackData, prefix='back_to_simple_tasks'):
    pass


class AddUserInTask(CallbackData, prefix='add_user'):
    task_id: int
