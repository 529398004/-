from cProfile import label

import matplotlib.pyplot as plt
import numpy as np


# 定义数据产生函数
def sin(start1, end1):
    # 使用np.linspace产生1000个等间隔的数据
    x = np.linspace(start1, end1, 1000)
    return x, np.sin(x)


start = -10
end = 10

data_x, data_y = sin(start, end)

# figure与axes对象，使用subplots默认只生成一个axes
figure, axes = plt.subplots()
axes.plot(data_x, data_y)
plt.ylabel("sin(x)")
plt.title('Plot of sin(x)')
# 显示图中标签
# axes.legend()
# 显示图中的网格
axes.grid()
# 显示图像
plt.show()
