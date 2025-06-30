import numpy as np
import matplotlib.pyplot as plt

# 定义计算概率的函数
def footfall_probability(x, y, mu_x, mu_y, sigma_x, sigma_y, beta, direction='up', noise_strength=0.05):
    """
    计算上楼梯或下楼梯的足迹概率，并加入一定的噪声模拟不规则磨损。
    
    参数：
    x, y        : 当前点的坐标
    mu_x, mu_y  : 坐标的期望位置
    sigma_x, sigma_y : 坐标分布的标准差
    beta        : 偏移修正因子
    direction   : 'up' 表示上楼梯，'down' 表示下楼梯
    noise_strength : 噪声强度，控制不规则磨损的程度
    
    返回值：
    p           : 给定点的足迹概率（带噪声）
    """
    # 判断方向，计算对应的偏移
    if direction == 'up':
        mu_x_corrected = mu_x + beta
    elif direction == 'down':
        mu_x_corrected = mu_x - beta
    else:
        raise ValueError("direction should be 'up' or 'down'")
    
    # 计算二维高斯分布的概率密度函数
    p = (1 / (sigma_x * sigma_y * np.sqrt(2 * np.pi))) * np.exp(
        -((x - mu_x_corrected)**2 / (2 * sigma_x**2) + (y - mu_y)**2 / (2 * sigma_y**2))
    )
    
    # 加入噪声以模拟不规则磨损
    noise = np.random.normal(0, noise_strength, size=p.shape)
    p = p + noise
    
    # 确保概率不为负数
    p = np.clip(p, 0, None)
    
    return p

# 设置参数
mu_x_up = 5        # 上楼梯时 x方向的期望位置
mu_y_up = 10       # 上楼梯时 y方向的期望位置
mu_x_down = 5      # 下楼梯时 x方向的期望位置，偏左
mu_y_down = 4      # 下楼梯时 y方向的期望位置，偏下
sigma_x = 2        # x方向的标准差
sigma_y = 2        # y方向的标准差
beta = 1           # 偏移修正因子
noise_strength = 0.05  # 噪声强度

# 创建网格，计算不同点的概率
x_vals = np.linspace(0, 10, 100)
y_vals = np.linspace(0, 15, 100)
X, Y = np.meshgrid(x_vals, y_vals)

# 计算上楼梯和下楼梯的概率（加入噪声）
Z_up = np.vectorize(lambda x, y: footfall_probability(x, y, mu_x_up, mu_y_up, sigma_x, sigma_y, beta, direction='up', noise_strength=noise_strength))(X, Y)
Z_down = np.vectorize(lambda x, y: footfall_probability(x, y, mu_x_down, mu_y_down, sigma_x, sigma_y, beta, direction='down', noise_strength=noise_strength))(X, Y)

# 绘制结果
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# 上楼梯的概率图
ax[0].contourf(X, Y, Z_up, cmap='viridis')
ax[0].set_title("Footfall probability when ascending the stairs")
ax[0].set_xlabel("x coordinate")
ax[0].set_ylabel("y coordinate")

# 下楼梯的概率图
ax[1].contourf(X, Y, Z_down, cmap='viridis')
ax[1].set_title("Footfall probability when descending the stairs")
ax[1].set_xlabel("x coordinate")
ax[1].set_ylabel("y coordinate")

plt.tight_layout()
plt.show()

