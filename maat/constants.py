import numpy as np

'''
This module contains constants and conversion factors.
'''


#############################
##     MATERIAL CLASS      ##
#############################
# To play around with the composition of materials.
# Defined here, to set some default values.
class Material:
    def __init__(self,
                 atoms:dict,
                 name:str=None,
                 grams:float=None,
                 grams_error:float=None,
                 mols:float=None,
                 mols_error:float=None,
                 molar_mass:float=None,
                 cross_section:float=None,
                 ):
        self.atoms = atoms
        '''Dict of atoms in the material'''
        self.name = name
        self.grams = grams
        '''mass in grams'''
        self.grams_error = grams_error
        '''error of the measured mass in grams'''
        self.mols = mols
        '''number of moles'''
        self.mols_error = mols_error
        '''error of the number of moles'''
        self.molar_mass = molar_mass
        self.cross_section = cross_section

    def set_grams_error(self):
        if self.grams is None:
            return
        decimal_accuracy = len(str(self.grams).split('.')[1])
        # Calculate the error in grams
        self.grams_error = 10**(-decimal_accuracy)

    def set_mass(self):
        '''Set the molar mass of the material.\n
        If `self.grams` is not `None`, the number of moles will be calculated and overwritten.'''
        material_grams_per_mol = 0.0
        for key in self.atoms:
            material_grams_per_mol += self.atoms[key] * mass[key]
        self.molar_mass = material_grams_per_mol
        if self.grams is not None:
            self.set_grams_error()
            self.mols = self.grams / material_grams_per_mol
            self.mols_error = self.mols * np.sqrt((self.grams_error / self.grams)**2)
    
    def set_cross_section(self):
        total_cross_section = 0.0
        for key in self.atoms:
            total_cross_section += self.atoms[key] * cross_section[key]
        self.cross_section = total_cross_section

    def set(self):
        self.set_mass()
        self.set_cross_section()

    def print(self):
        print('\nMATERIAL')
        if self.name is not None:
            print(f'Name: {self.name}')
        if self.grams is not None and self.grams_error is not None:
            print(f'Grams: {self.grams} +- {self.grams_error} g')
        elif self.grams is not None:
            print(f'Grams: {self.grams} g')
        if self.mols is not None and self.mols_error is not None:
            print(f'Moles: {self.mols} +- {self.mols_error} mol')
        elif self.mols is not None:
            print(f'Moles: {self.mols} mol')
        if self.molar_mass is not None:
            print(f'Molar mass: {self.molar_mass} g/mol')
        if self.cross_section is not None:
            print(f'Cross section: {self.cross_section} barns')
        if self.atoms is not None:
            print(f'Atoms: {self.atoms}')
        print('')


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
# Expressed in atomic mass units (amu) by default
mass = {
    'H' : 1.00784,
    'D' : 2.014102,
    'C' : 12.0107,
    'N' : 14.0067,
    'I' : 126.90447,
    'Pb': 207.2,
}

mass_kg = {}
for key in mass:
    mass_kg[key] = mass[key] * amu_to_kg


#############################################
##  TOTAL BOUND SCATTERING CROSS SECTIONS  ##
#############################################
# From Felix Fernandez-Alonso 2013 book
# Expressed in barns (1 b = 100 fm^2)
cross_section = {
    'H' : 81.67,
    'D' : 7.64,
    'C' : 5.551,
    'N' : 11.51,
    'I' : 3.81,
    'Pb': 11.118,
}


