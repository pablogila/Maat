from .constants import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
from scipy.interpolate import CubicSpline
from copy import deepcopy
import os
import gzip
import shutil
import json
import time


version = 'vMT.2024.06.26.1200'


class Spectra:
    def __init__(self,
                 type:str=None,
                 title:str=None,
                 save_as:str=None,
                 filename=None,
                 dataframe=None,
                 units=None,
                 units_in=None,
                 log_xscale:bool=False,
                 low_xlim=0,
                 top_xlim=50,
                 low_ylim=None,
                 top_ylim=None,
                 offset=True,       
                 show_yticks:bool=False,
                 legend=None,
                 scale_range:list=[None, None, 1.0],
                 figsize:tuple=None,
                 atoms:dict=None,
                 atoms_ref:dict=None,
                 ):

        if scale_range is not None and not (len(scale_range) == 2 or len(scale_range) == 3):
            raise ValueError("scale_range must be a list of two elements: scale_range = [x_min, x_max, y_scale_factor]")

        self.title = title
        self.save_as = save_as
        self.log_xscale = log_xscale
        self.low_xlim = low_xlim
        self.top_xlim = top_xlim
        self.low_ylim = low_ylim
        self.top_ylim = top_ylim
        self.offset = offset
        self.show_yticks = show_yticks
        self.legend = legend
        self.scale_range = scale_range
        '''scale_range = [x_min, x_max, y_scale_factor]. Scale the y-axis of the dataframe to the maximum value in the range.'''
        self.figsize = figsize
        self.atoms = atoms
        '''Material object'''
        self.atoms_ref = atoms_ref
        ''''Material object used as reference'''

        self = self.set_type(type)
        self = self.set_dataframe(filename, dataframe)
        self.units = None
        self = self.set_units(units, units_in)


    def set_type(self, type):
        ins = ['INS', 'ins']
        atr = ['ATR', 'atr', 'FTIR', 'ftir']
        raman = ['RAMAN', 'raman', 'Raman']
        if type in ins:
            self.type = 'INS'
        elif type in atr:
            self.type = 'ATR'
        elif type in raman:
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
            default_unit='cm',
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

