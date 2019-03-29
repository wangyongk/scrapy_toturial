import matplotlib.pyplot as plt

name_list = ['Monday', 'Tuesday', 'Friday', 'Sunday']
num_list = [1.5, 0.6, 7.8, 6]
num_list1 = [1, 2, 3, 1]
plt.bar(range(len(num_list)), num_list, label='boy', fc='r')
plt.bar(range(len(num_list)), num_list1, bottom=num_list, label='girl', tick_label=name_list, fc='g')
plt.legend()
plt.show()