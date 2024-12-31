'''
## Description
This module contains common classes and their functions, used to load and manipulate data.
Any class can be instantiated directly: for example, to create a new
`Spectra` class for your data, you just need to call `maat.Spectra(options)` as described below:
```python
import maat as mt
ins = mt.Spectra(
    # Options here
    )
```

## Index
- `Spectra`. Used to load and process spectral data.
- `Plotting`. Stores plotting options. Used inside `Spectra.plotting`.
- `ScaleRange`. Handles data normalization inside the specified range of values. Used inside `Spectra.scale_range`.
- `Material`. Used to store and calculate material parameters, such as molar masses and cross sections.

---
'''


from . import alias
from .constants import *
from .elements import atom
from . import atoms
import numpy as np
import pandas as pd
from copy import deepcopy
import os


class Plotting:
    '''
    Stores plotting options.
    Read by `maat.plot.spectra(Spectra)`.
    '''
    def __init__(
            self,
            title:str=None,
            xlim=None,
            ylim=None,
            margins=None,
            offset=True,
            normalize:bool=False,
            vline:list=None,
            vline_error:list=None,
            figsize:tuple=None,
            log_xscale:bool=False,
            show_yticks:bool=False,
            xlabel:str=None,
            ylabel:str=None,
            legend=None,
            legend_title:str=None,
            legend_size='medium',
            legend_loc='best',
        ):
        '''Default values can be overwritten when initializing the Plotting object.'''
        self.title = title
        '''Title of the plot. Set it to an empty string to remove the title.'''
        self.xlim = self._set_limits(xlim)
        '''List with the x-limits of the plot, as in `[xlim_low, xlim_top]`.'''
        self.ylim = self._set_limits(ylim)
        '''List with the y-limits of the plot, as in `[ylim_low, ylim_top]`.'''
        self.margins = self._set_limits(margins)
        '''List with additional margins at the bottom and top of the plot, as in `[low_margin, top_margin]`.'''
        self.offset = offset
        '''
        If `True`, the plots will be separated automatically.
        It can be set to a float, to equally offset the plots by a given value.
        '''
        self.normalize = normalize
        '''
        Normalize or not the plotted spectra.
        `True` or `'y'` or `'Y'` to normalize the heights, `'area'` or `'a'` or `'A'` to normalize the areas.
        '''
        if vline is not None and not isinstance(vline, list):
            vline = [vline]
        self.vline = vline
        '''Vertical line/s to plot. Can be an int or float with the x-position, or a list with several ones.'''
        if vline_error is not None and not isinstance(vline_error, list):
            vline_error = [vline_error]
        self.vline_error = vline_error
        '''
        If not `None`, it will plot a shaded area of the specified width around the vertical lines specified at `vline`.
        It can be an array of the same length as `vline`, or a single value to be applied to all.
        '''
        self.figsize = figsize
        '''Tuple with the figure size, as in matplotlib.'''
        self.log_xscale = log_xscale
        '''If true, plot the x-axis in logarithmic scale.'''
        self.show_yticks = show_yticks
        '''Show or not the yticks on the plot.'''
        self.xlabel = xlabel
        '''
        Custom label of the x-axis. If `None`, the default label will be used.
        Set to `''` to remove the label of the horizontal axis.
        '''
        self.ylabel = ylabel
        '''
        Label of the y-axis. If `None`, the default label will be used.
        Set to `''` to remove the label of the vertical axis.
        '''
        if not isinstance(legend, list) and legend is not None and legend != False:
            legend = [legend]
        self.legend = legend
        '''
        If `None`, the filenames will be used as legend. Can be a bool to show or hide the plot legend.
        It can also be an array containing the strings to display; in that case, elements set to `False` will not be displayed.
        '''
        self.legend_title = legend_title
        '''Title of the legend. Defaults to `None`.'''
        self.legend_size = legend_size
        '''Size of the legend, as in matplotlib. Defaults to `'medium'`.'''
        self.legend_loc = legend_loc
        '''Location of the legend, as in matplotlib. Defaults to `'best'`.'''

    def _set_limits(self, limits) -> list:
        '''Set the x and y limits of the plot.'''
        if limits is None:
            return [None, None]
        if isinstance(limits, tuple):
            limits = list(limits)
        if isinstance(limits, list):
            if len(limits) == 0:
                return [None, None]
            if len(limits) == 1:
                return [None, limits[0]]
            if len(limits) == 2:
                return limits
            else:
                return limits[:2]
        if isinstance(limits, int) or isinstance(limits, float):
            return [None, limits]
        else:
            raise ValueError(f"Unknown plotting limits: Must be specified as a list of two elements, as [low_limit, high_limit]. Got: {limits}")


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
    def __init__(
            self,
            index:int=0,
            xmin:float=None,
            xmax:float=None,
            ymin:list=None,
            ymax:list=None,
            zoom:bool=False,
        ):
        '''All values can be set when initializing the ScaleRange object.'''
        self.index: int = index
        '''Index of the dataframe to use as reference.'''
        self.xmin: float = xmin
        '''Minimum x-value to start normalizing the plots.'''
        self.xmax: float = xmax
        '''Maximum x-value to normalize the plots.'''
        self.ymin: list = ymin
        '''List with minimum y-values to normalize the plots.'''
        self.ymax: list = ymax
        '''List with minimum y-values to normalize the plots.
        If `Plotting.normalize=True`, the plots are normalized according to the y-values provided.
        '''
        self.zoom: bool = zoom
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


