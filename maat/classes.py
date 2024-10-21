'''
This module contains the core classes and their functions.
'''


from .constants import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from copy import deepcopy
import os


class ScaleRange:
    '''
    The ScaleRange object is used to handle the normalization of the data inside the specified x-range,
    to the same heigth as in the specified `index` dataset (the first one by default).

    Custom heights can be normalized with `ymin` and `ymax`, overriding the x-values.
    For example, you may want to normalize with respect to the height of a given peak that overlaps with another.
    Those peaks may have ymin values of 2 and 3, and ymax values of 50 and 60 respectively. In that case:
    ```python
    spectra.scale_range = ScaleRange(index=0, ymin=[2, 3], ymax=[50, 60])
    ```

    To normalize when plotting with `maat.plot.spectra(Spectra)`, remember to set `Plotting.normalize=True`.
    When normalizing the plot, all datasets are fitted inside the plotting window, scaling over the entire data range into view.
    To override this behaviour and expand over the given range to fill the plot window, you can set `ScaleRange.zoom=True`.
    This zoom setting can also be enabled without normalizing the plot, resulting in a zoom over the given range
    so that the `index` dataset fits the full plotting window, scaling the rest of the set accordingly.
    '''
    def __init__(self,
                 index:int=0,
                 xmin:float=None,
                 xmax:float=None,
                 ymin:list=None,
                 ymax:list=None,
                 zoom:bool=False,
                 ):
        '''All values can be set when initializing the ScaleRange object.'''
        self.index = index
        '''Index of the dataframe to use as reference.'''
        self.xmin = xmin
        '''Minimum x-value to start normalizing the plots.'''
        self.xmax = xmax
        '''Maximum x-value to normalize the plots.'''
        self.ymin = ymin
        '''Minimum y-value to normalize the plots.'''
        self.ymax = ymax
        '''Minimum y-value to normalize the plots.
        If `plotting.normalize=True`, the plots are normalized according to the y-values provided.
        '''
        self.zoom = zoom
        '''
        Used when plotting with `maat.plot.spectra()`.
        If true, the data inside the range is scaled up to fit the entire plotting window.
        '''

    def set_x(self, xmin:float=None, xmax:float=None):
        '''Override with an horizontal range.'''
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = None
        self.ymax = None
        return self

    def set_y(self, ymin:list=None, ymax:list=None):
        '''Override with a vertical range.'''
        self.xmin = None
        self.xmax = None
        self.ymin = ymin
        self.ymax = ymax
        return self


