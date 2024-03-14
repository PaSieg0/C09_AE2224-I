import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from isa_calc import isa

df_CNT = pd.read_csv(r"./Dataset/CNT/CRUISE/Surface_loadings.txt", sep='\s+') # Load the data CNT
df_SBW = pd.read_csv(r"./Dataset/SBW/CRUISE/Surface_loadings.txt", sep='\s+') # Load the data SBW
df_low_fidelity_wing = pd.read_csv(r"./Dataset/low_fidelity/CRUISE/Wing_surface_laodings.dat", sep='\s+') # Load the data low fidelity wing
df_low_fidelity_strut = pd.read_csv(r"./Dataset/low_fidelity/CRUISE/Strut_surface_laodings.dat", sep='\s+') # Load the data low fidelity strut

plt.plot(df_CNT.iloc[:, 0], df_CNT.iloc[:, 2], label='CNT')
plt.plot(df_SBW.iloc[:, 0], df_SBW.iloc[:, 1], label='SBW')
plt.plot(df_low_fidelity_wing.iloc[:, 0], df_low_fidelity_wing.iloc[:, 2], label='Low fidelity wing')
plt.plot(df_low_fidelity_strut.iloc[:, 0], df_low_fidelity_strut.iloc[:, 2], label='Low fidelity strut')
plt.xlabel('y')
plt.ylabel('Cl')
plt.title('Cl-y')
plt.legend()
plt.savefig('./Plots/Cl-y.pdf')
plt.clf()

plt.plot(df_CNT.iloc[:, 0], df_CNT.iloc[:, 3], label='CNT')
plt.plot(df_SBW.iloc[:, 0], df_SBW.iloc[:, 2], label='SBW')
plt.plot(df_low_fidelity_wing.iloc[:, 0], df_low_fidelity_wing.iloc[:, 3], label='Low fidelity wing')
plt.plot(df_low_fidelity_strut.iloc[:, 0], df_low_fidelity_strut.iloc[:, 3], label='Low fidelity strut')
plt.xlabel('y')
plt.ylabel('Cd')
plt.title('Cd-y')
plt.legend()
plt.savefig('./Plots/Cd-y.pdf')
plt.clf()

plt.plot(df_CNT.iloc[:, 0], df_CNT.iloc[:, 2]/df_CNT.iloc[:, 3], label='CNT')
plt.plot(df_SBW.iloc[:, 0], df_SBW.iloc[:, 1]/df_SBW.iloc[:, 2], label='SBW')
plt.plot(df_low_fidelity_wing.iloc[:, 0], df_low_fidelity_wing.iloc[:, 2]/df_low_fidelity_wing.iloc[:, 3], label='Low fidelity wing')
plt.plot(df_low_fidelity_strut.iloc[:, 0], df_low_fidelity_strut.iloc[:, 2]/df_low_fidelity_strut.iloc[:, 3], label='Low fidelity strut')
plt.xlabel('y')
plt.ylabel('Cl/Cd')
plt.title('ClCd-y')
plt.legend()
plt.savefig('./Plots/ClCd-y.pdf')
plt.clf()

plt.plot(df_CNT.iloc[:, 0], df_CNT.iloc[:, 1], label='CNT')
plt.plot(df_SBW.iloc[:, 0], df_SBW.iloc[:, 3]/df_SBW.iloc[:, 1], label='SBW')
plt.plot(df_low_fidelity_wing.iloc[:, 0], df_low_fidelity_wing.iloc[:, 1], label='Low fidelity wing')
plt.plot(df_low_fidelity_strut.iloc[:, 0], df_low_fidelity_strut.iloc[:, 1], label='Low fidelity strut')
plt.xlabel('y')
plt.ylabel('chord')
plt.title('chord-y')
plt.legend()
plt.savefig('./Plots/c-y.pdf')
plt.clf()
