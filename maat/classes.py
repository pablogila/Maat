from .constants import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from copy import deepcopy
import os


'''
This module contains the core classes and their functions.
'''


class ScaleRange:
    '''
    If `plotting.normalize=True`, the data will be normalized inside the specified range.
    The vertical scale of the plots is still determined by the full data range, unless
    `plotting.zoom_range=True`, so that the data is scaled inside the range.
    If only `plotting.zoom_range=True`, with `plotting.normalize=False`, only the `index` dataset
    will be scaled to fit the range, and the rest of the datasets will be scaled accordingly. 
    '''
    def __init__(self,
                 index:int=0,
                 xmin:float=None,
                 xmax:float=None,
                 ymin:list=None,
                 ymax:list=None,
                 ):
        self.index = index
        '''Index of the dataframe to use as reference.'''
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        '''If `plotting.normalize=True`, normalize the plots according to the y-values provided.'''
    def x(self, xmin:float=None, xmax:float=None):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = None
        self.ymax = None
        return self
    def y(self, ymin:list=None, ymax:list=None):
        self.xmin = None
        self.xmax = None
        self.ymin = ymin
        self.ymax = ymax
        return self


class Plotting:
    '''Plotting options. To be used inside the `Spectra` class.'''
    def __init__(self,
                 low_xlim=0,
                 top_xlim=50,
                 low_ylim=None,
                 top_ylim=None,
                 add_top_ylim:float=0,
                 add_low_ylim:float=0,
                 hline:list=None,
                 hline_error:list=None,
                 vline:list=None,
                 vline_error:list=None,
                 figsize:tuple=None,
                 log_xscale:bool=False,
                 offset=True,
                 zoom_range:bool=False,
                 normalize:bool=False,
                 show_yticks:bool=False,
                 legend=None,
                 legend_title:str=None,
                 legend_size='medium',
                 ):
        self.low_xlim = low_xlim
        self.top_xlim = top_xlim
        self.low_ylim = low_ylim
        self.top_ylim = top_ylim
        self.add_top_ylim = add_top_ylim
        self.add_low_ylim = add_low_ylim
        self.hline = hline
        self.hline_error = hline_error
        if vline is not None and not isinstance(vline, list):
            vline = [vline]
        self.vline = vline
        if vline_error is not None and not isinstance(vline_error, list):
            vline_error = [vline_error]
        self.vline_error = vline_error
        self.figsize = figsize
        self.log_xscale = log_xscale
        self.offset = offset
        self.zoom_range = zoom_range
        self.normalize = normalize
        '''`True` or `y` or `Y` to normalize the heights, `area` or `a` or `A` to normalize the areas.'''
        self.show_yticks = show_yticks
        if not isinstance(legend, list) and legend is not None and legend != False:
            legend = [legend]
        self.legend = legend
        self.legend_title = legend_title
        self.legend_size = legend_size