class Plotting:
    '''Plotting options. To be used inside the `Spectra` class. Read by `maat.plot.spectra()`.'''
    def __init__(self,
                 low_xlim=0,
                 top_xlim=50,
                 low_ylim=None,
                 top_ylim=None,
                 add_top:float=0,
                 add_low:float=0,
                 hline:list=None,
                 hline_error:list=None,
                 vline:list=None,
                 vline_error:list=None,
                 figsize:tuple=None,
                 log_xscale:bool=False,
                 offset=True,
                 normalize:bool=False,
                 show_yticks:bool=False,
                 legend=None,
                 legend_title:str=None,
                 legend_size='medium',
                 ):
        '''Default values can be overwritten when initializing the Plotting object.'''
        self.low_xlim = low_xlim
        '''Minimum x-value to plot.'''
        self.top_xlim = top_xlim
        '''Maximum x-value to plot.'''
        self.low_ylim = low_ylim
        '''Minimum y-value to plot.'''
        self.top_ylim = top_ylim
        '''Maximum y-value to plot.'''
        self.add_top = add_top
        '''Add a given separation on top of the plot.'''
        self.add_low = add_low
        '''Add a given separation on the bottom of the plot.'''
        self.hline = hline
        '''TODO: implement horizontal lines'''
        self.hline_error = hline_error
        '''TODO: implement error for horizontal lines'''
        if vline is not None and not isinstance(vline, list):
            vline = [vline]
        self.vline = vline
        '''List of vertical lines to plot.'''
        if vline_error is not None and not isinstance(vline_error, list):
            vline_error = [vline_error]
        self.vline_error = vline_error
        '''
        If `vline_error` is not `None`, it will plot a shaded area of the specified width around the vertical lines.
        It can be an array of the same length as `vline`, or a single value to be applied to all.
        '''
        self.figsize = figsize
        '''Tuple with the figure size, as in matplotlib.'''
        self.log_xscale = log_xscale
        '''If true, plot the x-axis in logarithmic scale.'''
        self.offset = offset
        '''If `True`, the plots will be separated automatically. It can be set to a float, to offset the plots by a given value.'''
        self.normalize = normalize
        '''`True` or `'y'` or `'Y'` to normalize the heights, `'area'` or `'a'` or `'A'` to normalize the areas.'''
        self.show_yticks = show_yticks
        '''Show or not the yticks on the plot.'''
        if not isinstance(legend, list) and legend is not None and legend != False:
            legend = [legend]
        self.legend = legend
        '''
        If `None`, the filenames will be used as legend. Can be a bool to show or hide the plot legend.
        It can also be an array containing the strings to display. Elements set to `False` will not be displayed.
        '''
        self.legend_title = legend_title
        '''Title of the legend.'''
        self.legend_size = legend_size
        '''Size of the legend, as in matplotlib.'''


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
                 plotting:Plotting=Plotting()
                 ):
        '''All values can be set when initializing the Spectra object.'''

        self.type = None
        '''Type of the spectra: `INS`, `ATR`, or `RAMAN`.'''
        self.title = title
        '''Title of the plot.'''
        self.save_as = save_as
        '''Filename to save the plot.'''
        self.filename = None
        '''List containing the filenames with the spectral data.'''
        self.dataframe = None
        '''List containing the pandas dataframes with the spectral data.'''
        self.units = None
        '''Target units of the spectral data.'''
        self.units_in = None
        '''Input units of the spectral data.'''
        self.scale_range = scale_range
        '''`ScaleRange` object, used to set the normalization parameters.'''
        self.plotting = plotting
        '''`Plotting` object, used to set the plotting options.'''

        self = self._set_type(type)
        self = self._set_dataframe(filename, dataframe)
        self = self.set_units(units, units_in)

    def _set_type(self, type):
        '''Set and normalize the type of the spectra: `INS`, `ATR`, or `RAMAN`.'''
        if type in spectra_keys['INS']:
            self.type = 'INS'
        elif type in spectra_keys['ATR']:
            self.type = 'ATR'
        elif type in spectra_keys['RAMAN']:
            self.type = 'RAMAN'
        else:
            self.type = type
        return self

    def _set_dataframe(self, filename, dataframe):
        '''Set the dataframes, from the given files or dataframes.'''
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
            self.dataframe = [self._read_dataframe(file) for file in self.filename]
        return self

    def _read_dataframe(self, filename):
        '''Read the dataframes from the files.'''
        root = os.getcwd()
        file = os.path.join(root, filename)
        df = pd.read_csv(file, comment='#')
        df = df.sort_values(by=df.columns[0]) # Sort the data by energy

        print(f'\nNew dataframe from {file}')
        print(df.head(),'\n')
        return df

    def set_units(
            self,
            units,
            units_in=None,
            default_unit='cm-1',
            ):
        ''''Method to change units. ALWAYS use this method to do that.'''

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
        '''
        All values can be set when initializing the Material object. However, it is recommended
        to only set the atoms and the grams (and the name), and calculate the rest with `Material.set()`.
        '''
        self.atoms = atoms
        '''Dict of atoms in the material.'''
        self.name = name
        '''Name of the material.'''
        self.grams = grams
        '''Mass, in grams.'''
        self.grams_error = grams_error
        '''Error of the measured mass in grams. Set automatically with `self.set_mass()`.'''
        self.mols = mols
        '''Number of moles. Set automatically with `self.set_mass()`.'''
        self.mols_error = mols_error
        '''Error of the number of moles. Set automatically with `self.set_mass()`.'''
        self.molar_mass = molar_mass
        '''Molar mass of the material, in mol/g. Calculated automatically with `self.set_mass()`.'''
        self.cross_section = cross_section
        '''Cross section of the material, in barns. Calculated automatically with `self.set_cross_section()`.'''

    def _set_grams_error(self):
        '''Set the error in grams, based on the number of decimal places.'''
        if self.grams is None:
            return
        decimal_accuracy = len(str(self.grams).split('.')[1])
        # Calculate the error in grams
        self.grams_error = 10**(-decimal_accuracy)

    def _set_mass(self):
        '''Set the molar mass of the material.\n
        If `self.grams` is not `None`, the number of moles will be calculated and overwritten.'''
        material_grams_per_mol = 0.0
        for key in self.atoms:
            material_grams_per_mol += self.atoms[key] * mass[key]
        self.molar_mass = material_grams_per_mol
        if self.grams is not None:
            self._set_grams_error()
            self.mols = self.grams / material_grams_per_mol
            self.mols_error = self.mols * np.sqrt((self.grams_error / self.grams)**2)
    
    def _set_cross_section(self):
        '''Set the cross section of the material, based on the atoms dict.'''
        total_cross_section = 0.0
        for key in self.atoms:
            total_cross_section += self.atoms[key] * cross_section[key]
        self.cross_section = total_cross_section

    def set(self):
        '''Set the molar mass, cross section and errors of the material.'''
        self._set_mass()
        self._set_cross_section()

    def print(self):
        '''Print a summary with the material information.'''
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

