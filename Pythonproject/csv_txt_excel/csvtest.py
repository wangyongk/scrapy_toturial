'''
    CSV文件的规范
1、使用回车换行（两个字符）作为行分隔符，最后一行数据可以没有这两个字符。
2、标题行是否需要，要双方显示约定
3、每行记录的字段数要相同，使用逗号分隔。逗号是默认使用的值，双方可以约定别的。
4、任何字段的值都可以使用双引号括起来. 为简单期间，可以要求都使用双引号。
5、字段值中如果有换行符，双引号，逗号的，必须要使用双引号括起来。这是必须的。
6、如果值中有双引号，使用一对双引号来表示原来的一个双引号

原文：https://blog.csdn.net/luanpeng825485697/article/details/78358997
'''
import csv
#1 csv文件的写入
#打开文件，追加a
out=open('test_csv.csv','a',newline='')
#设定写入模式
csv_writer=csv.writer(out,dialect='excel')
#设置数据
data1=['ad',24]
#写入具体内容
csv_writer.writerow(data1)
print("over")

#2 csv 文件打开
with open('test_csv.csv','r',encoding='utf-8') as csvfile:
    read = csv.reader(csvfile)
    for i in read:
        print(i)

# 3 pandas写入读取csv
import pandas as pd
#pandas将数据写入csv文件
Data = {
        'english': ['one','two','three'],
         'number': [1,2,3]
         }
save = pd.DataFrame(Data,
                    index=['row1','row2','row3'],
                    columns=['english','number']
                    )
print(save)
save.to_csv('test1.csv',sep=',')

#  sep分隔符，
# encoding编码
# header=None自动列名，
# names自定义列名，
# index_col作为行索引的列（主键）,
# skiprows跳过行索引,na_values缺失值的替代字符串
df = pd.read_csv('test1.csv',sep=',',
                 encoding='gbk',
                 names=['column1','column2','column3'],
                 index_col=['column1'],
                 skiprows=[0],
                 na_values=['NULL']
                 )
print(df)
