import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from isa_calc import isa

def aircraft2global(force_vector, aoa):
    """Changes coordinate system form aircraft reference frame to global reference frame,
     z perpendicular to earth surface
    
    Args:
        force_vector (np.array): in aircraft frame (x, y, z) y usually = 0
        aoa (float): current angle of attack in radians

    Returns:
        resultant_force_vector (np.array): in global frame (x, y, z) y usually = 0 
    """
    rotation_matrix = np.array([[np.cos(-aoa) , 0, np.sin(-aoa)], 
                                [    0       , 1,     0      ],
                                [-np.sin(-aoa), 0, np.cos(-aoa)],])
    
    resultant_force_vector = np.matmul(rotation_matrix, force_vector)

    return resultant_force_vector

def global2aircraft(force_vector, aoa):
    """Changes coordinate system form global reference frame (z perpendicular to earth surface)
      to aircraft reference frame
    
    Args:
        force_vector (np.array): in global frame (x, y, z) y usually = 0
        aoa (float): current angle of attack in radians

    Returns:
        resultant_force_vector (np.array): in aircraft frame (x, y, z) y usually = 0 
    """
    rotation_matrix = np.array([[np.cos(aoa) , 0, np.sin(aoa)], 
                                [    0       , 1,     0      ],
                                [-np.sin(aoa), 0, np.cos(aoa)],])
    
    resultant_force_vector = np.matmul(rotation_matrix, force_vector)

    return resultant_force_vector

def calculate_coeff(force, density, airspeed, wingarea):
    """Self explicative

    """
    return 2*force/(wingarea*density*airspeed**2)

def extract_and_coefficients(path, velocity, density, area, chord):
    # moment coefficient still to be implemented
    """Extracts for .txt and calculates coefficients
    Args:
        path (string): path to .txt file
        velocity (float): velocity at desired condition
        density (float): density at desired conditon
        area (float): reference wing area
    
    Returns:
        o_aoa (np.array): ordered list of angles of attack
        o_cl (np.array): ordered list of lift coefficients
        o_cd (np.array): ordered list of drag coefficients
        o_cm (np.array): ordered list of moment coefficients
    """
    aoas = []
    liftcoeffs = []
    dragcoeffs = []
    momentcoeffs = []

    df = pd.read_csv(path, sep='\s+')
    for i in range(df.shape[0]):
        global_forces = aircraft2global(np.array([-df.loc[i, 'Fx'], 0, df.loc[i, 'Fz']]), df.loc[i, 'AoA']*np.pi/180)
        cl = calculate_coeff(global_forces[2], density, velocity, area)
        cd = calculate_coeff(-global_forces[0], density, velocity, area)
        cm = calculate_coeff(df.loc[i, 'My'], density, velocity, area*chord)

        aoas = np.append(aoas, df.loc[i, 'AoA'])
        liftcoeffs = np.append(liftcoeffs, cl)
        dragcoeffs = np.append(dragcoeffs, cd)
        momentcoeffs = np.append(momentcoeffs, cm)

    order = np.argsort(aoas)
    o_aoa = aoas[order]
    o_cl = liftcoeffs[order]
    o_cd = dragcoeffs[order]
    o_cm = momentcoeffs[order]
    
    return o_aoa, o_cl, o_cd, o_cm

if __name__ == "__main__":
    RHO0 = 1.225
    WING_AREA = 73
    CHORD = 1.8

    CRUISE_H = 22000 * 0.3048 #Convert form feet to meters
    CRUISE_RHO = isa(CRUISE_H)[2]
    CRUISE_V = 280 * 0.514444

    CLIMB_H = 12000 * 0.3048 #Convert form feet to meters
    CLIMB_RHO = isa(CLIMB_H)[2]
    CLIMB_V = 150 * 0.514444 * np.sqrt(RHO0/CLIMB_RHO) # https://aerotoolbox.com/airspeed-conversions/ use CAS as EAS below 200kts no difference

    data2plot = [None, None, None, None]
    #-----------------CRUISE SBW----------------------
    data2plot[0] = extract_and_coefficients(r"./Dataset/SBW/CRUISE/Global_forces.txt", CRUISE_V, CRUISE_RHO, WING_AREA, CHORD)

    #-----------------CLIMB SBW----------------------
    data2plot[1] = extract_and_coefficients(r"./Dataset/SBW/CLIMB/Global_forces.txt", CLIMB_V, CLIMB_RHO, WING_AREA, CHORD)

    #-----------------CRUISE CNT----------------------
    data2plot[2] = extract_and_coefficients(r"./Dataset/CNT/CRUISE/Global_forces.txt", CRUISE_V, CRUISE_RHO, WING_AREA, CHORD)

    #-----------------CLIMB CNT----------------------
    data2plot[3] = extract_and_coefficients(r"./Dataset/CNT/CLIMB/Global_forces.txt", CLIMB_V, CLIMB_RHO, WING_AREA, CHORD)



    for i in range(4):
        plt.plot(data2plot[i][0], data2plot[i][1], label=f"{i}", marker='.') # Cl-alpha
    
    plt.legend()
    plt.title("CL-alpha")
    plt.savefig('./Plots/Cl-alpha.png')
    plt.clf()

    for i in range(4):
        plt.plot(data2plot[i][0], data2plot[i][2], label=f"{i}", marker='.') # CD-alpha
    
    plt.legend()
    plt.title("CD-alpha")
    plt.savefig('./Plots/Cd-alpha.png')
    plt.clf()

    for i in range(4):
        plt.plot(data2plot[i][2], data2plot[i][1], label=f"{i}", marker='.') # Drag Polars

    plt.legend()
    plt.title("Drag Polars")
    plt.savefig('./Plots/Cl-Cd.png')
    plt.clf()

    for i in range(4):
        plt.plot(data2plot[i][0], data2plot[i][1]/data2plot[i][2], label=f"{i}", marker='.') # CM-alpha

    plt.legend()
    plt.title("CL/CD-alpha")
    plt.savefig('./Plots/ClCd-alpha.png')
    plt.clf()

    for i in range(4):
        plt.plot(data2plot[i][0], data2plot[i][3], label=f"{i}", marker='.') # CM-alpha

    plt.legend()
    plt.title("CM-alpha")
    plt.savefig('./Plots/Cm-alpha.png')
    plt.clf()
