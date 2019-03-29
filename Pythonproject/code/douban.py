# -*- coding: UTF-8 -*-
import requests
from lxml import etree
import time
import csv

# 从网页上获取电影数据
moviedata = []
count = 0
for i in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(25 * i)
    data = requests.get(url).text
    html = etree.HTML(data)
    movies = html.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for movie in movies:
        title = movie.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
        director_actor = movie.xpath('./div/div[2]/div[2]/p[1]/text()')[0].strip('\n').strip('\xa0')
        type_region_year = movie.xpath('./div/div[2]/div[2]/p[1]/text()')[1].strip('\n').strip('\xa0')
        score = movie.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
        director = director_actor[:director_actor.find('主演')].strip()
        actor = director_actor[director_actor.find('主演'):].strip()
        year = type_region_year.split('/')[0].strip()
        region = type_region_year.split('/')[1].strip()
        type = type_region_year.split('/')[2].strip()
        # time.sleep(1)
        # print("{0:<5}{1:{4}<15}{2:<3}{3:<}".format(count+1,title,score,info,chr(12288)))
        moviedata.append([count + 1, title, score, region, year, type, director, actor])
        count += 1

# 将数据写入CSV文件
timestr = time.strftime("%Y%m%d%H%M%S", time.localtime())
moviecsv = 'MoviesTop250' + timestr + '.csv'
with open(moviecsv, 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    header = ['序号', '电影名称', '豆瓣评分', '地区', '年份', '类型', '导演', '主演']
    writer.writerow(header)
    for line in moviedata:
        writer.writerow(line)