class Book:
    def __init__(self, name: str, location: str = "", content: str = "") -> None:
        self.location = location
        self.content = content
        self.name = name
    
    def get_name(self) -> str:
        return self.name
    
    def get_location(self) -> str:
        return self.location

    def get_content(self) -> str:
        return self.content