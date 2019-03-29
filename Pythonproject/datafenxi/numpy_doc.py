import numpy as np
#a=np.arange(15).reshape(3,5)

#a.shape
# 数组的：数组的维度。
# 为一个表示数组在每个维度上大小的整数元组。
# 例如二维数组中，表示数组的“行数”和“列数”。
#a.ndim
#数组的维数 数组轴的个数 即数组的秩
#a.dtype.name
# 数组中元素类型的对象
#a.itemsize
# 数组中每个元素的字节大小
# Array Creation
#a=arrany([1,2,3,4]) #创建一个数组
# 创建时指定数据类型
#c = np.array( [ [1,2], [3,4] ], dtype=complex )
#print(c)
# 创建一个充满零的数组
#d=np.zeros((3,4))
#print(d)
#创建一个充满一的数组
#e=np.ones((3,4),dtype=np.int16)
#print(e)
# 创建一个数组 初始内容是随机的
#f=np.empty((2,3))
#print(f)
#import sklearn
from numpy import pi
# x=np.linspace(0,2,9) # 9 numbers from 0 to 2
# print(x)
# y=np.linspace(0,2*pi,100)
# print(y)
# z=np.sin(y)
# print(z)
a=np.random.random((4,2,3))# 产生随机数
print(a)
print(a.sum())
print(a.min())
print(a.max())
np.setdiff1d()
np.setdiff1d