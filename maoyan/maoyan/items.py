# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


from scrapy import Item, Field
class MovieItem(Item):
    title = Field()     #电影标题
    actors = Field()    #演员
    releasetime = Field()   #上映时间
    cover_img = Field()     #缩略图
    detail_page = Field()   #电影详情页url
    score = Field()         #电影评分
