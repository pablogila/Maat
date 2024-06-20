

##############################
###### CONVERSION FACTORS ####
##############################
mev_to_cm = 8.0655
cm_to_mev = 1.0 / mev_to_cm
eV_to_J = 1.602176634e-19
J_to_eV = 1 / eV_to_J
angstrom_to_m = 1e-10
m_to_angstrom = 1 / angstrom_to_m
amu_to_kg = 1.66053906660e-27
kg_to_amu = 1 / amu_to_kg
eV_to_meV = 1000
meV_to_eV = 0.001


##############################
#### MATERIAL COMPOSITIONS ###
##############################
MAPI =      {'Pb': 1, 'I': 1, 'C': 1, 'N': 1, 'H': 6}
MAPI_CDND = {'Pb': 1, 'I': 1, 'C': 1, 'N': 1, 'D': 6}
MAPI_ND =   {'Pb': 1, 'I': 1, 'C': 1, 'N': 1, 'H': 3, 'D': 3}
MAPI_CD =   {'Pb': 1, 'I': 1, 'C': 1, 'N': 1, 'H': 3, 'D': 3}


##############################
##### EXPERIMENTAL VALUES ####
##############################
MAPI_peaks = {
    'h6d0' : [36.0, 39.0],
    'h5d1' : [33.0, 35.0],
    'h4d2' : [30.7, 33.0],
    'h3d3' : [28.8, 30.7],
}

