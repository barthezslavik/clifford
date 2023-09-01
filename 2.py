import numpy as np
from clifford.g3 import *  # Import 3D geometric algebra functions
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the incoming ray's direction (let's assume it's coming in at a 45-degree angle to the XY plane from the positive X direction)
incoming_ray = e1 + e3

# Normalize the incoming ray for clarity in visualization
incoming_ray = incoming_ray.normal()

# Define the mirror's normal vector (mirror is in the XY plane, so the normal is along the Z axis)
mirror_normal = e3

# Reflect the incoming ray using the geometric algebra formula
reflected_ray = -incoming_ray + 2*(mirror_normal|incoming_ray)*mirror_normal

# Extract coordinates for plotting
incoming_coords = [float(incoming_ray[e1]), float(incoming_ray[e2]), float(incoming_ray[e3])]
reflected_coords = [float(reflected_ray[e1]), float(reflected_ray[e2]), float(reflected_ray[e3])]

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Use quiver to plot vectors as arrows
ax.quiver(0, 0, 0, incoming_coords[0], incoming_coords[1], incoming_coords[2], color='b', length=1, label='Incoming Ray', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, reflected_coords[0], reflected_coords[1], reflected_coords[2], color='r', length=1, label='Reflected Ray', arrow_length_ratio=0.1)

# Adding the mirror surface as a plane
xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 50), np.linspace(-1.5, 1.5, 50))
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, color='c', alpha=0.5)

ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_title("Mirror Surface represented by cyan plane")
ax.legend()
plt.show()
