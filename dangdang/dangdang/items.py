# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

#import scrapy


#class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
 #   pass
import scrapy
class BookspiderItem(scrapy.Item):
    rank = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    press = scrapy.Field()
    price = scrapy.Field()
    comments = scrapy.Field()