#############################
##   USER INPUT STRINGS    ##
#############################
# Used to correct and normalise user inputs
unit_keys = {
    'mol'  : ['mol', 'mols', 'mole', 'moles', 'Mol', 'Mols', 'Mole', 'Moles', 'MOL', 'MOLS', 'MOLE', 'MOLES'],
    'g'    : ['g', 'gram', 'grams', 'G', 'Gram', 'Grams', 'GRAM', 'GRAMS'],
    'kg'   : ['kg', 'Kg', 'KG', 'kilogram', 'kilograms', 'Kilogram', 'Kilograms', 'KILOGRAM', 'KILOGRAMS'],
    'amu'  : ['amu', 'AMU', 'Amu', 'atomicmassunit', 'atomicmassunits', 'Atomicmassunit', 'Atomicmassunits', 'ATOMICMASSUNIT', 'ATOMICMASSUNITS'],
    'eV'   : ['eV', 'ev', 'EV', 'electronvolt', 'electronvolts', 'Electronvolt', 'Electronvolts', 'ELECTRONVOLT', 'ELECTRONVOLTS'],
    'meV'  : ['meV', 'mev', 'MEV', 'millielectronvolt', 'millielectronvolts', 'Millielectronvolt', 'Millielectronvolts', 'MILLIELECTRONVOLT', 'MILLIELECTRONVOLTS'],
    'J'    : ['J', 'j', 'JOULE', 'JOULES', 'joule', 'joules', 'Joule', 'Joules'],
    'cal'  : ['cal', 'Cal', 'CAL', 'calorie', 'calories', 'Calorie', 'Calories', 'CALORIE', 'CALORIES'],
    'kcal' : ['kcal', 'Kcal', 'KCAL', 'kilocalorie', 'kilocalories', 'Kilocalorie', 'Kilocalories', 'KILOCALORIE', 'KILOCALORIES'],
    'Ry'   : ['Ry', 'ry', 'RY', 'rydberg', 'rydbergs', 'Rydberg', 'Rydbergs', 'RYDBERG', 'RYDBERGS'],
    'cm'   : ['cm', 'CM', 'Cm', 'centimeter', 'centimeters', 'Centimeter', 'Centimeters', 'CENTIMETER', 'CENTIMETERS'],
    'A'    : ['A', 'a', 'AA', 'aa', 'angstrom', 'angstroms', 'Angstrom', 'Angstroms', 'ANGSTROM', 'ANGSTROMS'],
    'bohr' : ['bohr', 'Bohr', 'BOHR', 'bohr', 'Bohr', 'BOHR', 'bohrradii', 'Bohrradii', 'BOHRRADII'],
    'm'    : ['m', 'M', 'meter', 'meters', 'Meter', 'Meters', 'METER', 'METERS'],
    'deg'  : ['deg', 'DEG', 'Deg', 'degree', 'degrees', 'Degree', 'Degrees', 'DEGREE', 'DEGREES'],
    'rad'  : ['rad', 'RAD', 'Rad', 'radian', 'radians', 'Radian', 'Radians', 'RADIAN', 'RADIANS'],
    'bar'  : ['bar', 'Bar', 'BAR', 'bars', 'Bars', 'BARS'],
    'kbar' : ['kbar', 'Kbar', 'KBAR', 'kilobar', 'kilobars', 'Kilobar', 'Kilobars', 'KILOBAR', 'KILOBARS'],
    'Pa'   : ['Pa', 'pa', 'PA', 'Pascal', 'Pascals', 'PASCAL', 'PASCALS'],
    'GPa'  : ['GPa', 'Gpa', 'gpa', 'GPA', 'gigapascal', 'gigapascals', 'Gigapascal', 'Gigapascals', 'GIGAPASCAL', 'GIGAPASCALS'],
    's'    : ['s', 'S', 'second', 'seconds', 'Second', 'Seconds', 'SECOND', 'SECONDS'],
    'H'    : ['H', 'h', 'hour', 'hours', 'Hour', 'Hours', 'HOUR', 'HOURS'],
}


#############################
##  MATERIAL COMPOSITIONS  ##
#############################
MAPI = Material(
    atoms={'Pb': 1, 'I': 3, 'C': 1, 'N': 1, 'H': 6},
    name='MAPbI3'
    )
MAPI.set()

MAPI_CDND = Material(
    atoms={'Pb': 1, 'I': 3, 'C': 1, 'N': 1, 'D': 6},
    name='CD3ND3PbI3'
    )
MAPI_CDND.set()

MAPI_ND = Material(
    atoms={'Pb': 1, 'I': 3, 'C': 1, 'N': 1, 'H': 3, 'D': 3},
    name='CH3ND3PbI3'
    )
MAPI_ND.set()

MAPI_CD = Material(
    atoms={'Pb': 1, 'I': 3, 'C': 1, 'N': 1, 'H': 3, 'D': 3},
    name='CD3NH3PbI3'
    )
MAPI_CD.set()

CH3NH3I = Material(
    atoms={'C' : 1, 'N': 1, 'H': 6},
    name='CH3NH3'
    )
CH3NH3I.set()

CH3ND3I = Material(
    atoms={'C' : 1, 'N': 1, 'H': 3, 'D': 3},
    name='CH3ND3'
    )
CH3ND3I.set()


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

