'''
## Description
This module contains descriptions of chemical elements, such as atomic masses, cross sections, etc.

---
'''



class Isotope:
    def __init__(self, mass, abundance, mass_number, cross_section):
        self.mass = mass
        self.abundance = abundance
        self.mass_number = mass_number
        self.cross_section = cross_section


class Atom:
    def __init__(self, symbol, name, mass, atomic_number, cross_section):
        self.symbol = symbol
        self.name = name
        self.mass = mass
        self.number = atomic_number
        self.cross_section = cross_section
        self.isotope = []


