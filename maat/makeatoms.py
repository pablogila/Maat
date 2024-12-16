'''
## Description
This module provides the tools to build the `maat.atoms` submodule,
which contains the `maat.atoms.atom` dictionary.
This dictionary carries the information of every element: isotope mass, cross section, etc.

## Index
- `Isotope`
- `Element`
- `write_elements_to_py()`

---
'''


class Isotope:
    def __init__(self, mass=None, abundance=None, mass_number=None, cross_section=None):
        self.mass = mass
        '''Atomic mass of the isotope, in atomic mass units (amu)'''
        self.abundance = abundance
        '''Relative abundance of the isotope'''
        self.mass_number = mass_number
        '''Mass number (A) of the isotope. Corresponds to the total number of protons + neutrons in the core'''
        self.cross_section = cross_section
        '''Total bound scattering cross section of the isotope'''


class Element:
    def __init__(self=None, symbol=None, name=None, mass=None, number=None, cross_section=None, isotope=None):
        self.symbol = symbol
        '''Standard symbol'''
        self.name = name
        '''Full name'''
        self.mass = mass
        '''Atomic mass, in atomic mass units (amu)'''
        self.number = number
        '''Atomic number (Z). Corresponds to the number of protons / electrons'''
        self.cross_section = cross_section
        '''Total bound scattering cross section'''
        self.isotope = []
        '''List containing `Isotope`s of the element'''


def write_elements_to_py(dict_of_elements:dict, filename='exported_elements.py'):
    with open(filename, 'w') as f:
        f.write(
            "'''\n"
            "## Description.\n\n"
            "This module contains the `atom` dictionary, which contains the properties of all elements.\n"
            "This module is created and updated automatically with `maat.makeatoms`.\n\n"
            "Use example:\n"
            "```python\n"
            "aluminium_cross_section = maat.atom['Al'].cross_section\n"
            "protium_mass   = maat.atom['H'].isotope[0].mass\n"
            "deuterium_mass = maat.atom['H'].isotope[1].mass\n"
            "```\n\n"
            "## References\n\n"
            "Atomic `mass`es are in atomic mass units (amu), and come from:\n\n"
            "Pure Appl. Chem., Vol. 78, No. 11, pp. 2051-2066, 2006.\n"
            "The following masses are obtained from Wikipedia:\n"
            "Ac: 227, Np: 237, Pm: 145, Tc: 98\n\n"
            "Isotope `mass`, `mass_number` and `abundance` come from:\n"
            "J. R. de Laeter, J. K. Böhlke, P. De Bièvre, H. Hidaka, H. S. Peiser, K. J. R. Rosman\n"
            "and P. D. P. Taylor (2003). 'Atomic weights of the elements. Review 2000 (IUPAC Technical Report)'\n"
            "Total bound scattering `cross_section`s $\\sigma_s$ are in barns (1 b = 100 fm$^2$).\n"
            "From Felix Fernandez-Alonso's book 'Neutron Scattering Fundamentals' (2013).\n\n"
            "---\n"
            "'''\n\n\n"
            "from .makeatoms import Element, Isotope\n\n\n"
        )
        f.write("atom = {\n")
        for key, element in dict_of_elements.items():
            f.write(f"    '{element.symbol}': Element(\n"
                    f"        number        = {element.number},\n"
                    f"        symbol        = '{element.symbol}',\n"
                    f"        name          = '{element.name}',\n")
            if element.mass:
                f.write(f"        mass          = {element.mass},\n")
            if element.cross_section:
                f.write(f"        cross_section = {element.cross_section},\n")
            if element.isotope:
                f.write("        isotope       = [\n")
                for iso in element.isotope:
                    f.write(f"            Isotope(\n")
                    if iso.mass_number:
                        f.write(f"                mass_number   = {iso.mass_number},\n")
                    if iso.mass:
                        f.write(f"                mass          = {iso.mass},\n")
                    if iso.abundance:
                        f.write(f"                abundance     = {iso.abundance},\n")
                    if iso.cross_section:
                        f.write(f"                cross_section = {iso.cross_section}),\n")
                    f.write(f"                ),\n")
                f.write("            ],\n")
            f.write(f"        ),\n")
        f.write("}\n")
    return None
'''
Export a dictionary of elements to a python file.
This is used to build and update the `maat.atoms` module, that contains
the `` all atomic data such as element masses, cross-sections, etc.
'''

