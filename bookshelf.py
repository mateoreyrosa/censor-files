from typing import Optional
from book import Book
import os
import pathlib
class BookShelf:
    def __init__(self, books: Optional[list[Book]], output_dir="./") -> None:
        self.books = books if books else []
        self.output_dir = output_dir
        self.__create_bookshelf()

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        self.__create_book(book)
    
    def get_books(self) -> list[Book]:
        return self.books

    def get_book_paths(self) -> list[str]:
        file_paths = []
        for path in os.listdir(self.output_dir):
            file_path = os.path.join(self.output_dir, path)
            if os.path.isfile(file_path):
                file_paths.append(file_path)
        return file_paths

    def __create_bookshelf(self) -> None:
        for book in self.books:
            self.__create_book(book)

    def __create_book(self, book: Book) -> None:
        pathlib.Path(self.output_dir).mkdir(parents=True, exist_ok=True) 
        with open(f"{self.output_dir}/{book.get_name()}.txt", "w") as bookshelf:
            # Book passed as a file
            if book.location:
                # Allow IO exceptions to fire
                with open(book.location, "r") as book_source:
                    for line in book_source.readlines():
                        bookshelf.write(line)
            else:
                # Book was passed as a string
                bookshelf.write(book.get_content())
            


