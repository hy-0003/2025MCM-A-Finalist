import numpy as np
import matplotlib.pyplot as plt

# 假设的参数
d_values = np.linspace(0, 20, 100)  # 深度 d 从 0 到 20
m_values = np.array([1, 2, 3])  # 不同材料的索引 m

# 设定常数
rho_0 = 100  # 假设的参考电阻率 ρ0
V_total = 10  # 假设的总体积
n = 1.5  # 假设的指数 n

# 分段函数
def r_d_m(d, m):
    r_values = np.zeros_like(d)  # 创建与 d 相同大小的数组
    for i in range(len(d)):
        if d[i] < 5:
            r_values[i] = 0.1 * m * np.exp(0.05 * d[i])  # 第一段：逐渐递增
        elif d[i] < 10:
            r_values[i] = 0.2 * m * np.exp(0.05 * d[i])  # 第二段：更快递增
        else:
            r_values[i] = 0.3 * m * np.exp(0.05 * d[i])  # 第三段：加速递增
    return r_values

def rho_d_m(d, m):
    rho_values = np.zeros_like(d)  # 创建与 d 相同大小的数组
    for i in range(len(d)):
        if d[i] < 5:
            rho_values[i] = rho_0 * (1 + 0.05 * m) * np.exp(0.02 * d[i])  # 第一段：电阻率较低
        elif d[i] < 10:
            rho_values[i] = rho_0 * (1 + 0.05 * m) * np.exp(0.03 * d[i])  # 第二段：电阻率稍微增大
        else:
            rho_values[i] = rho_0 * (1 + 0.05 * m) * np.exp(0.04 * d[i])  # 第三段：电阻率大幅增大
    return rho_values

# 计算 W(d,m)
def W_with_segments(d, m):
    r = r_d_m(d, m)
    rho = rho_d_m(d, m)
    return r * V_total * (rho_0 / rho) ** n

# 绘制不同材料下的 W(d,m)
plt.figure(figsize=(10, 6))

materials = {1: "Wood", 2: "Stone", 3: "Concrete"}

for m in m_values:
    W_values = W_with_segments(d_values, m)
    plt.plot(d_values, W_values, label=f"{materials[m]}")

plt.title(r"Wear Value $W(d, m)$ for Different Materials with Stepwise Behavior", fontsize=14)
plt.xlabel("Depth (d)", fontsize=12)
plt.ylabel("Wear Value $W(d, m)$", fontsize=12)
plt.legend(title="Material", fontsize=12)

# 去掉网格
plt.grid(False)

plt.show()

