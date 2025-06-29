from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon import LEXICON

def build_bookmarks_keyboard(bookmarks: set[int], book: dict[int, str]) -> InlineKeyboardMarkup:
    kb_buttons = []
    for bm in bookmarks:
        page = book[bm]
        button = InlineKeyboardButton(text=f'{bm} - {page[:30]}...', callback_data=f'go_{str(bm)}')
        kb_buttons.append([button])
    
    edit_btn = InlineKeyboardButton(text=LEXICON['edit_bookmarks_button'], callback_data='edit_bookmarks')
    cancel_btn = InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel')

    kb_buttons.append([edit_btn, cancel_btn])

    kb = InlineKeyboardMarkup(inline_keyboard=kb_buttons)

    return kb
    

def build_edit_bookmarks_kb(bookmarks: set[int], book: dict[int, str]) -> InlineKeyboardMarkup:
    kb_buttons = []
    for bm in bookmarks:
        page = book[bm]
        button = InlineKeyboardButton(text=f'{LEXICON['del']} {bm} - {page[:30]}...', callback_data=f'remove_{str(bm)}')
        kb_buttons.append([button])
    
    cancel_btn = InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel')

    kb_buttons.append([cancel_btn])

    kb = InlineKeyboardMarkup(inline_keyboard=kb_buttons)

    return kb 