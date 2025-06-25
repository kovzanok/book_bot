from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from lexicon import LEXICON

router = Router()


@router.message(CommandStart())
async def process_start_commands(message: Message):
    await message.answer(text=LEXICON['/start'])


@router.message(Command(commands='help'))
async def process_start_commands(message: Message):
    await message.answer(text=LEXICON['/help'])
