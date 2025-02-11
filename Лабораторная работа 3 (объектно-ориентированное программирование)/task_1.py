class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги."""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, pages={self.pages})")


class AudioBook(Book):
    """Класс аудиокниги."""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, duration={self.duration})")

