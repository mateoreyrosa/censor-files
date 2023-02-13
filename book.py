class Book:
    def __init__(self, name: str, content: str) -> None:
        self.content = content
        self.name = name
    
    def get_name(self) -> str:
        return self.name
    
    def get_content(self) -> None:
        return self.content