import numpy as np
import matplotlib.pyplot as plt

# 假设一些材料的参数
t_values = np.linspace(0, 20, 100)  # 服务时间 t 从 0 到 20
m_values = np.array([1, 2, 3])  # 不同材料的索引 m 对应木头、石头、混凝土

# 设定常数
rho_0 = 100  # 假设的参考电阻率 ρ0
V_total = 10  # 假设的总体积
n = 1.5  # 假设的指数 n

# 假设的 r 和 ρ 的变化方式
r_t_m = lambda t, m: 0.1 * m * np.exp(0.1 * t)  # r(t,m) 随时间变化
rho_t_m = lambda t, m: rho_0 * (1 + 0.05 * m) * np.exp(0.02 * t)  # ρ(t,m) 随时间变化

# 计算 W(t,m)，加入噪声，但保持单调递增
def W_with_noise(t, m, noise_factor=0.05):
    r = r_t_m(t, m)
    rho = rho_t_m(t, m)
    W_values = r * V_total * (rho_0 / rho) ** n
    noise = np.random.normal(0, noise_factor, size=t.shape)  # 生成噪声
    W_values += noise
    # 保证W(t,m)单调递增
    W_values = np.maximum.accumulate(W_values)
    return W_values

# 绘制不同材料下的 W(t,m)
plt.figure(figsize=(10, 6))

materials = {1: "Wood", 2: "Stone", 3: "Concrete"}

for m in m_values:
    W_values = W_with_noise(t_values, m)
    plt.plot(t_values, W_values, label=f"{materials[m]}")

plt.title(r"Wear Value $W(t, m)$ for Different Materials", fontsize=14)
plt.xlabel("Service Time (t)", fontsize=12)
plt.ylabel("Wear Value $W(t, m)$", fontsize=12)
plt.legend(title="Material", fontsize=12)

# 去掉网格
plt.grid(False)

plt.show()
