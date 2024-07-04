

#################################################
##  CONVERSION FACTORS                         ##
#################################################
##  All conversion factors are taken from the  ##
##  sources cited in the English Wikipedia.    ##
#################################################
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
h_to_s      = 3600.0
s_to_h      = 1.0 / h_to_s


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
Experimental values of the partially-deuterated peaks\n
for the disrotatory mode of MAPbI3's methylammonium.\n
Measured at TOSCA, ISIS RAL, UK, May 2024.
'''

