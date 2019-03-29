# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 09:44:16 2018

@author: wangyongkang
"""

"""

结尾0的个数 
"""
L=[2,3,50,3,13,7,9,9]


product,count=1,0
s=1
for j in L:
    s=s*j
for i in [i for i in L if i%2==0 or i%5==0]:
    product*=i
    while product%10==0:
        product=product//10
        count+=1
print(count)
print(s)
s=s//10**count
print(s)
s=s%10
print(s)
if s%2==0:
    print(0)
else:
    print(1)
# 依次乘列表中的每个元素，每次乘完之后处理一下，只剩下非零的最小位的那个数，与下一个元素进行相乘；
num = 1
for i in L: #遍历列表中的元素；
    num = num*i
    while num % 10 == 0: # 这个while循环剥除末尾的所有零；
        num = num/10
    num = num % 10  #取剥除零后的最小位，接下来与下一个列表中的元素相乘；

if num % 2 == 0:
    print(0)
else:
    print(1)
    
    
"""
光棍们对1总是那么敏感，因此每年的11.11被戏称为光棍节。小Py光棍几十载，
光棍自有光棍的快乐。让我们勇敢地面对光棍的身份吧，
现在就证明自己：
给你一个整数a，数出a在二进制表示下1的个数，并输出。

例如：a=7

则输出：3
"""
import math
a=15
s=0
a=a+1
while a%2==0:
    s=s+1
    a=a/2
print(s)


a=7
s=bin(a)
s=str(s)
print(s.count('1'))

print("-----------------")
a=15
count = 0
while a > 0:
    if a%2 == 1:
        count += 1
    a //= 2
    print(a)
print(count)


import this
print(this.s)

"""
给你两个正整数a,b,  输出它们公约数的个数。
例如：a = 24， b = 36
则输出：6
"""
c=0
a,b=24,36
for i in range(1,min(a,b)+1):
    if a%i==0and b%i==0:
        c=c+1;
print(c)
    

L=[]
for x in range(1,min(a,b)+1):
   if a%x==0:
      if b%x==0:
         L.append(x)
print(len(L))
print(L)

"""
我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。
今天我们反其道而行之，给你两个数a和b，
计算出它们分别是哪两个数的最大公约数和最小公倍数
。输出这两个数，小的在前，大的在后，以空格隔开
。若有多组解，输出它们之和最小的那组。
注：所给数据都有解，不用考虑无解的情况。

例如：a=3, b = 60

则输出：12 15

"""

a=3
b=60
import math
L=[]
c=0
for i in range(int(math.sqrt(a*b))-1,0,-1):
    if i%a==0 and a*b/i%a==0:
        L.append(i)
        c=int(a*b/i)
        L.append(c)
        print(" ".join(str(j) for j in L))
        #print(i,int(a*b/i))
        break

print("---------------------------------------------------------")
"""
给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。
如果存在，则输出YES，否则输出NO。
回文串的定义：记串str逆序之后的字符串是str1，
若str=str1,则称str是回文串，如"abcba".

a="abcba"
b=a[::-1]
if b==a:
    print("YES")
else:
    print("NO")
"""
print("----------------------------------------------------------")
"""

给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 
请你给出这两个时间间隔的秒数。
如：st="00:00:00", et="00:00:10", 则输出10.
"""
st="00:00:00"
et="00:00:10"
import datetime
st=datetime.datetime.strptime(st,"%H:%M:%S")
et=datetime.datetime.strptime(et,"%H:%M:%S")
print((et-st).seconds)






















    
    