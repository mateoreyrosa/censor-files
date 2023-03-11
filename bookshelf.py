from typing import Optional
from book import Book
import os
import pathlib
class BookShelf:
    def __init__(self, books: Optional[list[Book]], output_path="./") -> None:
        self.books = books if books else []
        self.output_path = output_path
        self.__create_bookshelf()

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        self.__create_book(book)
    
    def get_books(self) -> list[Book]:
        return self.books

    def get_book_paths(self) -> list[str]:
        file_paths = []
        for path in os.listdir(self.output_path):
            file_path = os.path.join(self.output_path, path)
            if os.path.isfile(file_path):
                file_paths.append(file_path)
        return file_paths

    def __create_bookshelf(self) -> None:
        for book in self.books:
            self.__create_book(book)

    def __create_book(self, book: Book) -> None:
        pathlib.Path(self.output_path).mkdir(parents=True, exist_ok=True) 
        with open(f"{self.output_path}/{book.get_name()}.txt", "w") as bookshelf:
            if book.location:
                with open(book.location, "r") as book_source:
                    for line in book_source.readlines():
                        bookshelf.write(line)
            else:
                bookshelf.write(book.get_content())
            


