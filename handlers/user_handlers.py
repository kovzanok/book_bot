from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import logging

from lexicon import LEXICON
from database import user_dict_template, db
from services import book
from keyboards import build_pagination_kb, build_bookmarks_keyboard, build_edit_bookmarks_kb
from filters import IsDigit, IsBookmarkRemove, IsBookmarkRedirect


router = Router()
logger = logging.getLogger(__name__)

@router.message(CommandStart())
async def process_start_commands(message: Message):
    user_id = message.from_user.id

    if user_id not in db:
        db[user_id] = user_dict_template

    await message.answer(text=LEXICON['/start'])

@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message):
    kb = build_pagination_kb(1, len(book.keys()))
    await message.answer(text=book[1],reply_markup=kb)

@router.message(Command(commands='continue'))
async def process_continue_command(message: Message):
    user_id = message.from_user.id
    current_page = db[user_id]["page"]
    kb = build_pagination_kb(current_page, len(book.keys()))
    await message.answer(text=book[current_page],reply_markup=kb)

@router.callback_query(F.data == 'forward')
async def process_forward_pagination(callback: CallbackQuery):
    user_id = callback.from_user.id
    current_page = db[user_id]["page"]
    if current_page == len(book.keys()):
        await callback.answer()
    else:
        next_page = current_page + 1
        kb = build_pagination_kb(next_page, len(book.keys()))
        db[user_id]["page"] = next_page
        await callback.message.edit_text(text=book[next_page],reply_markup=kb)

@router.callback_query(F.data == 'backward')
async def process_backward_pagination(callback: CallbackQuery):
    if callback.message:
        user_id = callback.from_user.id
        current_page = db[user_id]["page"]
        if current_page == 1:
            await callback.answer()
        else:
            next_page = current_page - 1
            kb = build_pagination_kb(next_page, len(book.keys()))
            db[user_id]["page"] = next_page
            await callback.message.edit_text(text=book[next_page],reply_markup=kb)
           
@router.callback_query(IsDigit())
async def process_bookmark_add(callback: CallbackQuery):
    user_id = callback.from_user.id
    page = callback.data

    bookmarks:set = db[user_id]['bookmarks']
    if page:
        bookmarks.add(int(page))

    await callback.answer(text=LEXICON['bookmark_added'])

@router.message(Command(commands='bookmarks'))
async def process_bookmarks_command(message: Message):
    user_id = message.from_user.id

    bookmarks = db[user_id]["bookmarks"]

    if len(bookmarks)==0:
        await message.answer(text=LEXICON['no_bookmarks'])
    else:
        kb = build_bookmarks_keyboard(bookmarks, book)
        await message.answer(text=LEXICON['/bookmarks'], reply_markup=kb)

@router.callback_query(F.data == 'cancel')
async def process_bookmarks_exit(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['cancel_text'])

@router.callback_query(F.data == 'edit_bookmarks')
async def process_bookmarks_edit(callback: CallbackQuery):
    user_id = callback.from_user.id

    bookmarks = db[user_id]["bookmarks"]
    kb = build_edit_bookmarks_kb(bookmarks, book)

    await callback.message.edit_text(text=LEXICON['edit_bookmarks'], reply_markup=kb)

@router.callback_query(IsBookmarkRemove())
async def process_bookmark_remove(callback: CallbackQuery):
    page = int(callback.data.replace('remove_',''))
    user_id = callback.from_user.id

    bookmarks = db[user_id]["bookmarks"]

    bookmarks.discard(page)

    if len(bookmarks)==0:
        await callback.message.edit_text(text=LEXICON['no_bookmarks'])
    else:
        kb = build_edit_bookmarks_kb(bookmarks, book)
        await callback.message.edit_text(text=LEXICON['edit_bookmarks'], reply_markup=kb)

@router.callback_query(IsBookmarkRedirect())
async def process_bookmark_redirect(callback: CallbackQuery):
    message = callback.message
    page = int(callback.data.replace('go_',''))
    kb = build_pagination_kb(page, len(book.keys()))
    await message.edit_text(text=book[page],reply_markup=kb)

@router.message(Command(commands='help'))
async def process_help_commands(message: Message):
    await message.answer(text=LEXICON['/help'])
