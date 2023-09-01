import numpy as np
from clifford import Cl
import matplotlib.pyplot as plt

# Define a 1+1D spacetime
layout, blades = Cl(1, 1)  # 1 space and 1 time dimension
e1 = blades['e1']
e2 = blades['e2']
e12 = e1 ^ e2

# Parameters
c = 1  # Speed of light (normalized to 1 for simplicity)
q = 1  # Charge
v = 0.5  # Charge's velocity as a fraction of speed of light

# Rapidity
alpha = np.arctanh(v)

# Electric field in the rest frame of the charge (only in e1 direction for simplicity)
E_rest = q * e1

# Lorentz boost
B = np.cosh(alpha) + np.sinh(alpha) * e12

# Transform the electric field using the boost
E_moving = B * E_rest * ~B

# Extract components for visualization
E_rest_x = float(E_rest[e1])
E_moving_x = float(E_moving[e1])
E_moving_t = float(E_moving[e2])  # This component represents the temporal component due to the boost

# Visualization
plt.quiver(0, 0, E_rest_x, 0, angles='xy', scale_units='xy', scale=1, color='r', label='E (rest frame)')
plt.quiver(0, 0, E_moving_x, E_moving_t, angles='xy', scale_units='xy', scale=1, color='b', label='E (moving frame)')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='k')
plt.axvline(0, color='k')
plt.legend()
plt.title("Electric Field Transformation in 1+1D Spacetime")
plt.show()
