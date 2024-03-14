import numpy as np
import matplotlib.pyplot as plt
from isa_calc import isa
from aerocoeff import calculate_coeff

def split_data(data, split_value, split_column):
    return data[data[:, split_column] > split_value], data[data[:, split_column] < split_value]

def extract_columns(data):
    return data[:, 0], data[:, 1], data[:, 2]

CRUISE_H = 22000 * 0.3048 #Convert form feet to meters
CRUISE_RHO = isa(CRUISE_H)[2]
CRUISE_V = 280 * 0.514444
CRUISE_P = isa(CRUISE_H)[1]

# Load data from the .txt file
data_1 = np.loadtxt('./Dataset/SBW/CRUISE/Section1_hf.txt', skiprows=1, delimiter=' ')
data_2 = np.loadtxt('./Dataset/SBW/CRUISE/Section2_hf.txt', skiprows=1, delimiter=' ')
data_3 = np.loadtxt('./Dataset/SBW/CRUISE/Section3_hf.txt', skiprows=1, delimiter=' ')

# Split the data into wing_cp and strut_cp
#dont split last section because only has wing no strut
wing_cp_1 , strut_cp_1 = split_data(data_1, split_value=-1.5, split_column=1)
wing_cp_2 , strut_cp_2 = split_data(data_2, split_value=-1.5, split_column=1)


# Extract x, z, and p values from the data
x_wing_1, z_wing_1, p_wing_1 = extract_columns(wing_cp_1)
x_strut_1, z_strut_1, p_strut_1 = extract_columns(strut_cp_1)

x_wing_2, z_wing_2, p_wing_2 = extract_columns(wing_cp_2)
x_strut_2, z_strut_2, p_strut_2 = extract_columns(strut_cp_2)

x_wing_3, z_wing_3, p_wing_3 = extract_columns(data_3)

# Calculate pressure coefficient (Cp)
cp_1 = calculate_coeff(p_wing_1 - CRUISE_P, CRUISE_RHO, CRUISE_V, 1)
cp_2 = calculate_coeff(p_wing_2 - CRUISE_P, CRUISE_RHO, CRUISE_V, 1)
cp_3 = calculate_coeff(p_wing_3 - CRUISE_P, CRUISE_RHO, CRUISE_V, 1)

#---------------------------Plotting-------------------------------#
x_list = [x_wing_1, x_wing_2, x_wing_3]
z_list = [z_wing_1, z_wing_2, z_wing_3]
cp_list = [cp_1, cp_2, cp_3]

# Create a 3D plot
fig = plt.figure()

for i in range(3):
    ax = fig.add_subplot(1, 3, i+1, projection='3d')
    # Plot the 3D line
    ax.plot(x_list[i], z_list[i], cp_list[i])

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    ax.set_zlabel('Cp')
    ax.set_title(f'3D Line Plot of Cp (Case {i+1})')

# Adjust spacing between subplots
plt.tight_layout()
# Show the plot
plt.show()


# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 7))

for i in range(3):
    axs[i].plot(x_list[0], cp_list[0])
    axs[i].set_xlabel('X')
    axs[i].set_ylabel('Cp')
    axs[i].set_title(f'2D Line Plot of X and Cp (Case {i+1})')
    

# Adjust spacing between subplots
plt.tight_layout()
# Show the plot
plt.show()