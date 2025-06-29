from aiogram.types import BotCommand
from aiogram import Bot

from lexicon import LEXICON_COMMANDS


async def set_main_menu(bot: Bot):
    menu_commands: list[BotCommand] = [BotCommand(command='/help', description=LEXICON_COMMANDS['/help']),
                                       BotCommand(command='/beginning', description=LEXICON_COMMANDS['/beginning']),
                                       BotCommand(command='/continue', description=LEXICON_COMMANDS['/continue']),
                                       BotCommand(command='/bookmarks', description=LEXICON_COMMANDS['/bookmarks'])
                                       ]

    await bot.set_my_commands(menu_commands)
