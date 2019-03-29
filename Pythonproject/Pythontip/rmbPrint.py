# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 20:23:16 2018

@author: wangyongkang
"""
"""
digit = [u'零', u'壹', u'贰', u'叁', u'肆', u'伍', u'陆', u'柒', u'捌', u'玖']
unit = [u'', u'拾', u'佰', u'仟', u'万']
a = 9000


def chinesenum(x):
    s = ''
    if x == 0:  # 判断x是否为零，x为零的话字符串为空
        s = ''
    u = 0  # 用来索引unit的变量

    while x % 10 == 0:  # 摘除最小位开始的连续零的情况
        x = x//10
        u = u+1
    while x != 0:
        d = int(x % 10)
        if d != 0:   # 如果当前位的值非零，才要加单位
            s = unit[u] + s
        if not(len(s) > 0 and s[0] == u'零'):  # 如果上一位是零，不要重复叠加零
            s = digit[d] + s
        x = x//10
        u = u+1
    return s


num1 = abs(a)//10000  # 一万以上的部分
num2 = abs(a) % 10000  # 一万以下的部分

s1 = chinesenum(num1)
s2 = chinesenum(num2)


if num1 == 0 and num2 == 0:
    st = u'零圆'
elif num1 == 0:
    st = u'%s圆' % s2
else:
    if 0 < num2 < 1000:
        st = u'%s万零%s圆' % (s1, s2)
    else:
        st = u'%s万%s圆' % (s1, s2)
if a < 0:
    st = u'负'+st
print(st)




mod1=u'零壹贰叁肆伍陆柒捌玖'
mod2=u' 拾佰仟万拾佰仟'
yuan=u'圆'
sig=u''

def trans(a):
    nozero=1
    p=''
    t=0
    pos=0
    if a==0:
        return u'零'
    while a!=0:
        t=a%10
        if pos==4:
            nozero=1
        if t==0 :
            if pos==4:
                p=u'万'+p
            if nozero==0:
                p=mod1[0]+p
                nozero=1
        else:
            nozero=0
            if pos>0:
                p=mod1[t]+mod2[pos]+p
            else:
                p=mod1[t]
        pos=pos+1
        a=a/10
    return p

if a<0:
    sig=u'负'
    a=a*(-1)

print (sig+trans(a)+yuan).decode("utf8")

year="2012"
year = int(year)
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('366')
else:
    print('365')
    
a=123456678
sx=''
def change(n):
    unit = u'负圆拾佰仟万拾佰仟'
    num = u'零壹贰叁肆伍陆柒捌玖'
    if n < 0:
        sign = unit[0]
    elif n == 0:
        return u'零圆'
    else:
        sign = ''
    
    lst = []
    for i in str(abs(n)):
        lst.append(num[int(i)])         
    length = len(lst)
    i_lst = []    
    for i in range(length):
        index = (length - i)
        if lst[i] == u'零':
            i_lst.append(lst[i])
            if i_lst[i - 1] == u'零':
                i_lst[i - 1] = ''            
            if index % 4 == 1:
                i_lst[i] = unit[index]            
        else:
            i_lst.append(lst[i] + unit[index])            
        
    s = ''.join(i_lst)
    s = sign + s
    return s
sx=change(a)

    
    
"""


a=-12233457
num = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
unit = ['亿', '万', '仟', '佰', '拾', '']
baseList = [100000000, 10000, 1000, 100, 10, 1, 0]
def rmb(money):
	L = []
	level = 0
	while baseList[level] > money : level += 1
	base = baseList[level]
	if base <= 1:
	    L.append(num[money])
	else:
		L.extend(rmb(money // base))
		L.append(unit[level])
		r = money % base
		if r:
		    if r * 10 < base : L.append(num[0])
		    L.extend(rmb(r))
	
	return L


L = []
if a<0 :
    
    L.append('负')
    print("----------")
    a = -a


L.extend(rmb(a))
L.append('圆')


print(u''.join(L))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
