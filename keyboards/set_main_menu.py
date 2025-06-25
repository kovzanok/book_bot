from aiogram.types import BotCommand
from aiogram import Bot

from lexicon import LEXICON


async def set_main_menu(bot: Bot):
    menu_commands: list[BotCommand] = [BotCommand(command='/start', description=LEXICON['start']),
                                       BotCommand(command='/help', description=LEXICON['help']),
                                       BotCommand(command='/beginning', description=LEXICON['beginning']),
                                       BotCommand(command='/continue', description=LEXICON['continue']),
                                       BotCommand(command='/bookmarks', description=LEXICON['bookmarks'])
                                       ]

    await bot.set_my_commands(menu_commands)
