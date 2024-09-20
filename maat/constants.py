import numpy as np

'''
This module contains constants and conversion factors.
'''

#############################
##   CONVERSION FACTORS    ##
#############################
## Energy
eV_to_meV   = 1000.0
meV_to_eV   = 0.001
meV_to_cm   = 8.0655
cm_to_meV   = 1.0 / meV_to_cm
eV_to_J     = 1.602176634e-19
J_to_eV     = 1.0 / eV_to_J
Ry_to_eV    = 13.605693122990
eV_to_Ry    = 1.0 / Ry_to_eV
Ry_to_J     = 2.1798723611030e-18
J_to_Ry     = 1.0 / Ry_to_J
cal_to_J    = 4.184
J_to_cal    = 1 / cal_to_J
kcal_to_J   = cal_to_J * 1000.0
J_to_kcal   = 1 / kcal_to_J
## Distance
A_to_m      = 1.0e-10
m_to_A      = 1.0 / A_to_m
bohr_to_m   = 5.29177210544e-11
m_to_bohr   = 1.0 / bohr_to_m
A_to_bohr   = A_to_m * m_to_bohr
bohr_to_A   = 1.0 / A_to_bohr
## Mass
amu_to_kg   = 1.66053906660e-27
kg_to_amu   = 1.0 / amu_to_kg
# Pressure
GPa_to_Pa   = 1.0e9
Pa_to_GPa   = 1.0 / GPa_to_Pa
kbar_to_bar = 1000.0
bar_to_kbar = 1.0 / kbar_to_bar
Pa_to_bar   = 1.0e-5
bar_to_Pa   = 1.0 / Pa_to_bar
GPa_to_kbar = GPa_to_Pa * Pa_to_bar * bar_to_kbar
kbar_to_GPa = 1.0 / GPa_to_kbar
## Time
H_to_s      = 3600.0
s_to_H      = 1.0 / H_to_s


#############################
##   UNIVERSAL CONSTANTS   ##
#############################
# Given in SI units unless stated otherwise
h = 6.62607015e-34      # J s
h_eV = h * J_to_eV
hbar = h / (2 * np.pi)  # J s
hbar_eV = h_eV / (2 * np.pi)


#############################
##      ATOMIC MASSES      ##
#############################
m_H = 1.00784   # H amu (atomic mass units)
m_H_kg = m_H_amu * amu_to_kg
m_D = 2.014102  # D amu
m_D_kg = m_D_amu * amu_to_kg
m_C = 12.0107  # C amu
m_C_kg = m_C * amu_to_kg
m_N = 14.0067  # N amu
m_N_kg = m_N * amu_to_kg
m_I = 126.90447  # I amu
m_I_kg = m_I * amu_to_kg
m_Pb = 207.2  # Pb amu
m_Pb_kg = m_Pb * amu_to_kg


#############################
##  MATERIAL COMPOSITIONS  ##
#############################
MAPI_atoms =      {'Pb': 1, 'I': 1, 'C': 1, 'N': 1, 'H': 6}
MAPI_CDND_atoms = {'Pb': 1, 'I': 1, 'C': 1, 'N': 1, 'D': 6}
MAPI_ND_atoms =   {'Pb': 1, 'I': 1, 'C': 1, 'N': 1, 'H': 3, 'D': 3}
MAPI_CD_atoms =   {'Pb': 1, 'I': 1, 'C': 1, 'N': 1, 'H': 3, 'D': 3}


###########################
##  EXPERIMENTAL VALUES  ##
###########################
MAPI_peaks = {
    'h6d0' : [36.0, 39.0],
    'h5d1' : [33.0, 35.0],
    'h4d2' : [30.7, 33.0],
    'h3d3' : [28.8, 30.7],
}
'''
Experimental values of the partially-deuterated amine peaks\n
for the disrotatory mode of MAPbI3's methylammonium.\n
Measured at TOSCA, ISIS RAL, UK, May 2024.
'''

