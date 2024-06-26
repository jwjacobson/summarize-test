import pytest

from summarize_gutenberg.api import Book
from summarize_gutenberg.get_books import create_filename

def test_assertion():
    assert 1 == 1

@pytest.mark.xfail(reason="Designed to fail")
def test_assertion_fail():
    assert 1 == 2

def test_assertion_in():
    assert 'y' in 'pybites'

@pytest.fixture(scope="module")
def book_fixture():
    """
    Create a Book.
    """
    book = Book(
        id=1,
        title="Yesterday's Tomorrows",
        author="Wilfred Sinecure",
        url="https://www.gutenberg.org/",
        filename="yesterdaystomorrows.txt",
    )

    return book

def test_book_field_access_with_fixture(book_fixture):
    book = book_fixture

    assert book.id == 1
    assert book.title == "Yesterday's Tomorrows"
    assert book.author == "Wilfred Sinecure"
    assert book.url == "https://www.gutenberg.org/"
    assert book.filename == "yesterdaystomorrows.txt"

def test_from_dict_with_fixture(book_fixture):
    book1 = book_fixture

    book2_dict = {
        "id": 1,
        "title": "Yesterday's Tomorrows",
        "author": "Wilfred Sinecure",
        "url": "https://www.gutenberg.org/",
        "filename": "yesterdaystomorrows.txt",
    }
    book2 = Book.from_dict(book2_dict)

    assert book1 == book2

def test_create_filename():
    title = 'Dracula'
    expected_output = 'dracula.txt'
    assert create_filename(title) == expected_output

titles = [
    ('Dracula', 'dracula.txt'), # one word
]

@pytest.mark.parametrize('input, expected', titles)
def test_create_filenames(input, expected):
    assert create_filename(input) == expected, f'Expected {expected}, but got {create_filename(input)}'

titles = [
    ('Dracula', 'dracula.txt'), # one word
    ('Franny and Zooey', 'frannyandzooey.txt'), # spaces
    ('Frankenstein; Or, The Modern Prometheus', 'frankenstein.txt'), # semicolon
    ('"Left-Wing" Communism: an Infantile Disorder', 'leftwingcommunism.txt'), # colon, quoation marks, hyphen
    ('We Who Are About To...', 'wewhoareaboutto.txt'), # periods
    ("Swann's Way", 'swannsway.txt'), # apostrophe/single quote
    ("My Life — Volume 1", 'mylifevolume1.txt') # em dash which is weird but one of the top gutenberg books has one
]

@pytest.mark.parametrize('input, expected', titles)
def test_create_filenames_full(input, expected):
    assert create_filename(input) == expected, f'Expected {expected}, but got {create_filename(input)}'
