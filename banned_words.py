from collections.abc import Iterable

class Banned:
    def __init__(self, words: Iterable[str]) -> None:
        self.words = set(word.lower() for word in words)

    def get_words(self) -> set[str]:
        return self.words
    
    def print(self) -> None:
        print("Banned Words:", self.words)

