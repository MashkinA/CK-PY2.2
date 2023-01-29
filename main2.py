from typing import Optional

from pydantic import BaseModel


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id: int, name: str, pages: int):
        if not isinstance(id, int):
            raise TypeError("Идентификатор объекта книга должен быть целым числом")
        self.id = id

        if not isinstance(name, str):
            raise TypeError("Название книги может быть только строкой")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целочисленным")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


class Library(BaseModel):
    books: Optional[list] = []

    def get_next_book_id(self):
        last_book_index = len(self.books) - 1
        if last_book_index <= 0:
            next_book_id = 1
        else:
            next_book_id = self.books[last_book_index].id + 1
        return next_book_id

    def get_index_by_book_id(self, book_id: int):
        if not isinstance(book_id, int):
            raise TypeError("Идентификатор объекта книга должен быть целым числом")
        book_index = None
        list_id = []
        for i in range(len(self.books)):
            list_id.append(self.books[i].id)
        for index, current_id in enumerate(list_id):
            if current_id == book_id:
                book_index = index
        if book_index is None:
            raise ValueError("Книги с таким id не существует, проверьте написание")
        return book_index


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
# пустая строка


