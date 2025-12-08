from sqlalchemy.orm import Session
from model import Book
from entities import Books, BookUpdate
from typing import List, Union

def create_book(db: Session, book: Books) -> Book:
    new_book = Book(title= book.title, author= book.author, year= book.year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_books(db: Session) -> List[Book]:
    return db.query(Book).all()

def delete_book(db: Session, id_book: int) -> None:
    book = db.query(Book).filter(Book.id == id_book).first()
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book


def update_book(db: Session, book_id: int, title: str | None = None, author: str | None = None, year: int | None = None) -> Union[Books, None]:
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        if title:
            book.title = title
        if author:
            book.author = author
        if year:
            book.year = year

        db.commit()
        db.refresh(book)
        return book
    else:
        return None

def get_search(db: Session, title: str | None = None, author: str | None = None, year: int | None = None) -> List[Book]:
    query = db.query(Book)

    if title:
        query = query.filter(Book.title == title)
    if author:
        query = query.filter(Book.author == author)
    if year:
        query = query.filter(Book.year == year)

    return query.all()
