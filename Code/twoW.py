import matplotlib.pyplot as plt
import numpy as np

# 设置数据
stairs = ['Wear value of the surface layer']
stairs1_w = [1000]

# 创建渐变色
cmap = plt.get_cmap('YlGnBu')  # 从黄色到绿色到蓝色的渐变

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(8, 4))

# 创建渐变颜色
norm = plt.Normalize(vmin=0, vmax=1000)  # 正规化颜色值（0到1000的范围）

# 为柱子创建渐变效果
bars = ax.barh(stairs, stairs1_w, height=0.5)

# 给柱子应用渐变色
for bar in bars:
    bar.set_color(cmap(norm(bar.get_width())))

# 添加标题和标签
ax.set_title("Wear Value for Stairs 1")
ax.set_xlabel("Wear Value (W)")
ax.set_xlim(0, 1100)  # 设置x轴范围，确保柱子能够完全显示

# 添加颜色条
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])  # 将颜色条添加到图表
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label('Wear Value Gradient')

# 显示图形
plt.tight_layout()
plt.show()


