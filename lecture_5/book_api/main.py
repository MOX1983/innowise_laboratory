from fastapi import FastAPI, Depends, Request
from starlette.responses import HTMLResponse
from sqlalchemy.orm import sessionmaker, Session
import crud
from entities import Books, BookUpdate
from model import engine

app = FastAPI()

SessionLocal = sessionmaker(autoflush=False, bind=engine)

def  get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/")
def create_book(title: str, author: str, year: int, db: Session = Depends(get_db)):
    book = Books(title, author, year)
    return crud.create_book(db, book)

@app.get("/books/")
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db, book_id)

@app.post("/books/{book_id}")
def update_book(book_id: int, title: str | None = None, author: str | None = None, year: int | None = None, db: Session = Depends(get_db)):
    return crud.update_book(db, book_id, title, author, year)

@app.get("/books/search/")
def get_search(title: str | None = None, author: str | None = None, year: int | None = None, db: Session = Depends(get_db)):
    return crud.get_search(db, title, author, year)

