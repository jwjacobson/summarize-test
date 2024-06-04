import pytest

from summarize_gutenberg.api import Book

def test_assertion():
    assert 1 == 1

@pytest.mark.xfail(reason="Designed to fail")
def test_assertion_fail():
    assert 1 == 2

def test_assertion_in():
    assert 'y' in 'pybites'

def test_book_field_access():
    book = Book(
        id=1,
        title="Yesterday's Tomorrows",
        author="Wilfred Sinecure",
        url="https://www.gutenberg.org/",
        filename="yesterdaystomorrows.txt",
    )

    assert book.id == 1
    assert book.title == "Yesterday's Tomorrows"
    assert book.author == "Wilfred Sinecure"
    assert book.url == "https://www.gutenberg.org/"
    assert book.filename == "yesterdaystomorrows.txt"

def test_from_dict():
    book1 = Book(
        id=1,
        title="Yesterday's Tomorrows",
        author="Wilfred Sinecure",
        url="https://www.gutenberg.org/",
        filename="yesterdaystomorrows.txt",
    )

    book2_dict = {
        "id": 1,
        "title": "Yesterday's Tomorrows",
        "author": "Wilfred Sinecure",
        "url": "https://www.gutenberg.org/",
        "filename": "yesterdaystomorrows.txt",
    }
    book2 = Book.from_dict(book2_dict)

    assert book1 == book2
