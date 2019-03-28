# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class TsznPipeline(object):
    def process_item(self, item, spider):
        print(item["title"])
        print(item["student"])
        print(item["teacher"])
        print(item["link"])
        with open('test_csv.csv', 'a', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow((item['title'], item['student'], item['teacher'],
                                     item['link']))
        return item
