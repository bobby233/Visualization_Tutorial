#一次模拟分数趋势的折线图
import matplotlib.pyplot as plt

dates = [2, 3, 4, 5]
scores = [100, 100, 40, 100]
plt.plot(dates, scores, linewidth=7)

plt.title('Maths Scores', fontsize=30)
plt.xlabel('Dates', fontsize=17)
plt.ylabel('Scores', fontsize=17)

plt.tick_params(axis='both', labelsize=15)

plt.show()
