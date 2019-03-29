import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['STKaiti'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
labels = 'Frogs','Hogs','Dogs','Logs'
sizes = [15,30,45,10]
explode = (0,0.1,0,0) #0.1表示将Hogs那一块凸显出来
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90) #startangle表示饼图的起始角度
plt.title(u'饼图',fontsize=22)
plt.axis('equal')  #加入这行代码即可！
plt.show()