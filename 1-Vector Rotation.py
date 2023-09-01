import numpy as np
from clifford.g3 import *  # Import 3D geometric algebra functions
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a simple 3D vector (e.g., a point of an object)
v = e1 + e2 + e3
original_v = v  # Save the original vector for visualization

# Define a rotation bivector for a small rotation around the e3 (z) axis
small_angle = np.pi / 180  # 1 degree
B_small = small_angle * e12

# Rotor for 1 degree rotation around e3
R_small = np.e**(-B_small / 2)

trajectory_coords = []

# Iteratively rotate the vector 45 times by 1 degree to get 45 degrees rotation
for i in range(45):
    v = R_small * v * ~R_small
    trajectory_coords.append([float(v[e1]), float(v[e2]), float(v[e3])])

# Extract coordinates for plotting
original_coords = [float(original_v[e1]), float(original_v[e2]), float(original_v[e3])]
final_coords = trajectory_coords[-1]

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Use quiver to plot vectors as arrows
# Original vector before any rotation
ax.quiver(0, 0, 0, original_coords[0], original_coords[1], original_coords[2], color='b', label='Original Vector', arrow_length_ratio=0.1)
# Rotated vector after full rotation
ax.quiver(0, 0, 0, final_coords[0], final_coords[1], final_coords[2], color='r', label='Rotated Vector', arrow_length_ratio=0.1)

trajectory_coords = np.array(trajectory_coords)
ax.plot(trajectory_coords[:, 0], trajectory_coords[:, 1], trajectory_coords[:, 2], color='g', linestyle=':', label='Trajectory')
ax.plot([0, 0], [0, 0], [-1.5, 1.5], color='k', linestyle='--', label='Rotation Axis (e3)')

ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.legend()
plt.show()