from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String

engine = create_engine('sqlite:///Book.db')


class Base(DeclarativeBase): pass

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer, nullable=False)


Base.metadata.create_all(bind=engine)