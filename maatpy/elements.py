'''
# Description
This module contains the `atom` dictionary, which contains the properties of all elements.
This module is created, managed and updated automatically with `maatpy.atoms`,
which also contains the references for this data.
The `atom` dictionary is loaded directly in Maat as `maatpy.atom`.

Use example:
```python
aluminium_cross_section = maatpy.atom['Al'].cross_section
He4_mass = maatpy.atom['H'].isotope[4].mass
```

# Index
- `Isotope`
- `Element`
- `atom`

# References
See the full list of references for this data in `maatpy.atoms`.

---
'''


class Isotope:
    def __init__(self, mass_number:int=None, mass:float=None, abundance:float=None, cross_section:float=None):
        self.mass_number: int = mass_number
        '''Mass number (A) of the isotope. Corresponds to the total number of protons + neutrons in the core.'''
        self.mass: float = mass
        '''Atomic mass of the isotope, in atomic mass units (amu).'''
        self.abundance: float = abundance
        '''Relative abundance of the isotope.'''
        self.cross_section: float = cross_section
        '''Total bound scattering cross section of the isotope.'''


class Element:
    def __init__(self=None, number:int=None, symbol:str=None, name:str=None, mass:float=None, cross_section:float=None, isotope:dict=None):
        self.number: int = number
        '''Atomic number (Z). Corresponds to the number of protons / electrons.'''
        self.symbol: str = symbol
        '''Standard symbol of the element.'''
        self.name: str = name
        '''Full name.'''
        self.mass: float = mass
        '''Atomic mass, in atomic mass units (amu).'''
        self.cross_section: float = cross_section
        '''Total bound scattering cross section.'''
        self.isotope: dict = isotope
        '''Dictionary containing the different `Isotope` of the element. The keys are the mass number (A).'''


