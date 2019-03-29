from lxml import etree
import requests
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}
url="http://www.nuc.edu.cn/"
html = requests.get(url)
html.encoding="utf-8"
selector = etree.HTML(html.text)
infos = selector.xpath('//div[@class="news_list"]')

for info in infos:
    name = info.xpath('./ul/li[1]/a/text()')
    time=info.xpath('./ul/li[1]/span/text()')
    href=info.xpath('./ul/li[1]/a/@href')
    print(name)
    print(time)
    print(href)
    #url = info.xpath('td/div/a/@href')[0]
    #book_infos = info.xpath('td/p/text()')[0]'''