class Spectra:
    def __init__(self,
                 type:str=None,
                 title:str=None,
                 save_as:str=None,
                 filename=None,
                 dataframe=None,
                 units=None,
                 units_in=None,
                 scale_range:ScaleRange=ScaleRange(),
                 plotting:Plotting=Plotting(),
                 atoms:dict=None,
                 atoms_ref:dict=None,
                 ):
        self.title = title
        self.save_as = save_as
        self.scale_range = scale_range
        self.plotting = plotting
        self.atoms = atoms
        '''Dict of atoms in the material'''
        self.atoms_ref = atoms_ref
        ''''Dict of atoms used as reference'''
        self = self.set_type(type)
        self = self.set_dataframe(filename, dataframe)
        self.units = None
        self = self.set_units(units, units_in)

    def set_type(self, type):
        if type in spectra_keys['INS']:
            self.type = 'INS'
        elif type in spectra_keys['ATR']:
            self.type = 'ATR'
        elif type in spectra_keys['RAMAN']:
            self.type = 'RAMAN'
        else:
            self.type = type
        return self

    def set_dataframe(self, filename, dataframe):
        if isinstance(filename, list):
            self.filename = filename
        elif isinstance(filename, str):
            self.filename = [filename]
        else:
            self.filename = []

        if isinstance(dataframe, pd.DataFrame):
            self.dataframe = [dataframe]
        elif isinstance(dataframe, list) and isinstance(dataframe[0], pd.DataFrame):
            self.dataframe = dataframe
        else:
            self.dataframe = [self.read_dataframe(file) for file in self.filename]
        return self

    def set_units(
            self,
            units,
            units_in=None,
            default_unit='cm-1',
            ):
        ''''ALWAYS use this method to change units.'''

        mev = 'meV'
        cm = 'cm-1'
        unit_format={
                mev: ['mev', 'meV', 'MEV'],
                cm: ['cm', 'CM', 'cm-1', 'cm^-1'],
            }

        if self.units is not None:
            units_in = deepcopy(self.units)
            self.units = units
        elif units is not None:
            units_in = units_in
            self.units = deepcopy(units)
        elif units is None and units_in is None:
            units_in = None
            self.units = default_unit
        elif units is None and units_in is not None:
            units_in = None
            self.units = deepcopy(units_in)

        if isinstance(units_in, list):
            for i, unit_in in enumerate(units_in):
                for key, value in unit_format.items():
                    if unit_in in value:
                        units_in[i] = key
                        break
            if len(units_in) == 1:
                units_in = units_in * len(self.filename)
            elif len(units_in) != len(self.filename):
                raise ValueError("units_in must be a list of the same length as filenames.")

        if isinstance(units_in, str):
            for key, value in unit_format.items():
                if units_in in value:
                    units_in = key
                    break
            units_in = [units_in] * len(self.filename)
        
        if isinstance(self.units, list):
            for i, unit in enumerate(self.units):
                for key, value in unit_format.items():
                    if unit in value:
                        self.units[i] = key
                        break
            if len(self.units) == 1:
                self.units = self.units * len(self.filename)
            elif len(self.units) != len(self.filename):
                raise ValueError("units_in must be a list of the same length as filenames.")

        if isinstance(self.units, str):
            for key, value in unit_format.items():
                if self.units in value:
                    self.units = key
                    break
            self.units = [self.units] * len(self.filename)
        
        if units_in is None:
            return self
        # Otherwise, convert the dataframes
        if len(self.units) != len(units_in):
            raise ValueError("Units len mismatching.")
        for i, unit in enumerate(self.units):
            if unit == units_in[i]:
                continue
            if unit == mev and units_in[i] == cm:
                self.dataframe[i][self.dataframe[i].columns[0]] = self.dataframe[i][self.dataframe[i].columns[0]] * cm_to_meV
            elif unit == cm and units_in[i] == mev:
                self.dataframe[i][self.dataframe[i].columns[0]] = self.dataframe[i][self.dataframe[i].columns[0]] * meV_to_cm
            else:
                raise ValueError(f"Unit conversion error between '{unit}' and '{units_in[i]}'")

        # Rename dataframe columns
        E_units = None
        for i, df in enumerate(self.dataframe):
            if self.units[i] == mev:
                E_units = 'meV'
            elif self.units[i] == cm:
                E_units = 'cm-1'
            else:
                E_units = self.units[i]

            if self.type == 'INS':
                if self.dataframe[i].shape[1] == 3:
                    self.dataframe[i].columns = [f'Energy transfer / {E_units}', 'S(Q,E)', 'Error']
                else:
                    self.dataframe[i].columns = [f'Energy transfer / {E_units}', 'S(Q,E)']
            elif self.type == 'ATR':
                self.dataframe[i].columns = [f'Wavenumber / {E_units}', 'Absorbance']
            elif self.type == 'RAMAN':
                self.dataframe[i].columns = [f'Raman shift / {E_units}', 'Counts']

        return self

    def read_dataframe(self, filename):
        root = os.getcwd()
        file = os.path.join(root, filename)
        df = pd.read_csv(file, comment='#')
        df = df.sort_values(by=df.columns[0]) # Sort the data by energy

        print(f'\nNew dataframe from {file}')
        print(df.head(),'\n')
        return df


class Material:
    '''Material class. To play around with different material compositions.'''
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

