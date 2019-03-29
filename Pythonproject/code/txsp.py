# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 16:31:28 2017
@author: Andrew
"""
#######爬取腾讯视频中《九州天空城》视频评论
import urllib.request
import http.cookiejar
import re

# 设置视频编号
vid = "1472528692"
# 设置评论起始编号
comid = "6351776727144512306"
headers = {"Accept": "text/html,application/xthtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
           "Connection": "keep-alive",
           "referer": "http://www.163.com/"}
# 设置cookie
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# 设置头信息
headall = []
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
opener.addheaders = headall
# 将opener安装为全局
urllib.request.install_opener(opener)


# 建立一个自定义函数craw(vid,comid),实现自动爬取对应评论网页并返回爬取数据
def craw(vid, comid):
    url = "http://coral.qq.com/article/" + vid + "/comment/v2?callback=jQuery112402604990007163235_1514424106408&orinum=10&oriorder=t&pageflag=1&cursor=" + comid + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data


idpat = '"id":"(.*?)"'
userpat = '{"userid":"(.*?)","nick":"(.*?)"'
contpat = '"userid":"(.*?)","content":"(.*?)",'
# 第一层循环，代表爬取多少页，每一次外层循环爬取一页
for i in range(1, 3):
    print("===============================================================")
    print("第" + str(i) + "页评论内容")
    data = craw(vid, comid)
    # 第二层循环，根据爬取的结果提取并处理每条评论的信息，一页10条评论
    idlist = re.compile(idpat, re.S).findall(data)
    userlist = re.compile(userpat, re.S).findall(data)
    contlist = re.compile(contpat, re.S).findall(data)
    for i in range(0, min(len(idlist), len(userlist), len(contlist))):
        for j in range(0, min(len(idlist), len(userlist), len(contlist))):
            if userlist[i][0] == contlist[j][0]:
                print("用户名：" + eval('u"' + userlist[i][1] + '"'))
                print("内容是：" + eval('u"' + contlist[j][1] + '"'))
                print("------------------------------------------")
    # 将comid改变为该页的最后一条评论id，实现不断自动加载
    comid = idlist[9]



