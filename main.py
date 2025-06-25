from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
import asyncio
import logging

from config import load_config
from keyboards import set_main_menu
from handlers import other_handlers

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.INFO,
                        format=('%(filename)s:%(lineno)d #%(levelname)-8s '
                                '[%(asctime)s] - %(name)s - %(message)s'))
    config = load_config(None)

    logger.info('Start bot')

    bot = Bot(token=config.bot.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_router(other_handlers.router)

    await set_main_menu(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
