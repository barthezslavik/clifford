import numpy as np
from clifford.g3 import *  # Import 3D geometric algebra functions
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define normal vectors for the two planes
n1 = e1 + e2  # Example normal for the first plane
n2 = e1 - e2  # Example normal for the second plane

# Compute the bivector representing their line of intersection
B = n1 ^ n2

# Dualize the bivector to get the direction of the intersection line
direction = ~B * e3

# Extract coordinates for plotting
dir_coords = [float(direction[e1]), float(direction[e2]), float(direction[e3])]

# Compute a point on the line (intersecting the z=0 plane)
x0 = 0
y0 = 0  # For simplicity, we choose the origin
z0 = 0

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the planes
xx, yy = np.meshgrid(np.linspace(-1, 1, 50), np.linspace(-1, 1, 50))
zz1 = (-n1[0] * xx - n1[1] * yy) / n1[2]  # Using the plane equation to get z-coordinates
zz2 = (-n2[0] * xx - n2[1] * yy) / n2[2]
ax.plot_surface(xx, yy, zz1, alpha=0.5, color='r')
ax.plot_surface(xx, yy, zz2, alpha=0.5, color='b')

# Plot the intersection line
ax.quiver(x0, y0, z0, dir_coords[0], dir_coords[1], dir_coords[2], length=1, normalize=True, color='g', linewidth=2.5, label='Intersection Line')

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_title("Intersection of Two Planes")
ax.legend()
plt.show()