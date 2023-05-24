import pandas as pd
import numpy as np
from scipy import integrate, interpolate
import matplotlib.pyplot as plt
from Sterkteleerbeladen import Cw, n, F_c, P_punt, COB, G_punt, COV, F_tank, x_tank,V_tank



rho_staal = 7.85E3
E_staal=210E9
rho_water = 1.025E3
g = 9.81
tp_factor=1
df = pd.read_excel("IP.xlsx",'VB schip van Goris')
df = df.round(4)
nul = np.zeros(1)
Loa= df.iloc[0,1]
eind = np.array([Loa])
onderwater= df.iloc[42:64,0]
F_tank1=F_tank[0]/0.5*0.43


#som krachten
P_uitgebalanceerd = (G_punt[0] + F_tank1 +F_c)

#som momenten
LCG_c= -1*(P_punt[0]*COB +G_punt[0]*COV +F_tank1*x_tank)/F_c
displacement = df.iloc[18,1]
gewichtschip=displacement*rho_water





#GM berekenen

KB = df.iloc[20,3]
KG = df.iloc[21,3]

KG1=KG*gewichtschip+F_tank1
