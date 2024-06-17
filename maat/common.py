import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
from scipy.interpolate import CubicSpline
from copy import deepcopy
import os
import gzip
import shutil
import json
import time


version = 'vM.2024.06.17.1800'


# Conversion factors
mev_to_cm = 8.0655
cm_to_mev = 1.0 / mev_to_cm
eV_to_J = 1.602176634e-19
J_to_eV = 1 / eV_to_J
angstrom_to_m = 1e-10
m_to_angstrom = 1 / angstrom_to_m
amu_to_kg = 1.66053906660e-27
kg_to_amu = 1 / amu_to_kg
eV_to_meV = 1000
meV_to_eV = 0.001


class Material:
    def __init__(self, name=None, atoms:dict=None):
        self.name = name
        self.atoms = composition
        '''Material composition as a dictionary, such as: methane.atoms = {'H': 4, 'C': 1}'''
        self.name = name
        self.atoms = atoms


class MData:
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
                 legend=True,
                 scale_range:list=[None, None, 1.0],
                 figsize:tuple=None,
                 material:Material=None,
                 material_ref:Material=None,
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
        self.material = material
        '''Material object'''
        self.material_ref = material_ref
        ''''Material object used as reference'''

        self = self.set_type(type)
        self = self.set_dataframe(filename, dataframe)
        self.units = None
        self = self.set_units(self, units, units_in)


    def set_type(self, type):
        ins = ['INS', 'ins']
        atr = ['ATR', 'atr', 'FTIR', 'ftir']
        if type in ins:
            self.type = 'INS'
        elif type in atr:
            self.type = 'ATR'
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
            self.dataframe = [self.read_file(file) for file in self.filename]
        return self


    def set_units(
            self,
            units,
            units_in=None,
            default_unit='cm',
            ):
        ''''ALLWAYS use this method to change units.'''

        mev = 'mev'
        cm = 'cm'
        unit_format={
                mev: ['mev', 'meV', 'MEV'],
                cm: ['cm', 'CM'],
            }

        if self.units is not None:
            units_in = deepcopy(self.units)
            self.units = units
        elif units is not None:
            units_in = units_in
            self.units = units
        elif units is None and units_in is None:
            units_in = None
            self.units = default_unit
        elif units is None and units_in is not None:
            self.units = units_in
            units_in = None

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
                self.dataframe[i][self.dataframe[i].columns[0]] = self.dataframe[i][self.dataframe[i].columns[0]] * cm_to_mev
            elif unit == cm and units_in[i] == mev:
                self.dataframe[i][self.dataframe[i].columns[0]] = self.dataframe[i][self.dataframe[i].columns[0]] * mev_to_cm
            else:
                raise ValueError(f"Units mismatching: {unit} and {units_in[i]}")


    def read_file(self, file):
        if self.type == 'INS':
            self.read_ins(file)
        elif self.type == 'ATR':
            self.read_atr(file)
        else:
            raise ValueError("Please specify the type of data: 'INS' or 'ATR'.")


####### ME LLEGO POR AQUI


    def read_ins(self, filename):
        mev = ['mev', 'meV', 'MEV']
        cm = ['cm', 'CM']
        E_units = None
        root = os.getcwd()
        file = os.path.join(root, filename)
        df = pd.read_csv(file, comment='#')
        df = df.sort_values(by=df.columns[0])
        # Convert the energies
        if self.units in mev:
            E_units = 'meV'
            if self.units_in[self.filenames.index(filename)] in cm:
                df[df.columns[0]] = df[df.columns[0]] * cm_to_mev
        elif self.units in cm:
            E_units = 'cm^-1'
            if self.units_in[self.filenames.index(filename)] in mev:
                df[df.columns[0]] = df[df.columns[0]] * mev_to_cm
        else:
            E_units = self.units

        if len(df.columns) > 3:
            df = df.drop(columns=df.columns[3])
        df.columns = [f'Energy transfer / {E_units}', 'S(Q,E)', 'Error']
        print(df.head())
        return df
    

    def read_atr(self, filename):
        pass

