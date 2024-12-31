'''
# Description
This module provides the tools to create and manage the `maat.elements.atom` megadictionary,
which contains the properties of all elements.
Additionally, this module contains tools to sort and organise element data.

# Index
- `export_to_py()`
- `split_isotope()`
- `allowed_isotopes()`

# References

Atomic `mass` are in atomic mass units (amu), and come from:
Pure Appl. Chem., Vol. 78, No. 11, pp. 2051-2066, 2006.
The following masses are obtained from Wikipedia:
Ac: 227, Np: 237, Pm: 145, Tc: 98

Isotope `mass`, `mass_number` and `abundance` come from:
J. R. de Laeter, J. K. Böhlke, P. De Bièvre, H. Hidaka, H. S. Peiser, K. J. R. Rosman
and P. D. P. Taylor (2003). 'Atomic weights of the elements. Review 2000 (IUPAC Technical Report)'

Total bound scattering `cross_section` $\\sigma_s$ are in barns (1 b = 100 fm$^2$).
From Felix Fernandez-Alonso's book 'Neutron Scattering Fundamentals' (2013).

---
'''


from .elements import atom


def export_to_py(
        dict_of_elements:dict,
        filename='exported_elements.py'
    ) -> None:
    '''
    Export a dictionary of chemical elements to a python file.
    This is used to build and update the `maat.elements.atom` megadictionary, that contains
    all the element data, such as masses, cross-sections, etc.
    '''
    with open(filename, 'w') as f:
        # Write the docstrings
        f.write(
            "'''\n"
            "## Description\n"
            "This module contains the `atom` dictionary, which contains the properties of all elements.\n"
            "This module is created, managed and updated automatically with `maat.atoms`,\n"
            "which also contains the references for this data.\n"
            "The `atom` dictionary is loaded directly in Maat as `maat.atom`.\n\n"
            "Use example:\n"
            "```python\n"
            "aluminium_cross_section = maat.atom['Al'].cross_section\n"
            "He4_mass = maat.atom['H'].isotope[4].mass\n"
            "```\n\n"
            "## Index\n"
            "- `Isotope`\n"
            "- `Element`\n"
            "- `atom`\n\n"
            "## References\n"
            "See the full list of references for this data in `maat.atoms`.\n\n"
            "---\n"
            "'''\n\n\n"
        )
        # Write the Isotope and Element classes
        f.write(
            "class Isotope:\n"
            "    def __init__(self, mass_number:int=None, mass:float=None, abundance:float=None, cross_section:float=None):\n"
            "        self.mass_number: int = mass_number\n"
            "        '''Mass number (A) of the isotope. Corresponds to the total number of protons + neutrons in the core.'''\n"
            "        self.mass: float = mass\n"
            "        '''Atomic mass of the isotope, in atomic mass units (amu).'''\n"
            "        self.abundance: float = abundance\n"
            "        '''Relative abundance of the isotope.'''\n"
            "        self.cross_section: float = cross_section\n"
            "        '''Total bound scattering cross section of the isotope.'''\n\n\n"
            "class Element:\n"
            "    def __init__(self=None, number:int=None, symbol:str=None, name:str=None, mass:float=None, cross_section:float=None, isotope:dict=None):\n"
            "        self.number: int = number\n"
            "        '''Atomic number (Z). Corresponds to the number of protons / electrons.'''\n"
            "        self.symbol: str = symbol\n"
            "        '''Standard symbol of the element.'''\n"
            "        self.name: str = name\n"
            "        '''Full name.'''\n"
            "        self.mass: float = mass\n"
            "        '''Atomic mass, in atomic mass units (amu).'''\n"
            "        self.cross_section: float = cross_section\n"
            "        '''Total bound scattering cross section.'''\n"
            "        self.isotope: dict = isotope\n"
            "        '''Dictionary containing the different `Isotope` of the element. The keys are the mass number (A).'''\n\n\n"
        )
        # Start the atom megadictionary
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
                f.write("        isotope       = {\n")
                for iso in element.isotope.values():
                    f.write(f"            {iso.mass_number} : Isotope(\n")
                    if iso.mass_number:
                        f.write(f"                mass_number   = {iso.mass_number},\n")
                    if iso.mass:
                        f.write(f"                mass          = {iso.mass},\n")
                    if iso.abundance:
                        f.write(f"                abundance     = {iso.abundance},\n")
                    if iso.cross_section:
                        f.write(f"                cross_section = {iso.cross_section},\n")
                    f.write(f"                ),\n")
                f.write("            },\n")
            f.write(f"        ),\n")
        f.write("}\n")
        print(f'Exported elements to {filename}')
    return None


def split_isotope(name:str) -> tuple:
    '''
    Decomposes the `name` containing an isotope, such as 'H2' or 'He4',
    into a tuple with the element and the mass number.
    For example, 'He4' would return ('He', 4).
    If the isotope is not found in the `maat.elements.atom` megadictionary,
    it raises an error, informing of the allowed mass numbers (A) values for the given element.
    '''
    element = ''.join(filter(str.isalpha, name))
    isotope = int(''.join(filter(str.isdigit, name)))
    isotopes = allowed_isotopes(element)
    if not isotope in isotopes:
        raise KeyError(f'Unrecognised isotope: {name}. Allowed mass numbers for {element} are: {isotopes}')
    return element, isotope


def allowed_isotopes(element) -> list:
    '''
    Returns a list with the allowed mass numbers (A) of the isotopes of a given `element`.
    These mass numbers are used as isotope keys in the `maat.elements.atom` megadictionary.
    '''
    if not element in atom.keys():
        raise KeyError(f'Unrecognised element: {element}')
    isotopes = atom[element].isotope.keys()
    return isotopes

