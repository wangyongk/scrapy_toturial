import csv

#导入csv文件
filename='sitka_weather_07-2014.csv'

#打开csv文件
with open(filename) as f:
    #读取
    reader=csv.reader(f)
    #模块csv 包含next()函数,调用它并将阅读器对象
    # 传递给它时，他将返回到文件中的下一行
    header_row=next(reader)
    for index,column_header in enumerate(header_row):
        #调用enumerate 来获取每个元素的索引
        #及其值
        print(index,column_header)
        '''
        获取每天的最高气温
        '''
    highs=[]
    for row in reader:
        # 将得到的字符串转换为数字，
        # 让matplotlib能读取他们
        high=int(row[1])
        highs.append(high)
    print(highs)