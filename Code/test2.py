import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 调整单人行走的参数
mu_x = 15  # 单人行走的均值
mu_y = 30  # 垂直方向的均值
sigma_x = 4  # 水平方向的标准差
sigma_y = 8  # 垂直方向的标准差

# 创建网格点
x = np.linspace(0, 30, 1000)  # 修改楼梯宽度方向的网格点为0到30
y = np.linspace(0, 60, 1000)  # 修改楼梯长度方向的网格点为0到60
X, Y = np.meshgrid(x, y)  # 生成二维网格

# 定义高斯概率密度函数
def gaussian(x, y, mu_x, mu_y, sigma_x, sigma_y):
    return (1 / (sigma_x * sigma_y * np.sqrt(2 * np.pi))) * np.exp(
        -((x - mu_x) ** 2 / (2 * sigma_x ** 2)) - ((y - mu_y) ** 2 / (2 * sigma_y ** 2))
    )


# 调整双人行走的参数
mu_x1, mu_x2 = 9, 21  # 两个人的偏移，考虑新的范围


mu_x3 = 15  # 第三个人的偏移



# 单人行走的概率密度函数

P_single = gaussian(X, Y, mu_x, mu_y, sigma_x, sigma_y)

# 双人行走的概率密度函数

P_double = gaussian(X, Y, mu_x1, mu_y, sigma_x, sigma_y) + gaussian(X, Y, mu_x2, mu_y, sigma_x, sigma_y)

# 三人行走的概率密度函数

P_triple = gaussian(X, Y, mu_x1, mu_y, sigma_x, sigma_y) + gaussian(X, Y, mu_x2, mu_y, sigma_x, sigma_y) + gaussian(X, Y, mu_x3, mu_y, sigma_x, sigma_y)




# 绘制单人行走的概率密度函数
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(131, projection='3d')
ax.plot_surface(X, Y, P_single, cmap='viridis')
ax.set_title('Single Person')
ax.set_xlabel('Width (x)')
ax.set_ylabel('Length (y)')
#ax.set_zlabel('Probability Density')
# 设置背景为白色
fig.patch.set_facecolor('white')  # 设置图形背景颜色为白色
ax.set_facecolor('white')  # 设置坐标轴背景颜色为白色

# 禁用坐标面背景，使坐标面为白色
ax.xaxis.pane.fill = False  # 禁用 X 轴面板背景
ax.yaxis.pane.fill = False  # 禁用 Y 轴面板背景
ax.zaxis.pane.fill = False  # 禁用 Z 轴面板背景



# 绘制双人行走的概率密度函数
ax = fig.add_subplot(132, projection='3d')
ax.plot_surface(X, Y, P_double, cmap='viridis')
ax.set_title('Two People')
ax.set_xlabel('Width (x)')
ax.set_ylabel('Length (y)')
#ax.set_zlabel('Probability Density')
# 设置背景为白色
fig.patch.set_facecolor('white')  # 设置图形背景颜色为白色
ax.set_facecolor('white')  # 设置坐标轴背景颜色为白色

# 禁用坐标面背景，使坐标面为白色
ax.xaxis.pane.fill = False  # 禁用 X 轴面板背景
ax.yaxis.pane.fill = False  # 禁用 Y 轴面板背景
ax.zaxis.pane.fill = False  # 禁用 Z 轴面板背景



# 绘制三人行走的概率密度函数
ax = fig.add_subplot(133, projection='3d')
ax.plot_surface(X, Y, P_triple, cmap='viridis')
ax.set_title('More People')
ax.set_xlabel('Width (x)')
ax.set_ylabel('Length (y)')
#ax.set_zlabel('Probability Density')
# 设置背景为白色
fig.patch.set_facecolor('white')  # 设置图形背景颜色为白色
ax.set_facecolor('white')  # 设置坐标轴背景颜色为白色

# 禁用坐标面背景，使坐标面为白色
ax.xaxis.pane.fill = False  # 禁用 X 轴面板背景
ax.yaxis.pane.fill = False  # 禁用 Y 轴面板背景
ax.zaxis.pane.fill = False  # 禁用 Z 轴面板背景



plt.tight_layout()
plt.show()