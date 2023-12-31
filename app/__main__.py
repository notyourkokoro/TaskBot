import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.handlers.delete_handler import delete_router
from app.utils.main_menu import set_main_menu
from app.handlers import routers_list

from app.utils.config import config

logger = logging.getLogger(__name__)


async def main():
    # создание хранилища
    storage: MemoryStorage = MemoryStorage()

    bot: Bot = Bot(token=config.bot_info.bot_token,
                   parse_mode=ParseMode.HTML)
    dp: Dispatcher = Dispatcher()

    # настраиваем главное меню бота
    await set_main_menu(bot)

    # регистрация роутеров для команд
    dp.include_routers(*routers_list)

    # регистрация роутера для удаления "ненужных" сообщений
    dp.include_router(delete_router)

    # Пропуск накопившихся апдейтов
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == '__main__':
    # конфигурирование логирования
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )

    try:
        logger.info('Starting bot')
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # обработка исключений при завершении работы бота
        logger.info('Exit')
