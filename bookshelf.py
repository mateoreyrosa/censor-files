from typing import Optional
from book import Book
import os
class BookShelf:
    def __init__(self, path: str, books: Optional[list[Book]]) -> None:
        self.books = books if books else []
        self.dir_path = path
        self.__create_bookshelf()

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        self.__create_book(book)
    
    def get_books(self) -> list[Book]:
        return self.books

    def get_book_paths(self) -> list[str]:
        file_paths = []
        for path in os.listdir(self.dir_path):
            file_path = os.path.join(self.dir_path, path)
            if os.path.isfile(file_path):
                file_paths.append(file_path)
        return file_paths

    def __create_bookshelf(self) -> None:
        for book in self.books:
            self.__create_book(book)

    def __create_book(self, book: Book) -> None:
        with open(f"{self.dir_path}/{book.get_name()}.txt", "w") as file:
            file.write(book.get_content())
            


