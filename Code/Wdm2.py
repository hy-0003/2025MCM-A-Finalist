import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# 假设一些材料的参数
d_values_wood = np.linspace(12, 20, 100)  # Wood的深度 d ∈ [12, 20]
d_values_concrete = np.linspace(6, 12, 100)  # Concrete的深度 d ∈ [6, 12]
d_values_stone = np.linspace(0, 6, 100)  # Stone的深度 d ∈ [0, 6]

m_values = np.array([1, 2, 3])  # 不同材料的索引 m 对应木头、石头、混凝土

# 设定常数
rho_0 = 100  # 假设的参考电阻率 ρ0
V_total = 10  # 假设的总体积
n = 1.5  # 假设的指数 n

# 假设的 r 和 ρ 的变化方式
r_d_m = lambda d, m: 0.1 * m * np.exp(0.1 * d)  # r(d,m) 随深度变化
rho_d_m = lambda d, m: rho_0 * (1 + 0.05 * m) * np.exp(0.02 * d)  # ρ(d,m) 随深度变化

# 计算 W(d,m)，加入噪声，但保持单调递增
def W_with_noise(d, m, noise_factor=0.05):
    r = r_d_m(d, m)
    rho = rho_d_m(d, m)
    W_values = r * V_total * (rho_0 / rho) ** n
    noise = np.random.normal(0, noise_factor, size=d.shape)  # 生成噪声
    W_values += noise
    # 保证W(d,m)单调递增
    W_values = np.maximum.accumulate(W_values)
    return W_values

# 创建自定义的黄绿蓝渐变配色，保持色彩柔和
cmap = LinearSegmentedColormap.from_list("yellow_green_blue", ["yellow", "lightgreen", "lightblue", "blue"])

# 绘制不同材料下的 W(d,m)
fig, ax = plt.subplots(figsize=(10, 6))

# 手动定义材料名称，翻译为英文
material_names = {1: "Stage 1", 2: "Stage 2", 3: "Stage 3"}

# 为不同的材料绘制W(d,m)，并设置渐变颜色
for m, d_values in zip(m_values, [d_values_wood, d_values_stone, d_values_concrete]):
    # 计算W(d,m)值
    W_values = W_with_noise(d_values, m)
    
    # 根据每个d值的范围来计算颜色
    norm = plt.Normalize(d_values.min(), d_values.max())  # 对每个深度范围进行标准化
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)  # 映射标准化的深度值到颜色
    
    # 绘制渐变色的线条
    for i in range(1, len(d_values)):
        ax.plot(d_values[i-1:i+1], W_values[i-1:i+1], color=sm.to_rgba(d_values[i]))  # 每一段的渐变颜色

# 添加颜色条
sm.set_array([])  # 这是为了使颜色条正常显示
cbar = fig.colorbar(sm, ax=ax)  # 将颜色条添加到图形的指定轴

plt.title(r"Wear Value $W(d, m)$ for Different Stages", fontsize=14)
plt.xlabel("Depth (d)", fontsize=12)
plt.ylabel("Wear Value $W(d, m)$", fontsize=12)
plt.legend(title="Stages", fontsize=12)  # "阶段"翻译为"Stages"

# 去掉网格
plt.grid(False)

plt.show()



