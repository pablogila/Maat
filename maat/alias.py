'''
# Description
Similar to [thoth.alias](https://pablogila.github.io/Thoth/thoth/alias.html), this module contains common dictionaries with science-related stings, to normalize user inputs.

# Index
- `unit`
- `experiment`

---
'''


unit: dict = {
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
Dict with unit names, used to correct and normalise user inputs.
'''

experiment: dict = {
    'INS' : ['INS', 'ins', 'Ins', 'InelasticNeutronScattering'],
    'ATR' : ['ATR', 'atr', 'FTIR', 'ftir', 'AttenuatedTotalReflection'],
    'RAMAN' : ['RAMAN', 'raman', 'Raman'],
}
'''
Dictionary with experiment types, to correct user inputs.
'''

