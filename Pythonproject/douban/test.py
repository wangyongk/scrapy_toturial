import requests
import csv
from lxml import etree
moviedata = []
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47'
}
for i in range(0,250,25):
    url='https://movie.douban.com/top250?start='+str(i)
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    movies = html.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for movie in movies:
            #排名
            count=movie.xpath('./div/div[1]/em/text()')[0]
            #名称
            title=movie.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
            #导演和演员
            director_actor=movie.xpath('./div/div[2]/div[2]/p[1]/text()')[0].strip('\n').strip('\xa0')
            #导演
            director=director_actor[:director_actor.find('主演')].strip()
            #演员
            actor = director_actor[director_actor.find('主演'):].strip()
            #类型地区年份
            type_region_year=movie.xpath('./div/div[2]/div[2]/p[1]/text()')[1].strip('\n').strip('\xa0')
            #年份
            year=type_region_year.split('/')[0].strip()
            #地区
            region = type_region_year.split('/')[1].strip()
            #类型
            type = type_region_year.split('/')[2].strip()
            #评分
            score = movie.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0].strip('\n').strip('\xa0')
            #简评
            quote=movie.xpath('./div/div[2]/div[2]/p[2]/span/text()')
            moviedata.append([count, title,score,region,year,type,director,actor,quote])
            print(moviedata)
with open('xpathdouban.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    header = ['序号', '电影名称', '豆瓣评分', '地区', '年份', '类型', '导演', '主演']
    writer.writerow(header)
    for line in moviedata:
        writer.writerow(line)

