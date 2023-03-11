class Book:
    def __init__(self, name: str, content: str = "", dir: str = "",) -> None:
        self.dir = dir
        self.content = content
        self.name = name
        self.location = f"{dir}/{name}.txt" if dir else ""

    @classmethod
    def from_file(cls, name: str, dir: str):
        return cls(name, dir=dir)
    
    def get_name(self) -> str:
        return self.name
    
    def get_location(self) -> str:
        return self.location

    def get_content(self) -> str:
        return self.content