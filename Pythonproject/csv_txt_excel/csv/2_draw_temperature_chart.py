import csv
import matplotlib.pyplot as plt

# 导入csv文件
filename = 'sitka_weather_07-2014.csv'

# 打开csv文件
with open(filename) as f:
    # 读取
    reader = csv.reader(f)
    # 模块csv 包含next()函数,调用它并将阅读器对象
    # 传递给它时，他将返回到文件中的下一行
    header_row = next(reader)
    # 获取每天的最高气温
    highs = []
    for row in reader:
        # 将得到的字符串转换为数字，
        # 让matplotlib能读取他们
        high = int(row[1])
        highs.append(high)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
# 设置图表格式
# 设置标题
plt.title("Daily high tempatures July 2014",fontsize=24)
#设置x轴标签
plt.xlabel('',fontsize=16)
# 设置y轴标签
plt.ylabel("tempature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()
