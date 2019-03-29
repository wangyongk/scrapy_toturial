import lxml
import requests
from bs4 import BeautifulSoup
from lxml import html
import csv

urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 250, 25)]
url = 'https://movie.douban.com/top250'


def get_items(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
        'Cookie': 'bid=oJDHcRZAfZ0; ll="118282"; _vwo_uuid_v2=E214A7F1BDCECC6E723664187A86F52E|76a273c7310d9f375d99252440354e87; _pk_id.100001.4cf6=5b4a90664736e799.1479056723.5.1479286527.1479281884.; __utma=30149280.993280854.1479056726.1479281805.1479286717.5; __utmc=30149280; __utmz=30149280.1479056726.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1435542470.1479056726.1479281805.1479286717.5; __utmc=223695111; __utmz=223695111.1479056726.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap=1'

        }
    content = requests.get(url, headers=headers)
    content.encoding = 'utf-8'
    return content.content


def get_items2(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
        'Cookie': 'bid=oJDHcRZAfZ0; ll="118282"; _vwo_uuid_v2=E214A7F1BDCECC6E723664187A86F52E|76a273c7310d9f375d99252440354e87; _pk_id.100001.4cf6=5b4a90664736e799.1479056723.5.1479286527.1479281884.; __utma=30149280.993280854.1479056726.1479281805.1479286717.5; __utmc=30149280; __utmz=30149280.1479056726.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1435542470.1479056726.1479281805.1479286717.5; __utmc=223695111; __utmz=223695111.1479056726.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap=1'

        }
    content = requests.get(url, headers=headers)
    content = BeautifulSoup(content.text, 'lxml')
    content = content.decode('utf-8')
    return content  # 这个函数也可以解析网页,但是不是很懂为何要解码,不解码xpath是会报错,以后来填坑吧.而且这样采集出的数据不美观,行与行的间距太大,编码的问题还是要好好研究一下啊


def get_everyitem(source):
    selector = lxml.html.document_fromstring(source)
    moveItemList = selector.xpath('//div[@class="info"]')
    movieList = []
    # print(type(moveItemList),moveItemList)
    for eachmovie in moveItemList:
        movieDict = {}
        title = list(eachmovie.xpath('div[@class="hd"]/a/span[@class="title"]/text()'))
        # print(title)
        otherTitle = eachmovie.xpath('div[@class="hd"]/a/span[@class="other"]/text()')
        # print(otherTitle)
        link = eachmovie.xpath('div[@class="hd"]/a/@href')[0]
        directorAndActor = eachmovie.xpath('div[@class="bd"]/p[@class=""]/text()')
        star = eachmovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]
        quote = eachmovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()')
        if quote:
            quote = quote[0]
        else:
            quote = " "

        movieDict['title'] = "".join(title + otherTitle)
        movieDict['link'] = link
        movieDict['directorAndActor'] = "".join(directorAndActor).replace('                            ', '').replace(
            '\r', '').replace('\n', '')
        movieDict['star'] = star
        movieDict['quote'] = quote
        # print(movieDict)
        movieList.append(movieDict)
    return movieList


def writemovie(movielist):
    with open('doubantop250_movieList.csv', 'w', encoding="UTF-8", newline='')as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'link', 'directorAndActor', 'star', 'quote'])
        writer.writeheader()
        for i in movielist:
            print(i)
            writer.writerow(i)


if __name__ == '__main__':
    all_movoeList = []
    for i in urls:
        source = get_items(i)
        data = get_everyitem(source)
        all_movoeList += (data)

    # print(all_movoeList)

    writemovie(all_movoeList)
