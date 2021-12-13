# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 评论实体
class CommentItem(scrapy.Item):
    # define the fields for your item here like:
    # 书籍ID
    book_id = scrapy.Field()
    # 评论用户
    username = scrapy.Field()
    # 评论内容
    text = scrapy.Field()
    # 评论时间
    comment_time = scrapy.Field()
    # 点赞数
    up_count = scrapy.Field()


# 书籍实体
class BookItem(scrapy.Item):
    # 作者ID
    author_id = scrapy.Field()
    # 书籍ID
    book_id = scrapy.Field()
