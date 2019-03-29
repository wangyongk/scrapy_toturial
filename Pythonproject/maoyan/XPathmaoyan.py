import threading
import requests, csv
from lxml import etree

with open('XPathmaoyan.csv', 'a', newline='',encoding='utf-8') as f:
    spamwriter = csv.writer(f)
    spamwriter.writerow(['title', 'star', 'date', 'score'])

class Crawler(threading.Thread):

    def __init__(self, page):
        super().__init__()
        self.page = page

    def run(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                                 ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
                   }
        url = 'http://maoyan.com/board/4?offset={}'.format(10 * self.page)
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)
        results = html.xpath('//*[@class="board-wrapper"]/dd/div/div')
        for result in results:
            # 电影名称 电影主演 电影上映日期 评分
            ws = [
                result.xpath('./div[1]/p[1]/a/text()')[0],
                result.xpath('./div[1]/p[2]/text()')[0].strip(),
                result.xpath('./div[1]/p[3]/text()')[0],
                result.xpath('./div[2]/p/i[1]/text()')[0] + result.xpath('./div[2]/p/i[2]/text()')[0],
            ]
            print(ws)
            #保存到CSV
            with open('XPathmaoyan.csv','a',newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(ws)
if __name__ == '__main__':

    for page in range(10):
        th = Crawler(page)
        th.start()

