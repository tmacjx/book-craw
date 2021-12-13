
from sqlalchemy import Column, String, Integer, DateTime, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'
    # 主键ID
    id = Column(Integer, primary_key=True)
    # 作者ID
    author_id = Column(Integer)
    # 书籍ID
    book_id = Column(Integer)
