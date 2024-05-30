import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
import os

version = '2024.05.30.2100'

# Conversion factors
mev_to_cm = 8.0655
cm_to_mev = 1.0 / mev_to_cm


class ATR:
    def __init__(self,
                 filenames,
                 title:str=None,
                 save_as:str=None,
                 x_low_lim=0,
                 x_top_lim=50,
                 y_low_lim=None,
                 y_top_lim=None,
                 y_offset=True,
                 log:bool=False,
                 hide_y_axis:bool=True,
                 legend:bool=True,
                 scale_range:list=None,
                 scale_y=1.0,
                 figsize:tuple=None,
                 ):

        self.filenames = filenames
        self.title = title
        self.dataframes = [self.read_atr(filename) for filename in filenames] if isinstance(filenames, list) else [self.read_atr(filenames)]
        self.save_as = save_as
        self.x_low_lim = x_low_lim
        self.x_top_lim = x_top_lim
        self.y_low_lim = y_low_lim
        self.y_top_lim = y_top_lim
        self.y_offset = y_offset
        self.log = log
        self.hide_y_axis = hide_y_axis
        self.legend = legend
        self.scale_range = scale_range
        self.scale_y = scale_y
        self.figsize = figsize

    def read_atr(self, filename):
        E_units = 'cm^-1'
        root = os.getcwd()
        file = os.path.join(root, filename)
        df = pd.read_csv(file, comment='#')
        df.columns = [f'Wavenumber / {E_units}', 'Absorbance']
        print(df.head())
        return df


def plot_atr(atr:ATR):
    
    if atr.figsize:
        fig, ax = plt.subplots(figsize=atr.figsize)
    else:
        fig, ax = plt.subplots()

    if atr.x_low_lim:
        ax.set_xlim(left=atr.x_low_lim)
    if atr.x_top_lim:
        ax.set_xlim(right=atr.x_top_lim)
    if atr.y_low_lim:
        ax.set_ylim(bottom=atr.y_low_lim)
    if atr.y_top_lim:
        ax.set_ylim(top=atr.y_top_lim)

    if atr.scale_range:
        df0 = atr.dataframes[0]
        df0 = df0[(df0[df0.columns[0]] >= atr.scale_range[0]) & (df0[df0.columns[0]] <= atr.scale_range[1])]
        max_df = df0[df0.columns[1]].max()
        ax.set_ylim(top=atr.scale_y*max_df)

    strings_to_delete_from_name = ['.csv', '_INS', '_temp']
    for df, name in zip(atr.dataframes, atr.filenames):
        if atr.scale_range:
            first_cut = atr.scale_range[0]
            second_cut = atr.scale_range[1]
            df_range_i = df[(df[df.columns[0]] >= first_cut) & (df[df.columns[0]] <= second_cut)]
            max_df_i = df_range_i[df_range_i.columns[1]].max()
            df[df.columns[1]] = max_df * (df[df.columns[1]] / max_df_i)
        
        if (atr.y_offset is True) and (atr.y_low_lim is not None) and (atr.y_top_lim is not None):
            number_of_plots = len(atr.dataframes)
            height = atr.y_top_lim - atr.y_low_lim
            df[df.columns[1]] = (df[df.columns[1]] / number_of_plots) + (atr.filenames.index(name) * height) / number_of_plots

        name_clean = name.replace('_', ' ')
        for string in strings_to_delete_from_name:
            name_clean = name_clean.replace(string, '')
        if atr.legend and isinstance(atr.legend, list):
            name_clean = atr.legend[atr.filenames.index(name)]
        df.plot(x=df.columns[0], y=df.columns[1], label=name_clean, ax=ax)

    plt.title(atr.title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    if atr.log:
        ax.set_xscale('log')
    if atr.hide_y_axis:
        ax.set_yticks([])
    if atr.legend:
        ax.legend()
    else:
        ax.legend().set_visible(False)

    if atr.save_as:
        root = os.getcwd()
        save_name = os.path.join(root, atr.save_as)
        plt.savefig(save_name)
    
    plt.show()


### MAIN ###


atr_data = ATR(
    filenames=['MAI-ND_KS169_ATR_ISIS_256scans_4cm-res_atr-corrected.dat', 'MAI_comGCSM_ATR_ISIS_256scans_4cm-res_atr-corrected.dat'],
    title=None,
    save_as=None,
    x_low_lim=4000,
    x_top_lim=500,
    y_low_lim=0,
    y_top_lim=0.84,
    y_offset=True,
    log=False,
    hide_y_axis=True,
    legend=['CH3ND3I','CH3NH3I'],
    scale_range=None,
    scale_y=1.0,
    figsize=(7,4)
    )

plot_atr(atr_data)

