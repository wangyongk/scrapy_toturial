import matplotlib.pyplot as plt
import numpy as np

n=1024
X=np.random.normal(0,1,n)
Y=np.random.normal(0,1,n)
T=np.arctan2(X,Y)
plt.scatter(X,Y,s=75,c=T,alpha=0.5)
#plt.scatter(np.arange(5),np.arange(5))
plt.show()