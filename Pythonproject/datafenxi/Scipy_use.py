import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
"""
    集成（scipy.integrate)

    详情参考：https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html
    返回值 第一个元素保存积分的估计值，第二个元素保持错误的上限

"""
import scipy.integrate as integrate
import scipy.special as special
result=integrate.quad(lambda x:special.jv(2.5,x),0,4.5)
print(result)
