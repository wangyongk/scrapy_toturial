# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 08:22:40 2018

@author: wangyongkang
"""
"""
problem 排序

"""

def bubblesort(nums):
    for i in range(len(nums)):
        for j in range(1,len(nums)-i):
            if nums[j-1]>nums[j]:
                nums[j-1],nums[j]=nums[j],nums[j-1]
    return nums
nums = [5,2,45,6,8,2,1]

print(bubblesort(nums))

string='abcdef'

def string_reverse1(string):
    return string[::-1]
print(string_reverse1(string))

def string_reverse2(string):
    vector=[]
    for i in string:
        vector.append(i)
    vector.reverse()
    return ''.join(vector) #   将list转换成字符串
print(string_reverse2(string))


from collections import deque
def string_reverse3(string):
    d=deque()
    d.extendleft(string)
    return ''.join(d) #   将list转换成字符串
print(string_reverse3(string))






















