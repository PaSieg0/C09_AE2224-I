import numpy as np
import matplotlib.pyplot as plt
from isa_calc import isa
from aerocoeff import calculate_coeff

CRUISE_H = 22000 * 0.3048 #Convert form feet to meters
CRUISE_RHO = isa(CRUISE_H)[2]
CRUISE_V = 280 * 0.514444
CRUISE_P = isa(CRUISE_H)[1]

# Load data from the .txt file
data = np.loadtxt('./Dataset/SBW/CRUISE/Section1_hf.txt', skiprows=1, delimiter=' ')

# Extract x, y, and temperature values from the data
x = data[:, 0]
z = data[:, 1]
p = data[:, 2]

# Calculate pressure coefficient (Cp)
cp = calculate_coeff(p - CRUISE_P, CRUISE_RHO, CRUISE_V, 1)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D line
ax.plot(x, z, cp)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_zlabel('Cp')
ax.set_title('3D Line Plot of Cp')

# Show the plot
plt.show()

# Plot the 2D line
plt.plot(x, z)

# Set labels and title
plt.xlabel('X')
plt.ylabel('Z')
plt.title('2D Line Plot of X and Z')

# Show the plot
plt.show()