import numpy as np
import matplotlib.pyplot as plt

# Define parameters
r = 1.0  # Proportionality coefficient (assumed)
V_total = 1.0  # Total volume (assumed)
rho_0 = 1.0  # Reference resistivity (assumed)
n_values = [1, 2, 3]  # Different values of n to compare
rho_values = np.linspace(0.1, 5.0, 100)  # Range of rho values (10% to 500% of rho_0)

# Create figure
plt.figure(figsize=(10, 7))

# Use different line styles and colors for each n value
line_styles = ['-', '-', '-']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Calculate W for different n values and plot
for i, n in enumerate(n_values):
    W_values = r * V_total * (rho_0 / rho_values) ** (1/n)
    plt.plot(rho_values / rho_0, W_values, label=f'n={n}', linestyle=line_styles[i], color=colors[i], linewidth=2)

# Add labels and title with a more modern font
plt.xlabel('Resistivity ratio ρ/ρ0', fontsize=14, fontweight='bold', family='serif')
plt.ylabel('Wear value W', fontsize=14, fontweight='bold', family='serif')
plt.title('Sensitivity of Wear Value (W) to Resistivity Ratio (ρ/ρ0)', fontsize=16, fontweight='bold', family='serif')

# Add grid with customized style
plt.grid(True, linestyle=':', color='gray', alpha=0.7)

# Add legend with better positioning
plt.legend(loc='upper right', fontsize=12, frameon=False)

# Show the plot
plt.tight_layout()
plt.show()
