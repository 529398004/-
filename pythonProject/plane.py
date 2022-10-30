import matplotlib.pyplot as plt          #导入库
from mpl_toolkits.mplot3d import Axes3D  #导入库
plt.rcParams['font.sans-serif'] = ['SimHei']                #解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False                  # 解决中文显示问题
plt.subplot(projection='3d')                                #设置3D绘图空间
x = [28.502, 28.1947, 34.3751, 44.3863, 46.3783, 35.2945,28.502]                      #设置x轴坐标
y = [-2, 0, 0, 0, -2, -2, -2]                                          #设置y轴坐标
z = [-13.9952, -13.9441, -15.9362, -19.1540, -19.1540, -15.9872, -13.9952]                #设置z轴坐标
plt.plot(x, y, z)                                           #绘制3个点对应连线的三维线性图
plt.xlabel('x轴')                                           #给横轴命名
plt.ylabel('y轴')                                           #给纵轴命名
plt.title('三维线图')                                        #添加标题
plt.show()