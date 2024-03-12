import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from isa_calc import isa

df_CNT = pd.read_csv(r"./Dataset/CNT/CRUISE/Surface_loadings.txt", sep='\s+') # Load the data CNT
df_SBW = pd.read_csv(r"./Dataset/SBW/CRUISE/Surface_loadings.txt", sep='\s+') # Load the data SBW

plt.plot(df_CNT.iloc[:, 0], df_CNT.iloc[:, 2], label='CNT')
plt.plot(df_SBW.iloc[:, 0], df_SBW.iloc[:, 1], label='SBW')
plt.xlabel('y')
plt.ylabel('Cl')
plt.title('Cl-y')
plt.legend()
plt.savefig('./Plots/Cl-y.pdf')
plt.clf()

plt.plot(df_CNT.iloc[:, 0], df_CNT.iloc[:, 3], label='CNT')
plt.plot(df_SBW.iloc[:, 0], df_SBW.iloc[:, 2], label='SBW')
plt.xlabel('y')
plt.ylabel('Cd')
plt.title('Cd-y')
plt.legend()
plt.savefig('./Plots/Cd-y.pdf')
plt.clf()

plt.plot(df_CNT.iloc[:, 0], df_CNT.iloc[:, 2]/df_CNT.iloc[:, 3], label='CNT')
plt.plot(df_SBW.iloc[:, 0], df_SBW.iloc[:, 1]/df_SBW.iloc[:, 2], label='SBW')
plt.xlabel('y')
plt.ylabel('Cl/Cd')
plt.title('ClCd-y')
plt.legend()
plt.savefig('./Plots/ClCd-y.pdf')
plt.clf()

plt.plot(df_CNT.iloc[:, 0], df_CNT.iloc[:, 1], label='CNT')
plt.plot(df_SBW.iloc[:, 0], df_SBW.iloc[:, 3]/df_SBW.iloc[:, 1], label='SBW')
plt.xlabel('y')
plt.ylabel('chord')
plt.title('chord-y')
plt.legend()
plt.savefig('./Plots/c-y.pdf')
plt.clf()
