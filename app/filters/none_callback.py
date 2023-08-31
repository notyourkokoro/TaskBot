from aiogram.filters.callback_data import CallbackData


class NoneCallbackData(CallbackData, prefix='nodata'):
    """
    Данный фильтр применяется в случаях,
    когда кнопка не должна ничего делать
    """

    pass
