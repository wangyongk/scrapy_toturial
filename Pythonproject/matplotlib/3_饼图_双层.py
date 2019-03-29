import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['STKaiti'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
s={'S0': 3, 'S1': 19, 'S2': 6, 'S3': 2}
s_labels=list(sorted(s.keys()))
s_fracs=[s.get(s_labels[i]) for i in range(len(s_labels))]

p={'P0': 1, 'P1': 5, 'P2': 16, 'P3': 8}
p_labels=list(sorted(p.keys()))
p_fracs=[p.get(p_labels[i]) for i in range(len(p_labels))]
fig=plt.figure()
plt.pie(p_fracs, labels=p_labels,radius=0.9,autopct='%1.1f%%',pctdistance=0.8)
plt.pie(s_fracs, labels=s_labels,radius=0.6,autopct='%1.1f%%',pctdistance=0.8)
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
plt.title('s,p因素等级分布图',fontsize=20)
plt.show()