atom = {
    'H': Element(
        number        = 1,
        symbol        = 'H',
        name          = 'Hydrogen',
        mass          = 1.00794,
        cross_section = 82.02,
        isotope       = {
            1 : Isotope(
                mass_number   = 1,
                mass          = 1.0078250319,
                abundance     = 0.999885,
                cross_section = 81.67,
                ),
            2 : Isotope(
                mass_number   = 2,
                mass          = 2.0141017779,
                abundance     = 0.000115,
                cross_section = 7.64,
                ),
            },
        ),
    'He': Element(
        number        = 2,
        symbol        = 'He',
        name          = 'Helium',
        mass          = 4.002602,
        cross_section = 1.34,
        isotope       = {
            3 : Isotope(
                mass_number   = 3,
                mass          = 3.0160293094,
                abundance     = 1.34e-06,
                ),
            4 : Isotope(
                mass_number   = 4,
                mass          = 4.0026032497,
                abundance     = 0.99999866,
                ),
            },
        ),
    'Li': Element(
        number        = 3,
        symbol        = 'Li',
        name          = 'Lithium',
        mass          = 6.941,
        cross_section = 1.37,
        isotope       = {
            6 : Isotope(
                mass_number   = 6,
                mass          = 6.0151223,
                abundance     = 0.0759,
                ),
            7 : Isotope(
                mass_number   = 7,
                mass          = 7.0160041,
                abundance     = 0.9241,
                ),
            },
        ),
    'Be': Element(
        number        = 4,
        symbol        = 'Be',
        name          = 'Beryllium',
        mass          = 9.012182,
        cross_section = 7.63,
        isotope       = {
            9 : Isotope(
                mass_number   = 9,
                mass          = 9.0121822,
                abundance     = 1.0,
                ),
            },
        ),
    'B': Element(
        number        = 5,
        symbol        = 'B',
        name          = 'Boron',
        mass          = 10.811,
        cross_section = 5.24,
        isotope       = {
            10 : Isotope(
                mass_number   = 10,
                mass          = 10.0129371,
                abundance     = 0.199,
                ),
            11 : Isotope(
                mass_number   = 11,
                mass          = 11.0093055,
                abundance     = 0.801,
                ),
            },
        ),
    'C': Element(
        number        = 6,
        symbol        = 'C',
        name          = 'Carbon',
        mass          = 12.0107,
        cross_section = 5.551,
        isotope       = {
            12 : Isotope(
                mass_number   = 12,
                mass          = 12,
                abundance     = 0.9893,
                ),
            13 : Isotope(
                mass_number   = 13,
                mass          = 13.003354838,
                abundance     = 0.0107,
                ),
            },
        ),
    'N': Element(
        number        = 7,
        symbol        = 'N',
        name          = 'Nitrogen',
        mass          = 14.0067,
        cross_section = 11.51,
        isotope       = {
            14 : Isotope(
                mass_number   = 14,
                mass          = 14.0030740074,
                abundance     = 0.99636,
                ),
            15 : Isotope(
                mass_number   = 15,
                mass          = 15.000108973,
                abundance     = 0.00364,
                ),
            },
        ),
    'O': Element(
        number        = 8,
        symbol        = 'O',
        name          = 'Oxygen',
        mass          = 15.9994,
        cross_section = 4.232,
        isotope       = {
            16 : Isotope(
                mass_number   = 16,
                mass          = 15.9949146223,
                abundance     = 0.99757,
                ),
            17 : Isotope(
                mass_number   = 17,
                mass          = 16.9991315,
                abundance     = 0.00038,
                ),
            18 : Isotope(
                mass_number   = 18,
                mass          = 17.9991604,
                abundance     = 0.00205,
                ),
            },
        ),
    'F': Element(
        number        = 9,
        symbol        = 'F',
        name          = 'Fluorine',
        mass          = 18.9984032,
        cross_section = 4.018,
        isotope       = {
            19 : Isotope(
                mass_number   = 19,
                mass          = 18.9984032,
                abundance     = 1.0,
                ),
            },
        ),
    'Ne': Element(
        number        = 10,
        symbol        = 'Ne',
        name          = 'Neon',
        mass          = 20.1797,
        cross_section = 2.628,
        isotope       = {
            20 : Isotope(
                mass_number   = 20,
                mass          = 19.992440176,
                abundance     = 0.9048,
                ),
            21 : Isotope(
                mass_number   = 21,
                mass          = 20.99384674,
                abundance     = 0.0027,
                ),
            22 : Isotope(
                mass_number   = 22,
                mass          = 21.9913855,
                abundance     = 0.0925,
                ),
            },
        ),
    'Na': Element(
        number        = 11,
        symbol        = 'Na',
        name          = 'Sodium',
        mass          = 22.98976928,
        cross_section = 3.28,
        isotope       = {
            23 : Isotope(
                mass_number   = 23,
                mass          = 22.98976966,
                abundance     = 1.0,
                ),
            },
        ),
    'Mg': Element(
        number        = 12,
        symbol        = 'Mg',
        name          = 'Magnesium',
        mass          = 24.305,
        cross_section = 3.71,
        isotope       = {
            24 : Isotope(
                mass_number   = 24,
                mass          = 23.98504187,
                abundance     = 0.7899,
                ),
            25 : Isotope(
                mass_number   = 25,
                mass          = 24.985837,
                abundance     = 0.1,
                ),
            26 : Isotope(
                mass_number   = 26,
                mass          = 25.982593,
                abundance     = 0.1101,
                ),
            },
        ),
    'Al': Element(
        number        = 13,
        symbol        = 'Al',
        name          = 'Aluminium',
        mass          = 26.9815386,
        cross_section = 1.503,
        isotope       = {
            27 : Isotope(
                mass_number   = 27,
                mass          = 26.98153841,
                abundance     = 1.0,
                ),
            },
        ),
    'Si': Element(
        number        = 14,
        symbol        = 'Si',
        name          = 'Silicon',
        mass          = 28.0855,
        cross_section = 2.167,
        isotope       = {
            28 : Isotope(
                mass_number   = 28,
                mass          = 27.97692649,
                abundance     = 0.92223,
                ),
            29 : Isotope(
                mass_number   = 29,
                mass          = 28.97649468,
                abundance     = 0.04685,
                ),
            30 : Isotope(
                mass_number   = 30,
                mass          = 29.97377018,
                abundance     = 0.03092,
                ),
            },
        ),
    'P': Element(
        number        = 15,
        symbol        = 'P',
        name          = 'Phosphorus',
        mass          = 30.973762,
        cross_section = 3.312,
        isotope       = {
            31 : Isotope(
                mass_number   = 31,
                mass          = 30.97376149,
                abundance     = 1.0,
                ),
            },
        ),
    'S': Element(
        number        = 16,
        symbol        = 'S',
        name          = 'Sulfur',
        mass          = 32.065,
        cross_section = 1.026,
        isotope       = {
            32 : Isotope(
                mass_number   = 32,
                mass          = 31.97207073,
                abundance     = 0.9499,
                ),
            33 : Isotope(
                mass_number   = 33,
                mass          = 32.97145854,
                abundance     = 0.0075,
                ),
            34 : Isotope(
                mass_number   = 34,
                mass          = 33.96786687,
                abundance     = 0.0425,
                ),
            36 : Isotope(
                mass_number   = 36,
                mass          = 35.96708088,
                abundance     = 0.0001,
                ),
            },
        ),
    'Cl': Element(
        number        = 17,
        symbol        = 'Cl',
        name          = 'Chlorine',
        mass          = 35.453,
        cross_section = 16.8,
        isotope       = {
            35 : Isotope(
                mass_number   = 35,
                mass          = 34.96885271,
                abundance     = 0.7576,
                ),
            37 : Isotope(
                mass_number   = 37,
                mass          = 36.9659026,
                abundance     = 0.2424,
                ),
            },
        ),
    'Ar': Element(
        number        = 18,
        symbol        = 'Ar',
        name          = 'Argon',
        mass          = 39.948,
        cross_section = 0.683,
        isotope       = {
            36 : Isotope(
                mass_number   = 36,
                mass          = 35.96754626,
                abundance     = 0.003365,
                ),
            38 : Isotope(
                mass_number   = 38,
                mass          = 37.9627322,
                abundance     = 0.000632,
                ),
            40 : Isotope(
                mass_number   = 40,
                mass          = 39.962383124,
                abundance     = 0.996003,
                ),
            },
        ),
    'K': Element(
        number        = 19,
        symbol        = 'K',
        name          = 'Potassium',
        mass          = 39.0983,
        cross_section = 1.96,
        isotope       = {
            39 : Isotope(
                mass_number   = 39,
                mass          = 38.9637,
                abundance     = 0.932581,
                ),
            40 : Isotope(
                mass_number   = 40,
                mass          = 39.96399867,
                abundance     = 0.000117,
                ),
            41 : Isotope(
                mass_number   = 41,
                mass          = 40.96182597,
                abundance     = 0.067302,
                ),
            },
        ),
    'Ca': Element(
        number        = 20,
        symbol        = 'Ca',
        name          = 'Calcium',
        mass          = 40.078,
        cross_section = 2.83,
        isotope       = {
            40 : Isotope(
                mass_number   = 40,
                mass          = 39.9625912,
                abundance     = 0.96941,
                ),
            42 : Isotope(
                mass_number   = 42,
                mass          = 41.9586183,
                abundance     = 0.00647,
                ),
            43 : Isotope(
                mass_number   = 43,
                mass          = 42.9587668,
                abundance     = 0.00135,
                ),
            44 : Isotope(
                mass_number   = 44,
                mass          = 43.9554811,
                abundance     = 0.02086,
                ),
            46 : Isotope(
                mass_number   = 46,
                mass          = 45.9536927,
                abundance     = 4e-05,
                ),
            48 : Isotope(
                mass_number   = 48,
                mass          = 47.952533,
                abundance     = 0.00187,
                ),
            },
        ),
    'Sc': Element(
        number        = 21,
        symbol        = 'Sc',
        name          = 'Scandium',
        mass          = 44.955912,
        cross_section = 23.5,
        isotope       = {
            45 : Isotope(
                mass_number   = 45,
                mass          = 44.9559102,
                abundance     = 1.0,
                ),
            },
        ),
    'Ti': Element(
        number        = 22,
        symbol        = 'Ti',
        name          = 'Titanium',
        mass          = 47.867,
        cross_section = 4.35,
        isotope       = {
            46 : Isotope(
                mass_number   = 46,
                mass          = 45.9526295,
                abundance     = 0.0825,
                ),
            47 : Isotope(
                mass_number   = 47,
                mass          = 46.9517637,
                abundance     = 0.0744,
                ),
            48 : Isotope(
                mass_number   = 48,
                mass          = 47.947947,
                abundance     = 0.7372,
                ),
            49 : Isotope(
                mass_number   = 49,
                mass          = 48.9478707,
                abundance     = 0.0541,
                ),
            50 : Isotope(
                mass_number   = 50,
                mass          = 49.944792,
                abundance     = 0.0518,
                ),
            },
        ),
    'V': Element(
        number        = 23,
        symbol        = 'V',
        name          = 'Vanadium',
        mass          = 50.9415,
        cross_section = 5.1,
        isotope       = {
            50 : Isotope(
                mass_number   = 50,
                mass          = 49.9471627,
                abundance     = 0.0025,
                ),
            51 : Isotope(
                mass_number   = 51,
                mass          = 50.9439635,
                abundance     = 0.9975,
                ),
            },
        ),
    'Cr': Element(
        number        = 24,
        symbol        = 'Cr',
        name          = 'Chromium',
        mass          = 51.9961,
        cross_section = 3.49,
        isotope       = {
            50 : Isotope(
                mass_number   = 50,
                mass          = 49.9460495,
                abundance     = 0.04345,
                ),
            52 : Isotope(
                mass_number   = 52,
                mass          = 51.9405115,
                abundance     = 0.83789,
                ),
            53 : Isotope(
                mass_number   = 53,
                mass          = 52.9406534,
                abundance     = 0.09501,
                ),
            54 : Isotope(
                mass_number   = 54,
                mass          = 53.9388846,
                abundance     = 0.02365,
                ),
            },
        ),
    'Mn': Element(
        number        = 25,
        symbol        = 'Mn',
        name          = 'Manganese',
        mass          = 54.938045,
        cross_section = 2.15,
        isotope       = {
            55 : Isotope(
                mass_number   = 55,
                mass          = 54.9380493,
                abundance     = 1.0,
                ),
            },
        ),
    'Fe': Element(
        number        = 26,
        symbol        = 'Fe',
        name          = 'Iron',
        mass          = 55.845,
        cross_section = 11.62,
        isotope       = {
            54 : Isotope(
                mass_number   = 54,
                mass          = 53.9396147,
                abundance     = 0.05845,
                ),
            56 : Isotope(
                mass_number   = 56,
                mass          = 55.9349418,
                abundance     = 0.91754,
                ),
            57 : Isotope(
                mass_number   = 57,
                mass          = 56.9353983,
                abundance     = 0.02119,
                ),
            58 : Isotope(
                mass_number   = 58,
                mass          = 57.9332801,
                abundance     = 0.00282,
                ),
            },
        ),
    'Co': Element(
        number        = 27,
        symbol        = 'Co',
        name          = 'Cobalt',
        mass          = 58.933195,
        cross_section = 5.6,
        isotope       = {
            59 : Isotope(
                mass_number   = 59,
                mass          = 58.9331999,
                abundance     = 1.0,
                ),
            },
        ),
    'Ni': Element(
        number        = 28,
        symbol        = 'Ni',
        name          = 'Nickel',
        mass          = 58.6934,
        cross_section = 18.5,
        isotope       = {
            58 : Isotope(
                mass_number   = 58,
                mass          = 57.9353477,
                abundance     = 0.680769,
                ),
            60 : Isotope(
                mass_number   = 60,
                mass          = 59.9307903,
                abundance     = 0.262231,
                ),
            61 : Isotope(
                mass_number   = 61,
                mass          = 60.9310601,
                abundance     = 0.011399,
                ),
            62 : Isotope(
                mass_number   = 62,
                mass          = 61.9283484,
                abundance     = 0.036345,
                ),
            64 : Isotope(
                mass_number   = 64,
                mass          = 63.9279692,
                abundance     = 0.009256,
                ),
            },
        ),
    'Cu': Element(
        number        = 29,
        symbol        = 'Cu',
        name          = 'Copper',
        mass          = 63.546,
        cross_section = 8.03,
        isotope       = {
            63 : Isotope(
                mass_number   = 63,
                mass          = 62.9296007,
                abundance     = 0.6915,
                ),
            65 : Isotope(
                mass_number   = 65,
                mass          = 64.9277938,
                abundance     = 0.3085,
                ),
            },
        ),
    'Zn': Element(
        number        = 30,
        symbol        = 'Zn',
        name          = 'Zinc',
        mass          = 65.38,
        cross_section = 4.131,
        isotope       = {
            64 : Isotope(
                mass_number   = 64,
                mass          = 63.9291461,
                abundance     = 0.48268,
                ),
            66 : Isotope(
                mass_number   = 66,
                mass          = 65.9260364,
                abundance     = 0.27975,
                ),
            67 : Isotope(
                mass_number   = 67,
                mass          = 66.9271305,
                abundance     = 0.04102,
                ),
            68 : Isotope(
                mass_number   = 68,
                mass          = 67.9248473,
                abundance     = 0.19024,
                ),
            70 : Isotope(
                mass_number   = 70,
                mass          = 69.925325,
                abundance     = 0.00631,
                ),
            },
        ),
    'Ga': Element(
        number        = 31,
        symbol        = 'Ga',
        name          = 'Gallium',
        mass          = 69.723,
        cross_section = 6.83,
        isotope       = {
            69 : Isotope(
                mass_number   = 69,
                mass          = 68.925581,
                abundance     = 0.60108,
                ),
            71 : Isotope(
                mass_number   = 71,
                mass          = 70.9247073,
                abundance     = 0.39892,
                ),
            },
        ),
    'Ge': Element(
        number        = 32,
        symbol        = 'Ge',
        name          = 'Germanium',
        mass          = 72.64,
        cross_section = 8.6,
        isotope       = {
            70 : Isotope(
                mass_number   = 70,
                mass          = 69.92425,
                abundance     = 0.2038,
                ),
            72 : Isotope(
                mass_number   = 72,
                mass          = 71.9220763,
                abundance     = 0.2731,
                ),
            73 : Isotope(
                mass_number   = 73,
                mass          = 72.9234595,
                abundance     = 0.0776,
                ),
            74 : Isotope(
                mass_number   = 74,
                mass          = 73.9211784,
                abundance     = 0.3672,
                ),
            76 : Isotope(
                mass_number   = 76,
                mass          = 75.921402,
                abundance     = 0.0783,
                ),
            },
        ),
    'As': Element(
        number        = 33,
        symbol        = 'As',
        name          = 'Arsenic',
        mass          = 74.9216,
        cross_section = 5.5,
        isotope       = {
            75 : Isotope(
                mass_number   = 75,
                mass          = 74.9215966,
                abundance     = 1.0,
                ),
            },
        ),
    'Se': Element(
        number        = 34,
        symbol        = 'Se',
        name          = 'Selenium',
        mass          = 78.96,
        cross_section = 8.3,
        isotope       = {
            74 : Isotope(
                mass_number   = 74,
                mass          = 73.9224767,
                abundance     = 0.0089,
                ),
            76 : Isotope(
                mass_number   = 76,
                mass          = 75.9192143,
                abundance     = 0.0937,
                ),
            77 : Isotope(
                mass_number   = 77,
                mass          = 76.9199148,
                abundance     = 0.0763,
                ),
            78 : Isotope(
                mass_number   = 78,
                mass          = 77.9173097,
                abundance     = 0.2377,
                ),
            80 : Isotope(
                mass_number   = 80,
                mass          = 79.9165221,
                abundance     = 0.4961,
                ),
            82 : Isotope(
                mass_number   = 82,
                mass          = 81.9167003,
                abundance     = 0.0873,
                ),
            },
        ),
    'Br': Element(
        number        = 35,
        symbol        = 'Br',
        name          = 'Bromine',
        mass          = 79.904,
        cross_section = 5.9,
        isotope       = {
            79 : Isotope(
                mass_number   = 79,
                mass          = 78.9183379,
                abundance     = 0.5069,
                ),
            81 : Isotope(
                mass_number   = 81,
                mass          = 80.916291,
                abundance     = 0.4931,
                ),
            },
        ),
    'Kr': Element(
        number        = 36,
        symbol        = 'Kr',
        name          = 'Krypton',
        mass          = 83.798,
        cross_section = 7.68,
        isotope       = {
            78 : Isotope(
                mass_number   = 78,
                mass          = 77.920388,
                abundance     = 0.00355,
                ),
            80 : Isotope(
                mass_number   = 80,
                mass          = 79.916379,
                abundance     = 0.02286,
                ),
            82 : Isotope(
                mass_number   = 82,
                mass          = 81.913485,
                abundance     = 0.11593,
                ),
            83 : Isotope(
                mass_number   = 83,
                mass          = 82.914137,
                abundance     = 0.115,
                ),
            84 : Isotope(
                mass_number   = 84,
                mass          = 83.911508,
                abundance     = 0.56987,
                ),
            86 : Isotope(
                mass_number   = 86,
                mass          = 85.910615,
                abundance     = 0.17279,
                ),
            },
        ),
    'Rb': Element(
        number        = 37,
        symbol        = 'Rb',
        name          = 'Rubidium',
        mass          = 85.4678,
        cross_section = 6.8,
        isotope       = {
            85 : Isotope(
                mass_number   = 85,
                mass          = 84.9117924,
                abundance     = 0.7217,
                ),
            87 : Isotope(
                mass_number   = 87,
                mass          = 86.9091858,
                abundance     = 0.2783,
                ),
            },
        ),
    'Sr': Element(
        number        = 38,
        symbol        = 'Sr',
        name          = 'Strontium',
        mass          = 87.62,
        cross_section = 6.25,
        isotope       = {
            84 : Isotope(
                mass_number   = 84,
                mass          = 83.913426,
                abundance     = 0.0056,
                ),
            86 : Isotope(
                mass_number   = 86,
                mass          = 85.9092647,
                abundance     = 0.0986,
                ),
            87 : Isotope(
                mass_number   = 87,
                mass          = 86.9088816,
                abundance     = 0.07,
                ),
            88 : Isotope(
                mass_number   = 88,
                mass          = 87.9056167,
                abundance     = 0.8258,
                ),
            },
        ),
    'Y': Element(
        number        = 39,
        symbol        = 'Y',
        name          = 'Yttrium',
        mass          = 88.90585,
        cross_section = 7.7,
        isotope       = {
            89 : Isotope(
                mass_number   = 89,
                mass          = 88.9058485,
                abundance     = 1.0,
                ),
            },
        ),
    'Zr': Element(
        number        = 40,
        symbol        = 'Zr',
        name          = 'Zirconium',
        mass          = 91.224,
        cross_section = 6.46,
        isotope       = {
            90 : Isotope(
                mass_number   = 90,
                mass          = 89.9047022,
                abundance     = 0.5145,
                ),
            91 : Isotope(
                mass_number   = 91,
                mass          = 90.9056434,
                abundance     = 0.1122,
                ),
            92 : Isotope(
                mass_number   = 92,
                mass          = 91.9050386,
                abundance     = 0.1715,
                ),
            94 : Isotope(
                mass_number   = 94,
                mass          = 93.9063144,
                abundance     = 0.1738,
                ),
            96 : Isotope(
                mass_number   = 96,
                mass          = 95.908275,
                abundance     = 0.028,
                ),
            },
        ),
    'Nb': Element(
        number        = 41,
        symbol        = 'Nb',
        name          = 'Niobium',
        mass          = 92.90638,
        cross_section = 6.255,
        isotope       = {
            93 : Isotope(
                mass_number   = 93,
                mass          = 92.9063762,
                abundance     = 1.0,
                ),
            },
        ),
    'Mo': Element(
        number        = 42,
        symbol        = 'Mo',
        name          = 'Molybdenum',
        mass          = 95.96,
        cross_section = 5.71,
        isotope       = {
            92 : Isotope(
                mass_number   = 92,
                mass          = 91.90681,
                abundance     = 0.1477,
                ),
            94 : Isotope(
                mass_number   = 94,
                mass          = 93.9050867,
                abundance     = 0.0923,
                ),
            95 : Isotope(
                mass_number   = 95,
                mass          = 94.9058406,
                abundance     = 0.159,
                ),
            96 : Isotope(
                mass_number   = 96,
                mass          = 95.904678,
                abundance     = 0.1668,
                ),
            97 : Isotope(
                mass_number   = 97,
                mass          = 96.9060201,
                abundance     = 0.0956,
                ),
            98 : Isotope(
                mass_number   = 98,
                mass          = 97.905406,
                abundance     = 0.2419,
                ),
            100 : Isotope(
                mass_number   = 100,
                mass          = 99.907476,
                abundance     = 0.0967,
                ),
            },
        ),
    'Tc': Element(
        number        = 43,
        symbol        = 'Tc',
        name          = 'Technetium',
        mass          = 98,
        cross_section = 6.3,
        ),
    'Ru': Element(
        number        = 44,
        symbol        = 'Ru',
        name          = 'Ruthenium',
        mass          = 101.07,
        cross_section = 6.6,
        isotope       = {
            96 : Isotope(
                mass_number   = 96,
                mass          = 95.907604,
                abundance     = 0.0554,
                ),
            98 : Isotope(
                mass_number   = 98,
                mass          = 97.905287,
                abundance     = 0.0187,
                ),
            99 : Isotope(
                mass_number   = 99,
                mass          = 98.9059385,
                abundance     = 0.1276,
                ),
            100 : Isotope(
                mass_number   = 100,
                mass          = 99.9042189,
                abundance     = 0.126,
                ),
            101 : Isotope(
                mass_number   = 101,
                mass          = 100.9055815,
                abundance     = 0.1706,
                ),
            102 : Isotope(
                mass_number   = 102,
                mass          = 101.9043488,
                abundance     = 0.3155,
                ),
            104 : Isotope(
                mass_number   = 104,
                mass          = 103.90543,
                abundance     = 0.1862,
                ),
            },
        ),
    'Rh': Element(
        number        = 45,
        symbol        = 'Rh',
        name          = 'Rhodium',
        mass          = 102.9055,
        cross_section = 4.39,
        isotope       = {
            103 : Isotope(
                mass_number   = 103,
                mass          = 102.905504,
                abundance     = 1.0,
                ),
            },
        ),
    'Pd': Element(
        number        = 46,
        symbol        = 'Pd',
        name          = 'Palladium',
        mass          = 106.42,
        cross_section = 4.48,
        isotope       = {
            102 : Isotope(
                mass_number   = 102,
                mass          = 101.905607,
                abundance     = 0.0102,
                ),
            104 : Isotope(
                mass_number   = 104,
                mass          = 103.904034,
                abundance     = 0.1114,
                ),
            105 : Isotope(
                mass_number   = 105,
                mass          = 104.905083,
                abundance     = 0.2233,
                ),
            106 : Isotope(
                mass_number   = 106,
                mass          = 105.903484,
                abundance     = 0.2733,
                ),
            108 : Isotope(
                mass_number   = 108,
                mass          = 107.903895,
                abundance     = 0.2646,
                ),
            110 : Isotope(
                mass_number   = 110,
                mass          = 109.905153,
                abundance     = 0.1172,
                ),
            },
        ),
    'Ag': Element(
        number        = 47,
        symbol        = 'Ag',
        name          = 'Silver',
        mass          = 107.8682,
        cross_section = 4.99,
        isotope       = {
            107 : Isotope(
                mass_number   = 107,
                mass          = 106.905093,
                abundance     = 0.51839,
                ),
            109 : Isotope(
                mass_number   = 109,
                mass          = 108.904756,
                abundance     = 0.48161,
                ),
            },
        ),
    'Cd': Element(
        number        = 48,
        symbol        = 'Cd',
        name          = 'Cadmium',
        mass          = 112.411,
        cross_section = 6.5,
        isotope       = {
            106 : Isotope(
                mass_number   = 106,
                mass          = 105.906458,
                abundance     = 0.0125,
                ),
            108 : Isotope(
                mass_number   = 108,
                mass          = 107.904183,
                abundance     = 0.0089,
                ),
            110 : Isotope(
                mass_number   = 110,
                mass          = 109.903006,
                abundance     = 0.1249,
                ),
            111 : Isotope(
                mass_number   = 111,
                mass          = 110.904182,
                abundance     = 0.128,
                ),
            112 : Isotope(
                mass_number   = 112,
                mass          = 111.9027577,
                abundance     = 0.2413,
                ),
            113 : Isotope(
                mass_number   = 113,
                mass          = 112.9044014,
                abundance     = 0.1222,
                ),
            114 : Isotope(
                mass_number   = 114,
                mass          = 113.9033586,
                abundance     = 0.2873,
                ),
            116 : Isotope(
                mass_number   = 116,
                mass          = 115.904756,
                abundance     = 0.0749,
                ),
            },
        ),
    'In': Element(
        number        = 49,
        symbol        = 'In',
        name          = 'Indium',
        mass          = 114.818,
        cross_section = 2.62,
        isotope       = {
            113 : Isotope(
                mass_number   = 113,
                mass          = 112.904062,
                abundance     = 0.0429,
                ),
            115 : Isotope(
                mass_number   = 115,
                mass          = 114.903879,
                abundance     = 0.9571,
                ),
            },
        ),
    'Sn': Element(
        number        = 50,
        symbol        = 'Sn',
        name          = 'Tin',
        mass          = 118.71,
        cross_section = 4.892,
        isotope       = {
            112 : Isotope(
                mass_number   = 112,
                mass          = 111.904822,
                abundance     = 0.0097,
                ),
            114 : Isotope(
                mass_number   = 114,
                mass          = 113.902783,
                abundance     = 0.0066,
                ),
            115 : Isotope(
                mass_number   = 115,
                mass          = 114.903347,
                abundance     = 0.0034,
                ),
            116 : Isotope(
                mass_number   = 116,
                mass          = 115.901745,
                abundance     = 0.1454,
                ),
            117 : Isotope(
                mass_number   = 117,
                mass          = 116.902955,
                abundance     = 0.0768,
                ),
            118 : Isotope(
                mass_number   = 118,
                mass          = 117.901608,
                abundance     = 0.2422,
                ),
            119 : Isotope(
                mass_number   = 119,
                mass          = 118.903311,
                abundance     = 0.0859,
                ),
            120 : Isotope(
                mass_number   = 120,
                mass          = 119.9021985,
                abundance     = 0.3258,
                ),
            122 : Isotope(
                mass_number   = 122,
                mass          = 121.9034411,
                abundance     = 0.0463,
                ),
            124 : Isotope(
                mass_number   = 124,
                mass          = 123.9052745,
                abundance     = 0.0579,
                ),
            },
        ),
    'Sb': Element(
        number        = 51,
        symbol        = 'Sb',
        name          = 'Antimony',
        mass          = 121.76,
        cross_section = 3.9,
        isotope       = {
            121 : Isotope(
                mass_number   = 121,
                mass          = 120.9038222,
                abundance     = 0.5721,
                ),
            123 : Isotope(
                mass_number   = 123,
                mass          = 122.904216,
                abundance     = 0.4279,
                ),
            },
        ),
    'Te': Element(
        number        = 52,
        symbol        = 'Te',
        name          = 'Tellurium',
        mass          = 127.6,
        cross_section = 4.32,
        isotope       = {
            120 : Isotope(
                mass_number   = 120,
                mass          = 119.904026,
                abundance     = 0.0009,
                ),
            122 : Isotope(
                mass_number   = 122,
                mass          = 121.9030558,
                abundance     = 0.0255,
                ),
            123 : Isotope(
                mass_number   = 123,
                mass          = 122.9042711,
                abundance     = 0.0089,
                ),
            124 : Isotope(
                mass_number   = 124,
                mass          = 123.9028188,
                abundance     = 0.0474,
                ),
            125 : Isotope(
                mass_number   = 125,
                mass          = 124.9044241,
                abundance     = 0.0707,
                ),
            126 : Isotope(
                mass_number   = 126,
                mass          = 125.9033049,
                abundance     = 0.1884,
                ),
            128 : Isotope(
                mass_number   = 128,
                mass          = 127.9044615,
                abundance     = 0.3174,
                ),
            130 : Isotope(
                mass_number   = 130,
                mass          = 129.9062229,
                abundance     = 0.3408,
                ),
            },
        ),
    'I': Element(
        number        = 53,
        symbol        = 'I',
        name          = 'Iodine',
        mass          = 126.90447,
        cross_section = 3.81,
        isotope       = {
            127 : Isotope(
                mass_number   = 127,
                mass          = 126.904468,
                abundance     = 1.0,
                ),
            },
        ),
    'Xe': Element(
        number        = 54,
        symbol        = 'Xe',
        name          = 'Xenon',
        mass          = 131.293,
        isotope       = {
            124 : Isotope(
                mass_number   = 124,
                mass          = 123.9058954,
                abundance     = 0.000952,
                ),
            126 : Isotope(
                mass_number   = 126,
                mass          = 125.904268,
                abundance     = 0.00089,
                ),
            128 : Isotope(
                mass_number   = 128,
                mass          = 127.9035305,
                abundance     = 0.019102,
                ),
            129 : Isotope(
                mass_number   = 129,
                mass          = 128.9047799,
                abundance     = 0.264006,
                ),
            130 : Isotope(
                mass_number   = 130,
                mass          = 129.9035089,
                abundance     = 0.04071,
                ),
            131 : Isotope(
                mass_number   = 131,
                mass          = 130.9050828,
                abundance     = 0.212324,
                ),
            132 : Isotope(
                mass_number   = 132,
                mass          = 131.9041546,
                abundance     = 0.269086,
                ),
            134 : Isotope(
                mass_number   = 134,
                mass          = 133.9053945,
                abundance     = 0.104357,
                ),
            136 : Isotope(
                mass_number   = 136,
                mass          = 135.90722,
                abundance     = 0.088573,
                ),
            },
        ),
    'Cs': Element(
        number        = 55,
        symbol        = 'Cs',
        name          = 'Caesium',
        mass          = 132.9054519,
        cross_section = 3.9,
        isotope       = {
            133 : Isotope(
                mass_number   = 133,
                mass          = 132.905447,
                abundance     = 1.0,
                ),
            },
        ),
    'Ba': Element(
        number        = 56,
        symbol        = 'Ba',
        name          = 'Barium',
        mass          = 137.327,
        cross_section = 3.38,
        isotope       = {
            130 : Isotope(
                mass_number   = 130,
                mass          = 129.906311,
                abundance     = 0.00106,
                ),
            132 : Isotope(
                mass_number   = 132,
                mass          = 131.905056,
                abundance     = 0.00101,
                ),
            134 : Isotope(
                mass_number   = 134,
                mass          = 133.904504,
                abundance     = 0.02417,
                ),
            135 : Isotope(
                mass_number   = 135,
                mass          = 134.905684,
                abundance     = 0.06592,
                ),
            136 : Isotope(
                mass_number   = 136,
                mass          = 135.904571,
                abundance     = 0.07854,
                ),
            137 : Isotope(
                mass_number   = 137,
                mass          = 136.905822,
                abundance     = 0.11232,
                ),
            138 : Isotope(
                mass_number   = 138,
                mass          = 137.905242,
                abundance     = 0.71698,
                ),
            },
        ),
    'La': Element(
        number        = 57,
        symbol        = 'La',
        name          = 'Lanthanum',
        mass          = 138.90547,
        cross_section = 9.66,
        isotope       = {
            138 : Isotope(
                mass_number   = 138,
                mass          = 137.907108,
                abundance     = 0.0009,
                ),
            139 : Isotope(
                mass_number   = 139,
                mass          = 138.906349,
                abundance     = 0.9991,
                ),
            },
        ),
    'Ce': Element(
        number        = 58,
        symbol        = 'Ce',
        name          = 'Cerium',
        mass          = 140.116,
        cross_section = 2.94,
        isotope       = {
            136 : Isotope(
                mass_number   = 136,
                mass          = 135.90714,
                abundance     = 0.00185,
                ),
            138 : Isotope(
                mass_number   = 138,
                mass          = 137.905986,
                abundance     = 0.00251,
                ),
            140 : Isotope(
                mass_number   = 140,
                mass          = 139.905435,
                abundance     = 0.8845,
                ),
            142 : Isotope(
                mass_number   = 142,
                mass          = 141.909241,
                abundance     = 0.11114,
                ),
            },
        ),
    'Pr': Element(
        number        = 59,
        symbol        = 'Pr',
        name          = 'Praseodymium',
        mass          = 140.90765,
        cross_section = 2.66,
        isotope       = {
            141 : Isotope(
                mass_number   = 141,
                mass          = 140.907648,
                abundance     = 1.0,
                ),
            },
        ),
    'Nd': Element(
        number        = 60,
        symbol        = 'Nd',
        name          = 'Neodymium',
        mass          = 144.242,
        cross_section = 16.6,
        isotope       = {
            142 : Isotope(
                mass_number   = 142,
                mass          = 141.907719,
                abundance     = 0.272,
                ),
            143 : Isotope(
                mass_number   = 143,
                mass          = 142.90981,
                abundance     = 0.122,
                ),
            144 : Isotope(
                mass_number   = 144,
                mass          = 143.910083,
                abundance     = 0.238,
                ),
            145 : Isotope(
                mass_number   = 145,
                mass          = 144.912569,
                abundance     = 0.083,
                ),
            146 : Isotope(
                mass_number   = 146,
                mass          = 145.913113,
                abundance     = 0.172,
                ),
            148 : Isotope(
                mass_number   = 148,
                mass          = 147.916889,
                abundance     = 0.057,
                ),
            150 : Isotope(
                mass_number   = 150,
                mass          = 149.920887,
                abundance     = 0.056,
                ),
            },
        ),
    'Pm': Element(
        number        = 61,
        symbol        = 'Pm',
        name          = 'Promethium',
        mass          = 145,
        cross_section = 21.3,
        ),
    'Sm': Element(
        number        = 62,
        symbol        = 'Sm',
        name          = 'Samarium',
        mass          = 150.36,
        cross_section = 39.4,
        isotope       = {
            144 : Isotope(
                mass_number   = 144,
                mass          = 143.911996,
                abundance     = 0.0307,
                ),
            147 : Isotope(
                mass_number   = 147,
                mass          = 146.914894,
                abundance     = 0.1499,
                ),
            148 : Isotope(
                mass_number   = 148,
                mass          = 147.914818,
                abundance     = 0.1124,
                ),
            149 : Isotope(
                mass_number   = 149,
                mass          = 148.91718,
                abundance     = 0.1382,
                ),
            150 : Isotope(
                mass_number   = 150,
                mass          = 149.917272,
                abundance     = 0.0738,
                ),
            152 : Isotope(
                mass_number   = 152,
                mass          = 151.919729,
                abundance     = 0.2675,
                ),
            154 : Isotope(
                mass_number   = 154,
                mass          = 153.922206,
                abundance     = 0.2275,
                ),
            },
        ),
    'Eu': Element(
        number        = 63,
        symbol        = 'Eu',
        name          = 'Europium',
        mass          = 151.964,
        cross_section = 9.2,
        isotope       = {
            151 : Isotope(
                mass_number   = 151,
                mass          = 150.919846,
                abundance     = 0.4781,
                ),
            153 : Isotope(
                mass_number   = 153,
                mass          = 152.921227,
                abundance     = 0.5219,
                ),
            },
        ),
    'Gd': Element(
        number        = 64,
        symbol        = 'Gd',
        name          = 'Gadolinium',
        mass          = 157.25,
        cross_section = 180.0,
        isotope       = {
            152 : Isotope(
                mass_number   = 152,
                mass          = 151.919789,
                abundance     = 0.002,
                ),
            154 : Isotope(
                mass_number   = 154,
                mass          = 153.920862,
                abundance     = 0.0218,
                ),
            155 : Isotope(
                mass_number   = 155,
                mass          = 154.922619,
                abundance     = 0.148,
                ),
            156 : Isotope(
                mass_number   = 156,
                mass          = 155.92212,
                abundance     = 0.2047,
                ),
            157 : Isotope(
                mass_number   = 157,
                mass          = 156.923957,
                abundance     = 0.1565,
                ),
            158 : Isotope(
                mass_number   = 158,
                mass          = 157.924101,
                abundance     = 0.2484,
                ),
            160 : Isotope(
                mass_number   = 160,
                mass          = 159.927051,
                abundance     = 0.2186,
                ),
            },
        ),
    'Tb': Element(
        number        = 65,
        symbol        = 'Tb',
        name          = 'Terbium',
        mass          = 158.92535,
        cross_section = 6.84,
        isotope       = {
            159 : Isotope(
                mass_number   = 159,
                mass          = 158.925343,
                abundance     = 1.0,
                ),
            },
        ),
    'Dy': Element(
        number        = 66,
        symbol        = 'Dy',
        name          = 'Dysprosium',
        mass          = 162.5,
        cross_section = 90.3,
        isotope       = {
            156 : Isotope(
                mass_number   = 156,
                mass          = 155.924278,
                abundance     = 0.00056,
                ),
            158 : Isotope(
                mass_number   = 158,
                mass          = 157.924405,
                abundance     = 0.00095,
                ),
            160 : Isotope(
                mass_number   = 160,
                mass          = 159.925194,
                abundance     = 0.02329,
                ),
            161 : Isotope(
                mass_number   = 161,
                mass          = 160.92693,
                abundance     = 0.18889,
                ),
            162 : Isotope(
                mass_number   = 162,
                mass          = 161.926795,
                abundance     = 0.25475,
                ),
            163 : Isotope(
                mass_number   = 163,
                mass          = 162.928728,
                abundance     = 0.24896,
                ),
            164 : Isotope(
                mass_number   = 164,
                mass          = 163.929171,
                abundance     = 0.2826,
                ),
            },
        ),
    'Ho': Element(
        number        = 67,
        symbol        = 'Ho',
        name          = 'Holmium',
        mass          = 164.93032,
        cross_section = 8.42,
        isotope       = {
            165 : Isotope(
                mass_number   = 165,
                mass          = 164.930319,
                abundance     = 1.0,
                ),
            },
        ),
    'Er': Element(
        number        = 68,
        symbol        = 'Er',
        name          = 'Erbium',
        mass          = 167.259,
        cross_section = 8.7,
        isotope       = {
            162 : Isotope(
                mass_number   = 162,
                mass          = 161.928775,
                abundance     = 0.00139,
                ),
            164 : Isotope(
                mass_number   = 164,
                mass          = 163.929197,
                abundance     = 0.01601,
                ),
            166 : Isotope(
                mass_number   = 166,
                mass          = 165.93029,
                abundance     = 0.33503,
                ),
            167 : Isotope(
                mass_number   = 167,
                mass          = 166.932046,
                abundance     = 0.22869,
                ),
            168 : Isotope(
                mass_number   = 168,
                mass          = 167.932368,
                abundance     = 0.26978,
                ),
            170 : Isotope(
                mass_number   = 170,
                mass          = 169.935461,
                abundance     = 0.1491,
                ),
            },
        ),
    'Tm': Element(
        number        = 69,
        symbol        = 'Tm',
        name          = 'Thulium',
        mass          = 168.93421,
        cross_section = 6.38,
        isotope       = {
            169 : Isotope(
                mass_number   = 169,
                mass          = 168.934211,
                abundance     = 1.0,
                ),
            },
        ),
    'Yb': Element(
        number        = 70,
        symbol        = 'Yb',
        name          = 'Ytterbium',
        mass          = 173.054,
        cross_section = 23.4,
        isotope       = {
            168 : Isotope(
                mass_number   = 168,
                mass          = 167.933895,
                abundance     = 0.0013,
                ),
            170 : Isotope(
                mass_number   = 170,
                mass          = 169.934759,
                abundance     = 0.0304,
                ),
            171 : Isotope(
                mass_number   = 171,
                mass          = 170.936323,
                abundance     = 0.1428,
                ),
            172 : Isotope(
                mass_number   = 172,
                mass          = 171.936378,
                abundance     = 0.2183,
                ),
            173 : Isotope(
                mass_number   = 173,
                mass          = 172.938207,
                abundance     = 0.1613,
                ),
            174 : Isotope(
                mass_number   = 174,
                mass          = 173.938858,
                abundance     = 0.3183,
                ),
            176 : Isotope(
                mass_number   = 176,
                mass          = 175.942569,
                abundance     = 0.1276,
                ),
            },
        ),
    'Lu': Element(
        number        = 71,
        symbol        = 'Lu',
        name          = 'Lutetium',
        mass          = 174.9668,
        cross_section = 7.2,
        isotope       = {
            175 : Isotope(
                mass_number   = 175,
                mass          = 174.9407682,
                abundance     = 0.9741,
                ),
            176 : Isotope(
                mass_number   = 176,
                mass          = 175.9426827,
                abundance     = 0.0259,
                ),
            },
        ),
    'Hf': Element(
        number        = 72,
        symbol        = 'Hf',
        name          = 'Hafnium',
        mass          = 178.49,
        cross_section = 10.2,
        isotope       = {
            174 : Isotope(
                mass_number   = 174,
                mass          = 173.940042,
                abundance     = 0.0016,
                ),
            176 : Isotope(
                mass_number   = 176,
                mass          = 175.941403,
                abundance     = 0.0526,
                ),
            177 : Isotope(
                mass_number   = 177,
                mass          = 176.9432204,
                abundance     = 0.186,
                ),
            178 : Isotope(
                mass_number   = 178,
                mass          = 177.9436981,
                abundance     = 0.2728,
                ),
            179 : Isotope(
                mass_number   = 179,
                mass          = 178.9458154,
                abundance     = 0.1362,
                ),
            180 : Isotope(
                mass_number   = 180,
                mass          = 179.9465488,
                abundance     = 0.3508,
                ),
            },
        ),
    'Ta': Element(
        number        = 73,
        symbol        = 'Ta',
        name          = 'Tantalum',
        mass          = 180.94788,
        cross_section = 6.01,
        isotope       = {
            180 : Isotope(
                mass_number   = 180,
                mass          = 179.947466,
                abundance     = 0.00012,
                ),
            181 : Isotope(
                mass_number   = 181,
                mass          = 180.947996,
                abundance     = 0.99988,
                ),
            },
        ),
    'W': Element(
        number        = 74,
        symbol        = 'W',
        name          = 'Tungsten',
        mass          = 183.84,
        isotope       = {
            180 : Isotope(
                mass_number   = 180,
                mass          = 179.946706,
                abundance     = 0.0012,
                ),
            182 : Isotope(
                mass_number   = 182,
                mass          = 181.948205,
                abundance     = 0.265,
                ),
            183 : Isotope(
                mass_number   = 183,
                mass          = 182.9502242,
                abundance     = 0.1431,
                ),
            184 : Isotope(
                mass_number   = 184,
                mass          = 183.9509323,
                abundance     = 0.3064,
                ),
            186 : Isotope(
                mass_number   = 186,
                mass          = 185.95436,
                abundance     = 0.2843,
                ),
            },
        ),
    'Re': Element(
        number        = 75,
        symbol        = 'Re',
        name          = 'Rhenium',
        mass          = 186.207,
        cross_section = 11.5,
        isotope       = {
            185 : Isotope(
                mass_number   = 185,
                mass          = 184.952955,
                abundance     = 0.374,
                ),
            187 : Isotope(
                mass_number   = 187,
                mass          = 186.9557505,
                abundance     = 0.626,
                ),
            },
        ),
    'Os': Element(
        number        = 76,
        symbol        = 'Os',
        name          = 'Osmium',
        mass          = 190.23,
        cross_section = 14.7,
        isotope       = {
            184 : Isotope(
                mass_number   = 184,
                mass          = 183.952491,
                abundance     = 0.0002,
                ),
            186 : Isotope(
                mass_number   = 186,
                mass          = 185.953838,
                abundance     = 0.0159,
                ),
            187 : Isotope(
                mass_number   = 187,
                mass          = 186.9557476,
                abundance     = 0.0196,
                ),
            188 : Isotope(
                mass_number   = 188,
                mass          = 187.9558357,
                abundance     = 0.1324,
                ),
            189 : Isotope(
                mass_number   = 189,
                mass          = 188.958145,
                abundance     = 0.1615,
                ),
            190 : Isotope(
                mass_number   = 190,
                mass          = 189.958445,
                abundance     = 0.2626,
                ),
            192 : Isotope(
                mass_number   = 192,
                mass          = 191.961479,
                abundance     = 0.4078,
                ),
            },
        ),
    'Ir': Element(
        number        = 77,
        symbol        = 'Ir',
        name          = 'Iridium',
        mass          = 192.217,
        cross_section = 14.0,
        isotope       = {
            191 : Isotope(
                mass_number   = 191,
                mass          = 190.960591,
                abundance     = 0.373,
                ),
            193 : Isotope(
                mass_number   = 193,
                mass          = 192.962923,
                abundance     = 0.627,
                ),
            },
        ),
    'Pt': Element(
        number        = 78,
        symbol        = 'Pt',
        name          = 'Platinum',
        mass          = 195.084,
        cross_section = 11.71,
        isotope       = {
            190 : Isotope(
                mass_number   = 190,
                mass          = 189.95993,
                abundance     = 0.00014,
                ),
            192 : Isotope(
                mass_number   = 192,
                mass          = 191.961035,
                abundance     = 0.00782,
                ),
            194 : Isotope(
                mass_number   = 194,
                mass          = 193.962663,
                abundance     = 0.32967,
                ),
            195 : Isotope(
                mass_number   = 195,
                mass          = 194.964774,
                abundance     = 0.33832,
                ),
            196 : Isotope(
                mass_number   = 196,
                mass          = 195.964934,
                abundance     = 0.25242,
                ),
            198 : Isotope(
                mass_number   = 198,
                mass          = 197.967875,
                abundance     = 0.07163,
                ),
            },
        ),
    'Au': Element(
        number        = 79,
        symbol        = 'Au',
        name          = 'Gold',
        mass          = 196.966569,
        cross_section = 7.75,
        isotope       = {
            197 : Isotope(
                mass_number   = 197,
                mass          = 196.966551,
                abundance     = 1.0,
                ),
            },
        ),
    'Hg': Element(
        number        = 80,
        symbol        = 'Hg',
        name          = 'Mercury',
        mass          = 200.59,
        cross_section = 26.8,
        isotope       = {
            196 : Isotope(
                mass_number   = 196,
                mass          = 195.965814,
                abundance     = 0.0015,
                ),
            198 : Isotope(
                mass_number   = 198,
                mass          = 197.966752,
                abundance     = 0.0997,
                ),
            199 : Isotope(
                mass_number   = 199,
                mass          = 198.968262,
                abundance     = 0.1687,
                ),
            200 : Isotope(
                mass_number   = 200,
                mass          = 199.968309,
                abundance     = 0.231,
                ),
            201 : Isotope(
                mass_number   = 201,
                mass          = 200.970285,
                abundance     = 0.1318,
                ),
            202 : Isotope(
                mass_number   = 202,
                mass          = 201.970625,
                abundance     = 0.2986,
                ),
            204 : Isotope(
                mass_number   = 204,
                mass          = 203.973475,
                abundance     = 0.0687,
                ),
            },
        ),
    'Tl': Element(
        number        = 81,
        symbol        = 'Tl',
        name          = 'Thallium',
        mass          = 204.3833,
        cross_section = 9.89,
        isotope       = {
            203 : Isotope(
                mass_number   = 203,
                mass          = 202.972329,
                abundance     = 0.2952,
                ),
            205 : Isotope(
                mass_number   = 205,
                mass          = 204.974412,
                abundance     = 0.7048,
                ),
            },
        ),
    'Pb': Element(
        number        = 82,
        symbol        = 'Pb',
        name          = 'Lead',
        mass          = 207.2,
        cross_section = 11.118,
        isotope       = {
            204 : Isotope(
                mass_number   = 204,
                mass          = 203.973028,
                abundance     = 0.014,
                ),
            206 : Isotope(
                mass_number   = 206,
                mass          = 205.974449,
                abundance     = 0.241,
                ),
            207 : Isotope(
                mass_number   = 207,
                mass          = 206.97588,
                abundance     = 0.221,
                ),
            208 : Isotope(
                mass_number   = 208,
                mass          = 207.976636,
                abundance     = 0.524,
                ),
            },
        ),
    'Bi': Element(
        number        = 83,
        symbol        = 'Bi',
        name          = 'Bismuth',
        mass          = 208.9804,
        cross_section = 9.156,
        isotope       = {
            209 : Isotope(
                mass_number   = 209,
                mass          = 208.980384,
                abundance     = 1.0,
                ),
            },
        ),
    'Po': Element(
        number        = 84,
        symbol        = 'Po',
        name          = 'Polonium',
        ),
    'At': Element(
        number        = 85,
        symbol        = 'At',
        name          = 'Astatine',
        ),
    'Rn': Element(
        number        = 86,
        symbol        = 'Rn',
        name          = 'Radon',
        ),
    'Fr': Element(
        number        = 87,
        symbol        = 'Fr',
        name          = 'Francium',
        ),
    'Ra': Element(
        number        = 88,
        symbol        = 'Ra',
        name          = 'Radium',
        cross_section = 13.0,
        ),
    'Ac': Element(
        number        = 89,
        symbol        = 'Ac',
        name          = 'Actinium',
        mass          = 227,
        ),
    'Th': Element(
        number        = 90,
        symbol        = 'Th',
        name          = 'Thorium',
        mass          = 232.03806,
        cross_section = 13.36,
        isotope       = {
            232 : Isotope(
                mass_number   = 232,
                mass          = 232.0380495,
                abundance     = 1.0,
                ),
            },
        ),
    'Pa': Element(
        number        = 91,
        symbol        = 'Pa',
        name          = 'Protactinium',
        mass          = 231.03588,
        cross_section = 10.5,
        isotope       = {
            231 : Isotope(
                mass_number   = 231,
                mass          = 231.03588,
                abundance     = 1.0,
                ),
            },
        ),
    'U': Element(
        number        = 92,
        symbol        = 'U',
        name          = 'Uranium',
        mass          = 238.02891,
        isotope       = {
            234 : Isotope(
                mass_number   = 234,
                mass          = 234.0409447,
                abundance     = 5.4e-05,
                ),
            235 : Isotope(
                mass_number   = 235,
                mass          = 235.0439222,
                abundance     = 0.007204,
                ),
            238 : Isotope(
                mass_number   = 238,
                mass          = 238.0507835,
                abundance     = 0.992742,
                ),
            },
        ),
    'Np': Element(
        number        = 93,
        symbol        = 'Np',
        name          = 'Neptunium',
        mass          = 237,
        cross_section = 14.5,
        ),
    'Pu': Element(
        number        = 94,
        symbol        = 'Pu',
        name          = 'Plutonium',
        ),
    'Am': Element(
        number        = 95,
        symbol        = 'Am',
        name          = 'Americium',
        cross_section = 9.0,
        ),
    'Cm': Element(
        number        = 96,
        symbol        = 'Cm',
        name          = 'Curium',
        ),
    'Bk': Element(
        number        = 97,
        symbol        = 'Bk',
        name          = 'Berkelium',
        ),
    'Cf': Element(
        number        = 98,
        symbol        = 'Cf',
        name          = 'Californium',
        ),
    'Es': Element(
        number        = 99,
        symbol        = 'Es',
        name          = 'Einsteinium',
        ),
    'Fm': Element(
        number        = 100,
        symbol        = 'Fm',
        name          = 'Fermium',
        ),
    'Md': Element(
        number        = 101,
        symbol        = 'Md',
        name          = 'Mendelevium',
        ),
    'No': Element(
        number        = 102,
        symbol        = 'No',
        name          = 'Nobelium',
        ),
    'Lr': Element(
        number        = 103,
        symbol        = 'Lr',
        name          = 'Lawrencium',
        ),
    'Rf': Element(
        number        = 104,
        symbol        = 'Rf',
        name          = 'Rutherfordium',
        ),
    'Db': Element(
        number        = 105,
        symbol        = 'Db',
        name          = 'Dubnium',
        ),
    'Sg': Element(
        number        = 106,
        symbol        = 'Sg',
        name          = 'Seaborgium',
        ),
    'Bh': Element(
        number        = 107,
        symbol        = 'Bh',
        name          = 'Bohrium',
        ),
    'Hs': Element(
        number        = 108,
        symbol        = 'Hs',
        name          = 'Hassium',
        ),
    'Mt': Element(
        number        = 109,
        symbol        = 'Mt',
        name          = 'Meitnerium',
        ),
    'Ds': Element(
        number        = 110,
        symbol        = 'Ds',
        name          = 'Darmstadtium',
        ),
    'Rg': Element(
        number        = 111,
        symbol        = 'Rg',
        name          = 'Roentgenium',
        ),
    'Cn': Element(
        number        = 112,
        symbol        = 'Cn',
        name          = 'Copernicium',
        ),
    'Uut': Element(
        number        = 113,
        symbol        = 'Uut',
        name          = 'Ununtrium',
        ),
    'Uuq': Element(
        number        = 114,
        symbol        = 'Uuq',
        name          = 'Ununquadium',
        ),
    'Uup': Element(
        number        = 115,
        symbol        = 'Uup',
        name          = 'Ununpentium',
        ),
    'Uuh': Element(
        number        = 116,
        symbol        = 'Uuh',
        name          = 'Ununhexium',
        ),
    'Uus': Element(
        number        = 117,
        symbol        = 'Uus',
        name          = 'Ununseptium',
        ),
    'Uuo': Element(
        number        = 118,
        symbol        = 'Uuo',
        name          = 'Ununoctium',
        ),
}
