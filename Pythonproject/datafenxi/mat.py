import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)
# plot the second curve in this figure with certain parameters
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
# set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set new ticks
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           ['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])
# to use '$ $' for math text and nice looking, e.g. '$\pi$'

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
# ACCEPTS: [ 'top' | 'bottom' | 'both' | 'default' | 'none' ]

ax.spines['bottom'].set_position(('data', 0))
# the 1st is in 'outward' | 'axes' | 'data'
# axes: percentage of y axis
# data: depend on y data

ax.yaxis.set_ticks_position('left')
# ACCEPTS: [ 'left' | 'right' | 'both' | 'default' | 'none' ]

ax.spines['left'].set_position(('data',0))
plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# x=np.linspace(-1,1,50)
# y1=2*x+1
# y2=x**2
#
# plt.xlim(-1,2)
# plt.ylim(-2,3)
#
# plt.xlabel("I am x")
# plt.ylabel("I am y")
#
# new_ticks=np.linspace(-1,2,5)
# print(new_ticks)
#
# plt.xticks(new_ticks)
# plt.yticks([-2,-1,1,2,3],
#            [r'$reall \ good$',r'$ good$',r'$ bad$',r'$reall \ bad$',r'$worse$']
#            )
# ax=plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
#
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
#
#
# plt.plot(x,y1,color='red',linestyle='--',linewidth=1.0)
# plt.show()
#


















# import matplotlib.pyplot as plt
# import numpy as np
# x=np.linspace(-1,1,50)
# y1=2*x+1
# y2=x**2
#
# plt.xlim(-1,2)
# plt.ylim(-2,3)
#
# plt.xlabel("I am x")
# plt.ylabel("I am y")
#
# new_ticks=np.linspace(-1,2,5)
# print(new_ticks)
#
# plt.xticks(new_ticks)
# plt.yticks([-2,-1,1,2,3],
#            [r'$reall \ good$',r'$ good$',r'$ bad$',r'$reall \ bad$',r'$worse$']
#            )
#
# l1,=plt.plot(x,y1,label='up')
# l2,=plt.plot(x,y2,color='red',linestyle='--',linewidth=1.0,label='down')
# plt.legend(handles=[l1,l2],labels=['a','b'],loc='best')
#
# plt.show()
















# import matplotlib.pyplot as plt
# import numpy as np
# x=np.linspace(-1,1,50)
# y=2*x+1
# plt.figure(num=12,figsize=(8,5))
# plt.plot(x,y,color='red',linestyle='--',linewidth=1.0)
#
# plt.xlim(-1,2)
# plt.ylim(-2,3)
#
# plt.xlabel("I am x")
# plt.ylabel("I am y")
#
# new_ticks=np.linspace(-1,2,5)
# print(new_ticks)
#
# plt.xticks(new_ticks)
# plt.yticks([-2,-1,1,2,3],
#            [r'$reall \ good$',r'$ good$',r'$ bad$',r'$reall \ bad$',r'$worse$']
#            )
# plt.show()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# '''
# # 折线图，散点图
# import matplotlib.pylab as plt
# import numpy as npy
# x=[1,2,3,4,8]
# y=[5,7,2,1,5]
# # plt.plot(x,y,'o')# plot(x轴数据,y轴数据,展现形式)
# # plt.show()
#
# #plt.plot(x,y,'*')
# #plt.show()
#
#   颜色
# c-cyan--青色
# r-red--红色
# g-green--绿色
# b-blue--蓝色
# y-yellow--黄色
# k-black--黑色
# w-white--白色
#    线条样式
#    - 直线
#    --虚线
#    -. -.形式
#    : 细小虚线
#    点的样式
#    s --方形
#    h --六角形
#    H --六角形
#    * --星形
#    + --加号
#    x --x型号
#    d --菱形
#    D --菱形
#    p -- 五角星
# plt.plot(x,y)
# plt.title("show")
# plt.xlabel("ages")
# plt.ylabel("temp")
# plt.xlim(1,20)
# plt.ylim(1,20)
# #plt.show()
# #随机数的生成
# data=npy.random.random_integers(1,20,1000) # start end number
# #print(data)
# # 生成具有正态分布的随机数
# data2=npy.random.normal(1,3,4)# 均数、西格玛数、个数
# #print(data2)
# '''