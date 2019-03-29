import matplotlib.pylab as plt
import numpy as npy
data=npy.random.normal(100.0,10.0,100)
# plt.hist(data)
# plt.show()
data2=npy.random.random_integers(1,25,1000)
#plt.hist(data2)
#plt.show()
# plt.subplot(5,3,2) #行、列、位置
# plt.show()
plt.subplot(2,2,1)
x1=[1,2,3,4,5]
y1=[1,4,9,16,25]
plt.plot(x1,y1)

plt.subplot(2,2,2)
y2=[1,2,3,4,5]
x2=[1,4,9,16,25]
plt.plot(x2,y2)

plt.subplot(2,1,2)
plt.show()