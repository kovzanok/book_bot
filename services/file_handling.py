from pathlib import Path

BOOK_PATH = 'book/book.txt'
COVER_PATH = 'book/cover.jpg'
PROJECT_ROOT = Path(__file__).resolve().parent.parent
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end_signs = ',.!:;?'
    counter = 0
    if len(text) < start + size:
        size = len(text) - start
        text = text[start:start + size]
    else:
        if text[start + size] == '.' and text[start + size - 1] in end_signs:
            text = text[start:start + size - 2]
            size -= 2
        else:
            text = text[start:start + size]
        for i in range(size - 1, 0, -1):
            if text[i] in end_signs:
                break
            counter = size - i
    page_text = text[:size - counter]
    page_size = size - counter
    return page_text, page_size


def prepare_book(path: str) -> None:
    with open(Path.joinpath(PROJECT_ROOT, path), 'r', encoding='utf-8-sig') as f:
        book_text = f.read()
        start, page = 0, 1
        while start + PAGE_SIZE < len(book_text):
            book_page, page_size = _get_part_text(book_text, start, PAGE_SIZE)
            start += page_size
            book[page] = book_page.lstrip()
            page += 1

prepare_book(BOOK_PATH)