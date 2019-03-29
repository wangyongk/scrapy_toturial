import pymysql
import numpy as np
import pandas as pda
import matplotlib.pylab as plt
# 导入数据
coon=pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="newschema")
sql="select * from taob"
data=pda.read_sql(sql,coon)
print(data.describe())

#数据清洗
#发现缺失值
x=0
data["price"][(data["price"]==0)]=None
for i in data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]:
            data[i][j]="36"
            x+=1
print(x)
# 异常值处理
# 画散点图(x轴:价格 y轴:评论数)
#得到价格
data2=data.T
price=data2.values[2]
comment=data2.values[3]
# plt.plot(price,comment,"o")
# plt.show()

# 处理
line=len(data.values)
col=len(data.values[0])
da=data.values
for i in range(0,line):
    for j in range(0,col):
        if (da[i][2]>2300):
            print(da[i][j])
            da[i][2]=36
        if (da[i][3]>20000):
            da[i][3]=58
da2=da.T #转置
price=da2[2]
comt=da2[3]
plt.plot(price,comt,"o")
plt.show()
# 分布分析
pricemax = da2[2].max()
pricemin = da2[2].min()
commentmax = da2[3].max()
commentmin = da2[3].min()
# 极差：最大值-最小值
pricerg = pricemax - pricemin
commentrg = commentmax - commentmin
# 组距：极差/组数
pricedst = pricerg / 12
commentdst = commentrg / 12
# 画价格的直方图
pricesty = np.arange(pricemin, pricemax, pricedst)
plt.hist(da2[2], pricesty)
plt.show()