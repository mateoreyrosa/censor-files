
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
                    
                    
def get_files() -> list[str]:
    book1 = Book("book1", "There once was a panda that lived in the forest with a group of 10 (ten) other pandas. It was a hungry panda and was always thinking and asking \"When will it be meal time?\" He figures it's because he is constantly growing. Its hunger could not be satiated. \"Is that John's?\", he asked.")
    book2 = Book("book2", "\"I don't think so\", she said.")
    bookshelf = BookShelf("./files", [book1, book2])

    file_names = bookshelf.get_book_paths()
    return file_names

def main():
    words_to_ban = ["think", "thinking", "don't", "ten"]
    banned_words = Banned(words_to_ban)
    print(banned_words.get_words())
    file_names = get_files()
    print(file_names)
    censor_files(file_names, banned_words.get_words())
    print( banned_words.get_words())



if __name__ == "__main__":
    main()