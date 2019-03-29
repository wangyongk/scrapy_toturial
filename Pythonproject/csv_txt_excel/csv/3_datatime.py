from datetime import datetime
import csv
import matplotlib.pyplot as plt

# 导入csv文件
filename = 'sitka_weather_2014.csv'

# 打开csv文件
with open(filename) as f:
    # 读取
    reader = csv.reader(f)
    # 模块csv 包含next()函数,调用它并将阅读器对象
    # 传递给它时，他将返回到文件中的下一行
    header_row = next(reader)
    # 获取每天的最高气温
    dates,highs,lows = [],[],[]
    for row in reader:
        # 将得到的字符串转换为数字，
        # 让matplotlib能读取他们
        current_date=datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)
fig = plt.figure(dpi=128, figsize=(10, 6))

# alpha 指定颜色的透明度，Alpha值为0表示完全透明，默任设置为1表示完全不透明
# 透过将alpha设置为0.5可以让红色和蓝色折线看起来更浅
plt.plot(dates,highs, c='red',alpha=0.5)
plt.plot(dates,lows, c='blue',alpha=0.5)

# fill_between() 传递了x值系列，列表dates,传递了两个y值：highs和lows
# facecolor 指定了填充区域的颜色
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# 设置图表格式
# 设置标题
plt.title("Daily high and low tempatures - 2014",fontsize=24)
#设置x轴标签
plt.xlabel('',fontsize=16)
# 设置y轴标签
fig.autofmt_xdate()
plt.ylabel("tempature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()

# 方法strptime()可以接受各种实参,
#
# first_data=datetime.strptime('2014-7-1','%Y-%m-%d')
# print(first_data)

"""
%A          星期的名称，如Monday
%B          月份名，如January
%m          用数字表示的月份(01~12)
%d          用数字表示月份中的一天(01~31)
%Y          四位的年份，如2015
%y          两位的年份，如15
%H          24小时制的小时数(00~23)
%I          12小时制的小时数(01~12)
%p          am或pm
%M          分钟数(00~59)
%S          秒数(00~61)
"""