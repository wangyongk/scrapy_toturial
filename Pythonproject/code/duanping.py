













import threading
import requests, csv
from lxml import etree

with open('data22.csv', 'a', newline='') as f:
    spamwriter = csv.writer(f)

class Crawler(threading.Thread):

    def __init__(self, page):
        super().__init__()
        self.page = page

    def run(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                                 ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
                   }
        url = 'https://movie.douban.com/subject/26752088/comments?start=20&limit=20&sort=new_score&status=P&percent_type={}'.format(page * 20)
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)
        results = html.xpath('//*[@id="comments"]')
        for result in results:
            # 电影名称 电影主演 电影上映日期 评分
            ws = [
                result.xpath('./div[{}]/div[2]/h3/span[2]/a/text()')[0],
                result.xpath('./div[{}]/div[2]/p/text()')[0],
            ]
            print(ws)

            #保存到CSV
            with open('data22.csv','a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(ws)


if __name__ == '__main__':

    for page in range(10):
        th = Crawler(page)
        th.start()