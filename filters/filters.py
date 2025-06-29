from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery

class IsDigit(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        if callback.data:
            return callback.data.isdigit()
        return False

class IsBookmarkRemove(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        data = callback.data
        if data:
            return data.startswith('remove_') and data[7:].isdigit()
        
        return False
    
class IsBookmarkRedirect(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        data = callback.data
        if data:
            return data.startswith('go_') and data[3:].isdigit()
        
        return False