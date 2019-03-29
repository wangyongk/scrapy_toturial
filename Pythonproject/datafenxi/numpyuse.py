'''
   #numpy模块
import numpy as np

#array创建一维数组
# 格式np.array([元素1,元素2,.....,元素n])
a=np.array([1,2,3,4])
#创建二维数组
#格式格式np.array([[元素1,元素2,.....,元素n],[元素1,元素2,.....,元素n]])
b=np.array([[1,2,3],[4,6,2],[7,3,9]])

#排序 b.sort() 对b排序 返回副本 本身b为已排序好的数组
b.sort()
print(b)
#最大值 b.max() 最小值b.min()
x=b.max()
print(x)

#切片
#数组[start:end+1]
a1=a[1:3] # a[1],a[2]
print(a1)
a2=a[:3]
print(a2)
a3=a[1:]
print(a3)

'''
# pandas

import pandas as pd
import numpy as np

dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df.describe())


