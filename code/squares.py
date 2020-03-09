import matplotlib.pyplot as plt

values = list(range(1, 1000))
squares = list(v**2 for v in range(1, 1000))
plt.scatter(values, squares, s=40, c=squares, cmap=plt.cm.Blues)

plt.title('Squares of Numbers', fontsize=24)
plt.xlabel('Numbers', fontsize=14)
plt.ylabel('Squares', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.show()