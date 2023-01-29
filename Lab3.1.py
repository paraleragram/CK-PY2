class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str :
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, page: int):
        super().__init__(name, author)
        self.page = page

    @property
    def page(self) -> int:
        return self._page

    @page.setter
    def page(self, new_page: int) -> None:
        if type(new_page) == int:
            self._page = new_page

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страницы {self.page}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}), page={self.page!r}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if type(new_duration) == float:
            self._duration = new_duration

    def __str__(self):
        return f"Аудионига {self.name}. Автор {self.author}. Длительность {self.duration} ч"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}), duration={self.duration!r}"

"""Проверка результатов"""

book_1 = Book('The Great Gatsby', 'F. Scott Fitzgerald')
book_2 = PaperBook('The Master and Margarita', 'M. Bulgakov', 345)
#book_3 = PaperBook('The Adventures of Sherlock Holmes', '	Arthur Conan Doyle', '345') #проверим, как работают свойства
book_4 = AudioBook('Robinson Crusoe', '	Daniel Defoe', 7.42)

print(book_1, book_2, book_4, sep='\n')