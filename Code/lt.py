import numpy as np
import matplotlib.pyplot as plt

# Setting up the size of the noise map
width = 100  # Width of the staircase
height = 20  # Number of steps (height of the staircase)

# Noise parameters
scale = 10  # Noise scale
octaves = 6  # Layers of noise detail
persistence = 0.5  # Noise persistence
lacunarity = 2.0  # Noise lacunarity

# Generate a height map
height_map = np.zeros((height, width))

# Generate Perlin-like noise manually with numpy
def generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity):
    # Initialize the noise array
    noise_map = np.zeros((height, width))
    
    # Perlin-like noise generation using random function
    for y in range(height):
        for x in range(width):
            noise_map[y][x] = np.sin(x / scale) + np.cos(y / scale)
            
    return noise_map

# Apply the noise function to the height_map
height_map = generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity)

# Display the generated height map
plt.imshow(height_map, cmap='terrain', interpolation='lanczos')
plt.colorbar(label='Height')
plt.title('Staircase Height Map (Simulated Perlin Noise)')
plt.xlabel('Width of Staircase')
plt.ylabel('Step Number')
plt.show()
