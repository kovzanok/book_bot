from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon import LEXICON

def build_pagination_kb(current_page: int, total_pages: int):

    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=LEXICON['backward'], callback_data='backward'),
                          InlineKeyboardButton(text=f'{current_page}/{total_pages}', callback_data=str(current_page)),
                          InlineKeyboardButton(text=LEXICON['forward'], callback_data='forward')
                        ]])
    
    return kb
    