#txt读文件
# open(filename,打开方式,编码方式)
'''
w 以写方式打开，
a 以追加模式打开
r+ 以读写模式打开
w+ 以读写模式打开 不存在即创建
a+ 以读写模式打开
'''
#   写文件
#1 简单读取文件
f = open('txttest.txt','r',encoding='UTF-8')
str=f.read()
print(str)

#2 简单写入文件 会覆盖文档已有内容
f = open('txttest.txt','w',encoding='UTF-8')
f.write('12')

#3追加写入文件 不会覆盖已有内容
f = open('txttest.txt','a',encoding='UTF-8')
f.write('34')

#4读写模式打开写入文件 文件不存在会自动创建(a+具有相同作用)
#w+会覆盖掉文件内已经存在的内容 a+不会
f = open('txttest5.txt','a+',encoding='UTF-8')
f.write('5678')

#5按行写入数据(单行)
f = open('txttest3.txt','a+',encoding='UTF-8')
f.write('\n678')

#6将多个变量同时写入一行中,使用writelines()函数
f = open('txttest3.txt','a+',encoding='UTF-8')
f.writelines(['\nthe fourth writing...',',','good'])

# 读文件
#1简单读取
f = open('txttest.txt','r',encoding='UTF-8')
str=f.read()
print(str)

#2按行读取文件
#2.1简单按行读取
f = open('txttest.txt','r',encoding='UTF-8')
line= f.readlines()
while line:
    print(line)
    line = f.readline()
#2.2读取文件并存到list中
result=[]
with open('txttest.txt','r',encoding='UTF-8')as f:
	for line in f:
		result.append(list(line.strip('\n').split(',')))
print(result)
f.close()