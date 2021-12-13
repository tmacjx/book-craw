
from sqlalchemy import Column, String, Integer, DateTime, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Comment(Base):
    __tablename__ = 'comment'
    # 主键ID
    id = Column(Integer, primary_key=True)
    # 书籍ID
    book_id = Column(Integer)
    # 评论用户
    username = Column(String)
    # 评论内容
    text = Column(TEXT)
    # 评论时间
    comment_time = Column(DateTime)
    # 点赞数
    up_count = Column(Integer)


