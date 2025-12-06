class Books():
    def __init__(self, title: str, author: str, year: int):
        self._title = title
        self._author = author
        self._year = year

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


