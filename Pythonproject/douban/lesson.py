# -*- coding: utf-8 -*-
import scrapy


class LessonSpider(scrapy.Spider):
    name = 'lesson'
    allowed_domains = ['hellobi.com']
    start_urls = ['http://hellobi.com/']

    def parse(self, response):
        pass
