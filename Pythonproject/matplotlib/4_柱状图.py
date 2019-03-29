import matplotlib.pyplot as plt

num_list = [1.5, 0.6, 7.8, 6]
num_list = [1.5,0.6,7.8,6]
num_list = [1.5,0.6,7.8,6]
#plt.bar(range(len(num_list)), num_list,fc='r')
#设置颜色 fc='r'

name_list = ['Monday', 'Tuesday', 'Friday', 'Sunday']
plt.bar(range(len(num_list)), num_list,color='rgbr')
#设置颜色 color='rgbr'

plt.show()