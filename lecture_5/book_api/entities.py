from pydantic import BaseModel


class Books():

    def __int__(self):
        pass
    def __init__(self, title: str | None, author: str | None, year: int | None, id: int = None):
        self._id = id
        self._title = title
        self._author = author
        self._year = year

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None
