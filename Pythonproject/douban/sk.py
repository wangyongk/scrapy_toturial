# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 20:23:55 2018

@author: wangyongkang
"""

"""
file.read() 读取文件所有内容
file.readlines() 读取文件的全部内容 与file.read()不同之处在于readlines会把读取的
内容，赋给一个列表变量
file.readline() 读取一行内容

"""
import urllib.request

filename=urllib.request.urlopen("http://www.baidu.com")
response=urllib.request.urlopen("http://www.baidu.com").read().decode("utf-8", "ignore")
file=open("D:/1.html","w",encoding="utf-8")
file.write(response)
filename.info()
file.close()

