'''
## Description
This module contains useful constants and conversion factors.
Any value from this module can be acessed directly by calling it as `maat.value`.
For example, to call the planck constant in eV·s, you can use:
```python
import maat as mt
h_eV = mt.h_eV
```

## Index
- [Energy conversion factors](#energy-conversion-factors)
- [Distance conversion factors](#distance-conversion-factors)
- [Mass conversion factors](#mass-conversion-factors)
- [Pressure conversion factors](#pressure-conversion-factors)
- [Time conversion factors](#time-conversion-factors)
- [Universal constants](#universal-constants)
- [String dictionaries](#string-dictionaries)

---
'''


import numpy as np


version = 'v2.4.8'


'''---
## Energy conversion factors
Note that `cm` refers to cm$^{-1}$.
'''
eV_to_meV   = 1000.0
meV_to_eV   = 0.001
meV_to_cm   = 8.0655
cm_to_meV   = 1.0 / meV_to_cm
eV_to_J     = 1.602176634e-19
J_to_eV     = 1.0 / eV_to_J
meV_to_J    = meV_to_eV * eV_to_J
J_to_meV    = J_to_eV * eV_to_meV
Ry_to_eV    = 13.605693122990
eV_to_Ry    = 1.0 / Ry_to_eV
Ry_to_J     = 2.1798723611030e-18
J_to_Ry     = 1.0 / Ry_to_J
cal_to_J    = 4.184
J_to_cal    = 1 / cal_to_J
kcal_to_J   = cal_to_J * 1000.0
J_to_kcal   = 1 / kcal_to_J

'''---
## Distance conversion factors
Note that `A` refers to Angstroms.
'''
A_to_m      = 1.0e-10
m_to_A      = 1.0 / A_to_m
bohr_to_m   = 5.29177210544e-11
m_to_bohr   = 1.0 / bohr_to_m
A_to_bohr   = A_to_m * m_to_bohr
bohr_to_A   = 1.0 / A_to_bohr

'''---
## Mass conversion factors
'''
amu_to_kg   = 1.66053906660e-27
kg_to_amu   = 1.0 / amu_to_kg
kg_to_g     = 1000.0
g_to_kg     = 1.0 / kg_to_g

'''---
## Pressure conversion factors
'''
GPa_to_Pa   = 1.0e9
Pa_to_GPa   = 1.0 / GPa_to_Pa
kbar_to_bar = 1000.0
bar_to_kbar = 1.0 / kbar_to_bar
Pa_to_bar   = 1.0e-5
bar_to_Pa   = 1.0 / Pa_to_bar
GPa_to_kbar = GPa_to_Pa * Pa_to_bar * bar_to_kbar
kbar_to_GPa = 1.0 / GPa_to_kbar

'''---
## Time conversion factors
Note that `H` refers to hours.
'''
H_to_s      = 3600.0
s_to_H      = 1.0 / H_to_s

'''---
## Universal constants
Given in SI units unless stated otherwise.
'''
h = 6.62607015e-34      # J s
'''Planck constant, in J·s.'''
h_eV = h * J_to_eV
'''Planck constant, in eV·s.'''
hbar = h / (2 * np.pi)  # J s
'''Reduced Planck constant, in J·s.'''
hbar_eV = h_eV / (2 * np.pi)
'''Reduced Planck constant, in eV·s.'''

# Atomic masses
mass = {
    'H1': 1.00784,
    'H' : 1.00784,
    'H2': 2.014102,
    'D' : 2.014102,
    'C' : 12.0107,
    'N' : 14.0067,
    'I' : 126.90447,
    'Pb': 207.2,
}
'''
Atomic masses, in atomic mass units (amu) by default.
'''
mass_kg = {}
'''
Atomic masses, in kilograms.
'''
for key in mass:
    mass_kg[key] = mass[key] * amu_to_kg

# Total bound scattering cross sections
cross_section = {
    'H1': 81.67,
    'H' : 81.67,
    'H2': 7.64,
    'D' : 7.64,
    'C' : 5.551,
    'N' : 11.51,
    'I' : 3.81,
    'Pb': 11.118,
}
'''
Total bound scattering cross sections, in barns (1 b = 100 fm$^2$).
From Felix Fernandez-Alonso 2013 book.

---

## String dictionaries
To be used in the input correction functions.
'''

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
    'cm-1' : ['cm^{-1}', 'cm1', 'cm-1', 'cm^-1', 'Cm1', 'Cm-1', 'Cm^-1', 'Cm^{-1}', 'CM1', 'CM-1', 'CM^-1', 'CM^{-1}'],
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
'''
Strings with the name of the units, used to correct and normalise user inputs.
'''

# Spectra types
spectra_keys = {
    'INS' : ['INS', 'ins', 'Ins', 'InelasticNeutronScattering'],
    'ATR' : ['ATR', 'atr', 'FTIR', 'ftir', 'AttenuatedTotalReflection'],
    'RAMAN' : ['RAMAN', 'raman', 'Raman'],
}
'''
Strings with the name of the spectra types, to correct user inputs.
'''

file_keys = {
    'Error' : ['Error', 'error', 'ERROR', 'Errors', 'errors', 'ERRORS'],
}
'''
Strings with the name of the file types, to correct user inputs.
'''

confirmation_keys = {
    'yes' : ['yes', 'YES', 'Yes', 'Y', 'y'],
    'no'  : ['no', 'NO', 'No', 'N', 'n'],
}
'''
Strings with confirmations such as 'yes' / 'no', to correct user inputs.
'''

