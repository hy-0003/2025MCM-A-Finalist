import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义参数
r = 1.0  # 比例系数
rho_0 = 1.0  # 参考电阻率
V_values = np.linspace(0.1, 10, 200)  # 体积 V_total 的变化范围，增加分辨率
rho_values = np.linspace(0.1, 1.5, 200)  # 缩小电阻率比值范围，从 0.1 到 1.5
n_values = [1, 2, 3]  # 不同的 n 值

# 创建网格
V_grid, rho_grid = np.meshgrid(V_values, rho_values)

# 创建一个图形和 3D 子图
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 计算不同 n 值下的 W，并绘制多条曲线
for n in n_values:
    # 计算对应的 phi 值
    phi_grid = (rho_0 / rho_grid) ** (1 / n)
    
    # 计算 W
    W_grid = r * V_grid * phi_grid
    
    # 使用颜色映射绘制三维曲面
    surf = ax.plot_surface(V_grid, rho_grid, W_grid, cmap='viridis', alpha=0.8, edgecolor='none')
    
    # 给每个表面添加标签
    ax.text2D(0.05, 0.9 - 0.05 * n, f'n={n}', transform=ax.transAxes, fontsize=12, color='black')

# 添加标签和标题
ax.set_xlabel('Total Volume V_total', fontsize=14, fontweight='bold')
ax.set_ylabel('Resistivity Ratio ρ/ρ0', fontsize=14, fontweight='bold')
ax.set_zlabel('Wear Value W', fontsize=14, fontweight='bold')
ax.set_title('3D Sensitivity of Wear Value (W) to V_total and Resistivity Ratio (ρ/ρ_0)', fontsize=16, fontweight='bold')

# 添加颜色条
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# 设置背景为白色
fig.patch.set_facecolor('white')  # 设置图形背景颜色为白色
ax.set_facecolor('white')  # 设置坐标轴背景颜色为白色

# 禁用坐标面背景，使坐标面为白色
ax.xaxis.pane.fill = False  # 禁用 X 轴面板背景
ax.yaxis.pane.fill = False  # 禁用 Y 轴面板背景
ax.zaxis.pane.fill = False  # 禁用 Z 轴面板背景

# 调整视角
ax.view_init(elev=30, azim=45)  # 调整视角

# 显示图形
plt.tight_layout()
plt.show()
