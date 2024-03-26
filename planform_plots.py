import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Varibale inputs
CNT_HalfChordSweep = 0 #degrees
SBW_HalfChordSweep = 0
Strut_HalfChordSweep = 0

#Data inputs
CNT_coords = pd.read_csv(r"./Dataset/CNT/CRUISE/Surface_loadings.txt", sep='\s+').drop(columns=["Cl", "Cd", "cCl", "cCd"])
SBW_coords = pd.read_csv(r"./Dataset/SBW/CRUISE/Wing_surface_loadings.txt", sep='\s+').drop(columns=["Cl", "cCl"])
Strut_coords = pd.read_csv(r"./Dataset/SBW/CRUISE/Strut_Surface_loadings.txt", sep='\s+').drop(columns=["Cl", "cCl"])


#Define wing geometry with open root for calculation of area and AR
CNT_y = (pd.concat([CNT_coords['y'], CNT_coords['y'].iloc[::-1]], ignore_index=True)).to_numpy()
Unswept_CNT_chords = (pd.concat([(0.5*CNT_coords['c']), ((-0.5) * CNT_coords['c'].iloc[::-1])], ignore_index=True)).to_numpy()
CNT_chords = Unswept_CNT_chords - (CNT_y * np.sin((np.pi * CNT_HalfChordSweep)/180.))

SBW_y = (pd.concat([SBW_coords['y'], SBW_coords['y'].iloc[::-1]], ignore_index=True)).to_numpy()
Unswept_SBW_chords = (pd.concat([(0.5*(SBW_coords['cCd'] / SBW_coords['Cd'])), ((-0.5) * (SBW_coords['cCd'] / SBW_coords['Cd']).iloc[::-1])], ignore_index=True)).to_numpy()
SBW_chords = Unswept_SBW_chords - (SBW_y * np.sin((np.pi * SBW_HalfChordSweep)/180.))

Strut_y = (pd.concat([Strut_coords['y'], Strut_coords['y'].iloc[::-1]], ignore_index=True)).to_numpy()
Unswept_Strut_chords = (pd.concat([(0.5*(Strut_coords['cCd'] / Strut_coords['Cd'])), ((-0.5) * (Strut_coords['cCd'] / Strut_coords['Cd']).iloc[::-1])], ignore_index=True)).to_numpy()
Strut_chords = Unswept_Strut_chords - (Strut_y * np.sin((np.pi * Strut_HalfChordSweep)/180.))

#Calculations of area and AR
CNT_area = 2*np.trapz(CNT_chords, CNT_y)
SBW_area = 2*np.trapz(SBW_chords, SBW_y)
Strut_area = 2*np.trapz(Strut_chords, Strut_y)

print()
print(f'Cantilever area: ' + str(CNT_area) + ' [m^2]')
print(f'SBW area: ' + str(SBW_area) + ' [m^2]')
print(f'Strut area: ' + str(Strut_area) + ' [m^2]')
print()
print(f'Cantilever aspect ratio: ' + str(((2*np.max(CNT_y))**2)/CNT_area))
print(f'SBW aspect ratio: ' + str(((2*np.max(SBW_y))**2)/SBW_area))
print(f'Strut aspect ratio: ' + str(((2*np.max(Strut_y))**2)/Strut_area))

#Closing wing geometry at root for graphing
CNT_y = np.append(CNT_y, [0])
CNT_chords = np.append(CNT_chords, [0.5 * CNT_coords['c'].iloc[0]])

SBW_y = np.append(SBW_y, [0])
SBW_chords = np.append(SBW_chords, [0.5 * (SBW_coords['cCd'] / SBW_coords['Cd']).iloc[0]])

Strut_y = np.append(Strut_y, [0])
Strut_chords = np.append(Strut_chords, [0.5 * (Strut_coords['cCd'] / Strut_coords['Cd']).iloc[0]])

#Graphing wing geometries
plt.figure(figsize=(15, 5))

#Comparison plot of CNT and SBW
plt.plot(CNT_y, CNT_chords, label = 'Cantilever wing')
plt.plot(SBW_y, SBW_chords, label = 'SBW main wing')
plt.xlim(-0.25, 17.75)
plt.ylim(-3, 3)
plt.xlabel("Span position [m]", fontsize = 15)
plt.ylabel("Chord [m]", fontsize = 15)
#plt.axis('equal')
plt.legend(fontsize = 15)
plt.grid(True)
plt.tight_layout()
plt.savefig('./Plots/WingGeometry/CNT_SBW_Planforms.pdf')
plt.clf()

#CNT planform plot
plt.plot(CNT_y, CNT_chords)
plt.xlabel("Span position [m]", fontsize = 15)
plt.ylabel("Chord [m]", fontsize = 15)
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.savefig('./Plots/WingGeometry/CNT_Planform.pdf')
plt.clf()

#SBW planform plot
plt.plot(SBW_y, SBW_chords)
plt.xlabel("Span position [m]", fontsize = 15)
plt.ylabel("Chord [m]", fontsize = 15)
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.savefig('./Plots/WingGeometry/SBW_Planform.pdf')
plt.clf()

#Strut planform plot
plt.plot(Strut_y, Strut_chords)
plt.xlabel("Span position [m]", fontsize = 15)
plt.ylabel("Chord [m]", fontsize = 15)
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.savefig('./Plots/WingGeometry/Strut_Planform.pdf')
