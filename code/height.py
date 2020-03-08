import matplotlib.pyplot as plt
ages = [10, 11, 12, 13]
heights = [170, 156, 189, 175]
plt.scatter(ages, heights, s=300, c='red')

plt.title('Heights of Different Ages', fontsize=30)
plt.xlabel('Ages', fontsize=17)
plt.ylabel('Heights', fontsize=17)

plt.show()