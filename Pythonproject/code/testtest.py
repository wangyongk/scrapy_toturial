# -*- coding: UTF-8 -*-
#Python3网络爬虫——（3）代理服务器设置（IP代理使用）

from urllib import request
if __name__ == "__main__":
    #访问网址
    url = 'https://blog.csdn.net/asialee_bird'
    #这是代理IP
    proxy = {'http':'117.68.192.78:18118'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)
    #使用自己安装好的Opener
    response = request.urlopen(url)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    #打印信息
    print(html.title())
    print(len(html))