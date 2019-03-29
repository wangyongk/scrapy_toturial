import re
import requests
import time
import os


def get_one_html(url):  # 获取一个页面的html页面并返回
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            return r.text
    except Exception as er:
        print(er)


def get_pic_url(html):  # 用正则提取每一页的关键信息返回
    pic_urls = re.findall('"pic_url":"(.*?)"', html, re.S)
    img_url = []  # 创建空列表，装每一页的所有图片的链接
    for one_pic_url in pic_urls:
        img_url.append('http:' + one_pic_url)
    return img_url  # 返回图片的链接的列表


def write_to_file(page, img_urls):  # 写入文件（下载）
    i = page  # 利用页码，防止后面的写入会覆盖之前的
    n = 0
    for pic_url in img_urls:
        pic = requests.get(pic_url)
        with open('D:/pictures/' + str(i) + str(n) + '.jpg', 'wb') as f:
            f.write(pic.content)
        print('---第{}页第{}张图下载成功---'.format(str(i), str(n)))
        n += 1


def main(keyword, page_num, url):
    html = get_one_html(url)  # 调用函数得到该页的hml
    img_urls = get_pic_url(html)  # 调用函数得到该页的所有图片的链接
    write_to_file(page, img_urls)  # 调用函数，写入即下载图片


if __name__ == '__main__':
    keyword = input('请输入关键词：')
    page_num = eval(input('请输入要爬取的页数：'))
    try:
        os.mkdir('D:/pictures/')
        for page in range(0, page_num):
            url = 'http://s.taobao.com/search?q=' + keyword + '&s=' + str(page)
            main(keyword, page_num, url)
            if page % 2 == 0:
                time.sleep(10)  # 每爬取2页停留10秒
    except Exception as err:
        print(err)
