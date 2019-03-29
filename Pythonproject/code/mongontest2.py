import requests
from bs4 import BeautifulSoup
import csv

import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient(host='localhost', port=27017)
# 连接数据库
# 创建数据库
db = client.lianjia
# 创建集合
homes = db.homes


def getcontent(url): #网页请求头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47'} #发送get请求
    r = requests.get(url,headers=headers) #获取文本
    content = r.text
    soup = BeautifulSoup(content, 'lxml')
    # 找出所有电影的名字
    div_name = soup.find_all(class_='name')
    # 找出所有电影的主演
    div_star = soup.find_all(class_='star')
    # 找出所有电影的上映时间
    div_time = soup.find_all(class_='releasetime')
    # #找出所有电影的评分
    div_score = soup.find_all(class_='score')
    # 获取电影部数
    long = len(div_name)
    #申明一个全局List,用于保存多部电影参数，每部电影参数也是一个list
    global DATA
    # 遍历每一页中的电影
    for i in range(0, long): #定义一个临时的list保存一部电影的参数
        data =[]
        data.append(div_name[i].get_text().strip())#获取第i部电影的名字
        data.append(div_star[i].get_text().strip())#获取第i部电影的主演
        data.append(div_time[i].get_text().strip())#获取第i部电影的上映时间
        data.append(div_score[i].get_text().strip())#获取第i部电影的评分 #
        #print(data) #time.sleep(1) #将第i部电影的参数加入到全局list中
        DATA.append(data)
        result = homes.insert_one({'DATA':DATA})
        print(result)
        #将第i部电影的参数写入csv文件中 加上 newline=''
        #  可以去掉csv中的空白行 #加上
        # encoding='gb18030' 会让csv文件中能够正常显示中文，否则乱码
        with open('3MaoyanTOP100.csv', 'w', newline='',encoding='gb18030') as f:
            writer = csv.writer(f)
            writer.writerows(DATA)
    #定义一个全局的List变量
DATA = []
     #遍历所有网址，不同页面网址之间只有offset后面的数值有差异
for i in range(0, 100, 10):
    # 从0开始，每次增加10，到100结束，不包括100
    url = "http://maoyan.com/board/4?offset=" + str(i)
    # 调用函数
    getcontent(url)