from aiogram import Bot
from aiogram.types import BotCommand

from app.lexicon.lexicon_menu import LEXICON_COMMAND_MENU


async def set_main_menu(bot: Bot):
    """Функция для настройки кнопок меню бота"""

    main_menu_commands = [
        BotCommand(command=command,
                   description=description)
        for command, description in LEXICON_COMMAND_MENU.items()
    ]

    await bot.set_my_commands(main_menu_commands)