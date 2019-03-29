import pandas as pda
import numpy as npy
import matplotlib.pylab as plt
data=pda.read_csv(r"D:\Python\data\hexun.csv")
data.values
data2=data.T # 转置
y1=data2.values[3]
x1=data2.values[4]
#plt.plot(x1,y1)
#plt.show()
x2=data2.values[0]
# plt.plot(x2,y1)
# plt.show()
plt.plot(x2,x1)
plt.show()