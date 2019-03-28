# -*- coding: utf-8 -*-
import scrapy
from tszn.items import TsznItem
from scrapy.http import Request

class LesSpider(scrapy.Spider):
    name = 'les'
    allowed_domains = ['hellobi.com']
    start_urls = ['https://edu.hellobi.com/course/1']
    def parse(self, response):
        item=TsznItem()

        item["title"]=response.xpath("//ol[@class='breadcrumb']/li[@class='active']/text()").extract()
        item["student"] = response.xpath("//div[@class='course-price']/span[@class='course-view']/text()").extract()
        item["teacher"] = response.xpath("//div[@class='media-body']/a[@class='lec-name']/text()").extract()
        item["link"] = response.xpath("//ul[@class='nav nav-tabs']/li[@class='active']/a/@href").extract()

        yield item
        for i in range(2,6):
            url="https://edu.hellobi.com/course/"+str(i)
            yield Request(url, callback=self.parse)



