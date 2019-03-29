# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:27:44 2018

@author: wangyongkang
"""
import
seq=range(5)
print(enumerate(seq))

list1 = ["这", "是", "一个", "测试"]
for i in range (len(list1)):
    print(i,list1[i])
print("--------------------------")
# enumerate还可以接收第二个参数，用于指定索引起始值，如：
#enumerate(list2,0) i 从零开始
list2 = ["这", "是", "一个", "测试"]
for i,j in enumerate(list2,0):
    print(i,j)