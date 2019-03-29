import numpy as np
import matplotlib.pyplot as plt
# numpy.random.random() 生成随机浮点数 范围是0.0-1.0,
#a=np.random.random()
#print(a)
#通过参数size设置返回数据的size;
#size=(3,2)代表3行两列
#b=np.random.random(size=(3, 2))
#print(b)
# numpy.random.randint() 产生随机整数
# randint(low ,high,size,dtype)
# 设置方式 1：标明参数名称 randint(low=3,high=10,size=(2,3))
# 设置方式 2：randint(3,10,(2,3))
# c1=np.random.randint(3)
# c2=np.random.randint(3,size=(3))
# c3=np.random.randint(3,8,size=(2,3))
# print(c1)
# print(c2)
# print(c3)
#
#numpy.random.normal() 　高斯分布随机数
#normal(loc=0.0, scale=1.0, size=None)
#loc：均值，scale：标准差，size：抽取样本的size
# n=np.random.normal(loc=2,scale=1,size=(2,3))
# print(n)
# numpy.random.randn()　标准正态分布随机数
# 从标准正态分布中返回一个(d0*d1* …* dn)维样本值
#print(np.random.rand(4,2))
# numpy.random.rand()　生成[0, 1)间随机数
# x=range(0,8,1)
# print(x)
# numpy.random.shuffle()　随机打乱序列
# numpy.random.choice()　随机选取序列的一个元素
#print(np.random.choice(['a','b','c','d','e']))
#输出（9个小于5的元素）
#print(np.random.choice(5,9))
#  p=[0,0,0,0,1] 设置各个元素出现的概率
#print(np.random.choice(5,3, p=[0,0,0,0,1]))
'''
numpy.random.binomial()　二项分布采样
size:采样的次数,n p即式中的n p;函数的返回值表示n中发生/成功的次数s.
https://docs.scipy.org/doc/numpy/reference/
generated/numpy.random.binomial.html#numpy.random.binomial
'''
# s1=sum(np.random.binomial(2, 0.1, 2000000) == 0)/2000000
# s2=sum(np.random.binomial(2, 0.1, 2000000) == 1)/2000000
# s3=sum(np.random.binomial(2, 0.1, 2000000) == 2)/2000000
# s=s1+s2+s3
# print(s)
'''
print("--------直方图-------------")
histogram应用于数组的NumPy 函数返回一对向量：
数组的直方图和bin的向量。注意：
 matplotlib还有一个构建直方图的功能
（hist在Matlab中称为），与NumPy中的直方图不同。
主要区别在于pylab.hist自动绘制直方图，
而 numpy.histogram只生成数据。
'''
# import numpy as np
# import matplotlib.pyplot as plt
# mu,sigma=2,0.5
# v=np.random.normal(mu,sigma,10000)
# plt.hist(v,bins=50,density=1)
# plt.show()


'''
   存取元素
'''
a=np.arange(10)
a[4] # 用整数作为下标可以获取数组中的某个元素
a[3:5] #  用范围作为下标获取数组的一个切片，包括 a[3] 不包括 a[5]
a[:5] #  省略下标从0开始
a[::-1]  # 下标可以使用负数，表示从数组后往前数
a[2:4]= 100, 101  # 下标还可以用来修改元素的值

print(a)
