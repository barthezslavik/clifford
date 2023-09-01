from clifford.g3 import *  # Import 3D geometric algebra functions
import numpy as np

# Spin-1/2 particle properties
mu = 1.0  # Magnetic moment (arbitrary units)
B = e3  # Magnetic field along the z-axis

# Initial state of the spin particle (aligned with the x-axis)
psi = e1

# Time evolution
t_values = np.linspace(0, 10, 100)
spin_evolution = []

for t in t_values:
    # Compute the evolution operator
    U = np.exp(-0.5 * mu * B * t)
    
    # Apply the evolution operator to the initial state
    psi_t = U * psi * ~U
    spin_evolution.append([float(psi_t[e1]), float(psi_t[e2]), float(psi_t[e3])])

# Visualization
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

spin_evolution = np.array(spin_evolution)
ax.quiver(0, 0, 0, spin_evolution[:, 0], spin_evolution[:, 1], spin_evolution[:, 2], length=0.1, normalize=True, color='g', linewidth=2.5)

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_title("Evolution of Spin-1/2 Particle in Magnetic Field")
plt.show()