class Spectra:
    '''
    Spectra object. Used to load and process spectral data.
    Most functions present in Maat receive this object as input.

    **Use example:** to load two INS spectra CSV files from MANTID with cm$^{-1}$ as input units,
    and plot them in meV units, normalizing their heights over the range from 20 to 50 meV:
    ```python
    import maat as mt
    ins = mt.Spectra(
        type='INS',
        filename=['example_1.csv', 'example_2.csv'],
        units_in='cm-1',
        units='meV',
        plotting=mt.Plotting(
            title='Calculated INS',
            normalize=True,
            ),
        scale_range=mt.ScaleRange(
            xmin=20,
            xmax=50,
            ),
        )
    mt.plot.spectra(ins)
    ```

    Check more use examples in the `/examples/` folder.

    Below is a list of the available parameters for the Spectra object, along with their descriptions.
    '''
    def __init__(
            self,
            type:str=None,
            comment:str=None,
            save_as:str=None,
            filename=None,
            dataframe=None,
            units=None,
            units_in=None,
            plotting:Plotting=Plotting(),
            scale_range:ScaleRange=ScaleRange(),
        ):
        '''All values can be set when initializing the Spectra object.'''
        self.type = None
        '''Type of the spectra: `'INS'`, `'ATR'`, or `'RAMAN'`.'''
        self.comment = comment
        '''Custom comment. If `Plotting.title` is None,  it will be the title of the plot.'''
        self.save_as = save_as
        '''Filename to save the plot. None by default.'''
        self.filename = None
        '''
        List containing the filenames with the spectral data.
        Loaded automatically with Pandas at initialization.
        In order for Pandas to read the files properly, note that the column lines must start by `#`.
        Any additional line that is not data must be removed or commented with `#`.
        CSV files must be formatted with the first column as the energy or energy transfer,
        and the second column with the intensity or absorbance, depending on the case. An additional third `'Error'` column can be used.
        '''
        self.dataframe = None
        '''
        List containing the pandas dataframes with the spectral data.
        Loaded automatically from the filenames at initialization.
        '''
        self.units = None
        '''Target units of the spectral data. Can be `'meV'` or `'cm-1'`, written as any of the variants listed in `maat.alias.unit[unit]`.'''
        self.units_in = None
        '''
        Input units of the spectral data, used in the input CSV files. Can be `'meV'` or `'cm-1'`, written as any of the variants listed in `maat.alias.unit[unit]`.
        If the input CSV files have different units, it can also be set as a list of the same length of the number of input files, eg. `['meV', 'cm-1', 'cm-1']`.
        '''
        self.plotting = plotting
        '''`Plotting` object, used to set the plotting options.'''
        self.scale_range = scale_range
        '''`ScaleRange` object, used to set the normalization parameters.'''

        self = self._set_type(type)
        self = self._set_dataframe(filename, dataframe)
        self = self.set_units(units, units_in)

    def _set_type(self, type):
        '''Set and normalize the type of the spectra: `INS`, `ATR`, or `RAMAN`.'''
        if type in alias.experiment['INS']:
            self.type = 'INS'
        elif type in alias.experiment['ATR']:
            self.type = 'ATR'
        elif type in alias.experiment['RAMAN']:
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
        '''
        Method to change between spectral units. ALWAYS use this method to do that.

        For example, to change from cm-1 to meV:
        ```python
        # Spectra.set_units(desired_units, units_input)
        Spectra.set_units('meV', 'cm-1')
        ```
        '''
        mev = 'meV'
        cm = 'cm-1'
        unit_format={
                mev: alias.unit['meV'],
                cm: alias.unit['cm-1'] + alias.unit['cm'],
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
    '''
    Material class.
    Used to calculate molar masses and cross sections,
    and to pass data to different analysis functions such as `maat.deuteration.impulse_approx().`
    '''
    def __init__(
            self,
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
        to only set the atoms and the grams, and optionally the name, and calculate the rest with `Material.set()`.
        '''
        self.atoms = atoms
        '''
        Dict of atoms in the material, as in `{'H': 6, 'C':1, 'N':1}`.
        Isotopes can be expressed as 'H2', 'He4', etc. with the atom symbol + isotope mass number.
        '''
        self.name = name
        '''String with the name of the material.'''
        self.grams = grams
        '''Mass, in grams.'''
        self.grams_error = grams_error
        '''Error of the measured mass in grams. Set automatically with `Material.set()`.'''
        self.mols = mols
        '''Number of moles. Set automatically with `Material.set()`.'''
        self.mols_error = mols_error
        '''Error of the number of moles. Set automatically with `Material.set()`.'''
        self.molar_mass = molar_mass
        '''Molar mass of the material, in mol/g. Calculated automatically with `Material.set()`.'''
        self.cross_section = cross_section
        '''Cross section of the material, in barns. Calculated automatically with `Material.set()`.'''

    def _set_grams_error(self):
        '''Set the error in grams, based on the number of decimal places.'''
        if self.grams is None:
            return
        decimal_accuracy = len(str(self.grams).split('.')[1])
        # Calculate the error in grams
        self.grams_error = 10**(-decimal_accuracy)

    def _set_mass(self):
        '''
        Set the molar mass of the material.
        If `Material.grams` is not `None`, the number of moles will be calculated and overwritten.
        If an isotope is used, eg. `'He4'`, it splits the name with `maat.constants.atoms.get_isotope_index`.
        '''
        material_grams_per_mol = 0.0
        for key in self.atoms:
            try:
                material_grams_per_mol += self.atoms[key] * atom[key].mass
            except KeyError: # Split the atomic flag as H2, etc
                element, isotope = atoms.split_isotope(key)
                material_grams_per_mol += self.atoms[key] * atom[element].isotope[isotope].mass
        self.molar_mass = material_grams_per_mol
        if self.grams is not None:
            self._set_grams_error()
            self.mols = self.grams / material_grams_per_mol
            self.mols_error = self.mols * np.sqrt((self.grams_error / self.grams)**2)
    
    def _set_cross_section(self):
        '''
        Set the cross section of the material, based on the atoms dict.
        If an isotope is used, eg. `'He4'`, it splits the name with `maat.constants.atoms.get_isotope_index`.
        '''
        total_cross_section = 0.0
        for key in self.atoms:
            try:
                total_cross_section += self.atoms[key] * atom[key].cross_section
            except KeyError: # Split the atomic flag as H2, etc
                element, isotope_index = atoms.split_isotope(key)
                total_cross_section += self.atoms[key] * atom[element].isotope[isotope_index].cross_section
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

