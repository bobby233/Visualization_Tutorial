from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """生成随机漫步的类"""

    def __init__(self, num_points=5000):
        """初始化所有的属性"""
        self.num_points = num_points

        # 所有随机漫步初始于(0, 0)
        self.xvalues = [0]
        self.yvalues = [0]
    
    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到到达指定的长度
        while len(self.xvalues) < self.num_points:

            # 决定前进的方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.xvalues[-1] + x_step
            next_y = self.yvalues[-1] + y_step

            self.xvalues.append(next_x)
            self.yvalues.append(next_y)

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    # 绘制点并将图形显示出来
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.xvalues, rw.yvalues, c=point_numbers, cmap=plt.cm.Blues, s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.xvalues[-1], rw.yvalues[-1], c='red', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    plt.savefig('random_walk.png', bbox_inches='tight')

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break