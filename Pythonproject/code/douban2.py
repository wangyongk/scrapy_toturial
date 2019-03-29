from lxml import etree
import requests
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}
fp = open('douban.csv', 'w+', newline='', encoding='utf-8-sig')
writer = csv.writer(fp)
writer.writerow(('书名', '链接', '作者', '出版社', '出版日期', '价格', '星级', '评论数'))
urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]
for url in urls:
    html = requests.get(url)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        book_infos = info.xpath('td/p/text()')[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('td/div/span[2]/text()')[0]
        comments = info.xpath('td/div/span[3]/text()')
        comment = comments[0] if len(comments) != 0 else "空"
        writer.writerow((name, url, author, publisher, date, price, rate, comment))
fp.close()