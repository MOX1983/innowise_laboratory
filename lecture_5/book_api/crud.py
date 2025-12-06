from sqlalchemy.orm import Session
from model import Book
import Books
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
    db.delete(book)
    db.commit()

def update_book(db: Session, update_book: Books) -> Union[Books, None]:
    book = db.query(Book).filter(Book.id == update_book.id).first()
    if book != None:

        book.title = update_book.title
        book.author = update_book.author
        book.year = update_book.year

        db.commit()
        return book
    else:
        return None

def get_search(db: Session, title_parameter: str, parameter: Union[str, int]) -> Book:
    return db.query(Book).filter(getattr(Book, title_parameter) == parameter).first()
