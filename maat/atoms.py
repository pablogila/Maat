'''
## Description
This module contains the tools to create and manage the `maat.atomsdict.atom` megadictionary,
which contains the properties of all elements. 

## Index
- `write_to_py()`
- `get_isotope_index()`


## References

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


from .atomsdict import atom


def write_to_py(dict_of_elements:dict, filename='exported_elements.py'):
    with open(filename, 'w') as f:
        f.write(
            "'''\n"
            "## Description\n"
            "This module contains the `atom` dictionary, which contains the properties of all elements.\n"
            "This module is created, managed and updated automatically with `maat.atoms`,\n"
            "which also contains the references for this data.\n"
            "The `atom` dictionary is loaded directly in `maat` as `maat.atom`.\n\n"
            "Use example:\n"
            "```python\n"
            "aluminium_cross_section = maat.atom['Al'].cross_section\n"
            "protium_mass   = maat.atom['H'].isotope[0].mass\n"
            "deuterium_mass = maat.atom['H'].isotope[1].mass\n"
            "```\n\n"
            "---\n"
            "'''\n\n\n"
            "from elementclass import *\n\n\n"
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
                        f.write(f"                cross_section = {iso.cross_section},\n")
                    f.write(f"                ),\n")
                f.write("            ],\n")
            f.write(f"        ),\n")
        f.write("}\n")
        print(f'Exported atoms to {filename}')
    return None
'''
Export a dictionary of elements to a python file.
This is used to build and update the `maat.atoms` module, that contains
the `atom` dict with all the element data, such as masses, cross-sections, etc.
'''


def get_isotope_index(name:str):
    '''
    Decomposes the `name` containing an isotope, such as 'H2' or 'He4',
    into a tuple with the element and the isotope index in `maat.atoms.atom`.
    For example, 'H2' would return ('H', 1).
    '''
    element = ''.join(filter(str.isalpha, name))
    number = int(''.join(filter(str.isdigit, name)))
    i = 0
    isotope_index = None
    if element in atom.keys():
        for isotope in atom[element].isotope:
            if isotope.mass_number == number:
                isotope_index = i
                return element, isotope_index
            i += 1
        # mass_number not found, raise error
        allowed_mass_numbers = []
        for iso in atom[element].isotope:
            allowed_mass_numbers.append(iso.mass_number)
        raise KeyError(f'Unrecognised isotope: {name}. Allowed mass numbers for {key_letters} are: {allowed_mass_numbers}')
    raise KeyError(f'Unrecognised atom: {name}. What is {element}?')

