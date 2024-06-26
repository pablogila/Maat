

#################################################
##  CONVERSION FACTORS                         ##
#################################################
##  All conversion factors are taken from the  ##
##  sources cited in the English Wikipedia.    ##
#################################################
## Energy
eV_to_meV = 1000
meV_to_eV = 0.001
mev_to_cm = 8.0655
cm_to_mev = 1.0 / mev_to_cm
eV_to_J = 1.602176634e-19
J_to_eV = 1 / eV_to_J
ryd_to_eV = 13.605693122990
eV_to_ryd = 1 / rydberg_to_eV
ryd_to_J = 2.1798723611030e-18
J_to_ryd = 1 / rydberg_to_J
## Distance
angstrom_to_m = 1e-10
m_to_A = 1 / angstrom_to_m
bohr_to_m = 5.29177210544e-11
m_to_bohr = 1 / bohr_to_m
A_to_bohr = angstrom_to_m * m_to_bohr
bohr_to_A = 1 / angstrom_to_bohr
## Mass
amu_to_kg = 1.66053906660e-27
kg_to_amu = 1 / amu_to_kg


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

