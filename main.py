
from banned_words import Banned
from bookshelf import BookShelf
from book import Book
import os

import string
def censor_files(files, banned_words):
    for file_path in files:
        with open(file_path, "r+") as file:
            print(file_path)
            word = ""
            while (byte := file.read(1)):
                
                if byte.isspace():
                    word = ""
                    continue
                    
                if byte in string.punctuation:
                    continue
                
                word += byte.lower()
                print(word, len(word))
                if word in banned_words:
                    pos = file.tell()
                    print("cur pos: ", pos, "new pos: ", pos - len(word))
                    
                    file.seek(pos - len(word))
                    print(file.tell())
                    file.write("-" * len(word))
                    print(file.tell())

    print("Banned words found and censored")
                    
def create_bookshelf() -> list[str]:
    book1 = Book.from_file("book1", dir='./books')
    book2 = Book.from_file("book2", dir='./books')
    book3 = Book("book3", content='This is a small book.')
    bookshelf = BookShelf([book1, book2, book3], output_dir="./bookshelf")
    return bookshelf

def main():
    words_to_ban = ["think", "thinking", "don't", "ten", "this"]
    banned_words = Banned(words_to_ban)
    banned_words.print()
    bookshelf = create_bookshelf()
    file_names = bookshelf.get_book_paths()
    censor_files(file_names, banned_words.get_words())

if __name__ == "__main__":
    main()