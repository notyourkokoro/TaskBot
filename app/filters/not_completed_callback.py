from aiogram.filters.callback_data import CallbackData


class NotCompleted(CallbackData, prefix='not_completed'):
    """
    Данный фильтр применяется в случаях,
    когда функция находится на стадии
    разработки
    """

    pass
