# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


'''class DangdangPipeline(object):
   def process_item(self, item, spider):
       return item'''
import pymysql
# Define your item pipelines here #
#  Don't forget to add your pipeline to the ITEM_PIPELINES setting
#  See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
def dbHandle():
    conn = pymysql.connect('localhost', 'root', '123456', 'learing',charset='utf8')
    #conn = MySQLdb.connect(host='localhost',db='article',user='root',passwd='psw105',charset='utf8')
    return conn
class DangdangPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        sql = 'insert into dangdang(rank,name,author,press,price,comments) values(%s,%s,%s,%s,%s,%s)'
        #for j in range(len(item["rank"])):
         #   try:
        cursor.execute(sql,(item["rank"],item["name"],item["author"],item["press"],item["price"],item["comments"]))
        dbObject.commit()
           # except Exception as e:
            #    print(e)
             #   dbObject.rollback()
        return item

