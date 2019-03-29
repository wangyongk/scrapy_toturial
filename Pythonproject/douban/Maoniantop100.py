#import json
# import requests
# from requests.exceptions import RequestException
# import re
#
#
# def get_page(url):
#     # 伪装浏览器
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
#     }
#     try:
#         res = requests.get(url, headers=headers)
#         if res.status_code == 200:
#             return res.text
#     except RequestException:    # 捕捉请求请求失败
#         return None
#
#
# def parse_page(html):
#     # 根据网页编写正则表达式，首先确定<dd>开头和</dd>的内容为电影信息内容
#     # 再一层层找到相应的电影信息
#     pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'  # 排名
#                          '.*?<p.*?"name"><.*?title="(.*?)"'    # 名字
#                          '.*?"star">(.*?)</p>'            # 演员
#                          '.*?"releasetime">(.*?)</p>'       # 上映时间
#                          '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'   # 评分
#                          , re.S)
#     res = re.findall(pattern, html)     # 使用正则表达式查找所有，返回list
#
#     for item in res:
#         # 以迭代器的形式返回内容
#         yield {
#             'index': item[0],
#             'title': item[1],
#             'actor': item[2].strip()[3:],
#             "time": item[3].strip()[5:],
#             'score': item[4]+item[5]
#         }
#
#
# def write_to_file(content):
#     # 以utf-8 方法打开; 'a',附加写方式打开,不可读; a+附加读写方式打开
#     with open('result.txt', 'a', encoding='utf-8') as f:
#         # .dumps 将dict转换成str格式，
#         # .loads 将str转换成dict格式
#         f.write(json.dumps(content, ensure_ascii=False) + '\n')
#         f.close()
#
#
# def main(offset):
#     url = 'http://maoyan.com/board/4?offset='+str(offset)
#     html = get_page(url)
#     # 返回迭代器，循环写入文件
#     for item in parse_page(html):
#         print(item)
#         write_to_file(item)
#
#
# if __name__ == '__main__':
#     # 爬取多个页面，用for语句来生成翻页内容
#     for i in range(10):
#         main(i*10)

import requests
from lxml import etree
import time
import json
from requests.exceptions import RequestException
import re
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/52.0.2743.116 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_xpath(html):
    html = etree.HTML(html)
    results = html.xpath('//dd')
    for result in results:
        rank = result.xpath('i/text()')[0].strip()
        title = result.xpath('div//p[1]/a/@title')[0].strip()
        star = result.xpath('div//p[2]/text()')[0].strip()
        releasetime = result.xpath('div//p[3]/text()')[0].strip()
        score_0 = result.xpath('div/div/div/p/i[1]/text()')[0].strip()
        score_1 = result.xpath('div/div/div/p/i[2]/text()')[0].strip()
        score = score_0 + score_1
        print(rank, title, star, releasetime, score)
    return result

def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    aa = parse_xpath(html)


if __name__ == '__main__':
    for i in range(10):
        main(i*10)
        time.sleep(1)
