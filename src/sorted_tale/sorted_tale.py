'''
- main module for stored tale project
- uses functions from sorts.py and utils.py
'''
from src.algorithms.quick_sort import quicksort
from .utils import load_books
from .sorts import bubble_sort


bookshelf = load_books("books_small.csv")

# for book in bookshelf:
#   print(book['title'])

print(ord("a"))
# print(ord(""))
print(ord("A"))


def by_title_ascending(booka, bookb) -> bool:
    if booka["title_lower"] > bookb["title_lower"]:
        return True
    else:
        return False


def by_author_ascending(booka, bookb) -> bool:
    if booka["author_lower"] > bookb["author_lower"]:
        return True
    else:
        return False


def by_total_length(booka, bookb) -> bool:
    if len(booka["title"]) + len(booka["author"]) > len(bookb["title"]) + len(
        bookb["author"]
    ):
        return True
    else:
        return False


sort1 = bubble_sort(bookshelf, by_title_ascending)

# for book in sort1:
#     print(book['title'])


bookshelf_v1 = bookshelf.copy()

sort2 = bubble_sort(bookshelf_v1, by_author_ascending)

# for book in sort2:
#     print(book['author'])

bookshelf_v2 = bookshelf.copy()

quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

for book in bookshelf_v2:
    print(book["author"])


long_bookshelf = load_books("books_large.csv")

bubble_sort(long_bookshelf, by_total_length)

quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
