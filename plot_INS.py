import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
import os

version = '2024.05.30.2100'

# Conversion factors
mev_to_cm = 8.0655
cm_to_mev = 1.0 / mev_to_cm


class INS:
    def __init__(self,
                 filenames,
                 title:str=None,
                 save_as:str=None,
                 units_in='cm',
                 units='meV',
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

        self.units = units
        if units_in is None:
            self.units_in = ['cm'] * len(filenames)
        elif isinstance(units_in, str):
            self.units_in = [units_in] * len(filenames)
        elif isinstance(units_in, list) and len(units_in) == len(filenames):
            self.units_in = units_in
        elif isinstance(units_in, list) and len(units_in) == 1:
            self.units_in = units_in * len(filenames)
        else:
            raise ValueError("units_in must be either a string, or a list of the same length as filenames.")

        if scale_range is not None and len(scale_range) != 2:
            raise ValueError("scale_range must be a list of two elements.")

        self.filenames = filenames
        self.title = title
        self.dataframes = [self.read_ins(filename) for filename in filenames] if isinstance(filenames, list) else [self.read_ins(filenames)]
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


def plot_ins(ins:INS):
    
    if ins.figsize:
        fig, ax = plt.subplots(figsize=ins.figsize)
    else:
        fig, ax = plt.subplots()

    if ins.x_low_lim:
        ax.set_xlim(left=ins.x_low_lim)
    if ins.x_top_lim:
        ax.set_xlim(right=ins.x_top_lim)
    if ins.y_low_lim:
        ax.set_ylim(bottom=ins.y_low_lim)
    if ins.y_top_lim:
        ax.set_ylim(top=ins.y_top_lim)

    if ins.scale_range:
        df0 = ins.dataframes[0]
        df0 = df0[(df0[df0.columns[0]] >= ins.scale_range[0]) & (df0[df0.columns[0]] <= ins.scale_range[1])]
        max_df = df0[df0.columns[1]].max()
        ax.set_ylim(top=ins.scale_y*max_df)

    strings_to_delete_from_name = ['.csv', '_INS', '_temp']
    for df, name in zip(ins.dataframes, ins.filenames):
        if ins.scale_range:
            first_cut = ins.scale_range[0]
            second_cut = ins.scale_range[1]
            df_range_i = df[(df[df.columns[0]] >= first_cut) & (df[df.columns[0]] <= second_cut)]
            max_df_i = df_range_i[df_range_i.columns[1]].max()
            df[df.columns[1]] = max_df * (df[df.columns[1]] / max_df_i)
        
        if (ins.y_offset is True) and (ins.y_low_lim is not None) and (ins.y_top_lim is not None):
            number_of_plots = len(ins.dataframes)
            height = ins.y_top_lim - ins.y_low_lim
            df[df.columns[1]] = (df[df.columns[1]] / number_of_plots) + (ins.filenames.index(name) * height) / number_of_plots

        name_clean = name.replace('_', ' ')
        for string in strings_to_delete_from_name:
            name_clean = name_clean.replace(string, '')
        if ins.legend and isinstance(ins.legend, list):
            name_clean = ins.legend[ins.filenames.index(name)]
        df.plot(x=df.columns[0], y=df.columns[1], label=name_clean, ax=ax)

    plt.title(ins.title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    if ins.log:
        ax.set_xscale('log')
    if ins.hide_y_axis:
        ax.set_yticks([])
    if ins.legend:
        ax.legend()
    else:
        ax.legend().set_visible(False)

    if ins.save_as:
        root = os.getcwd()
        save_name = os.path.join(root, ins.save_as)
        plt.savefig(save_name)
    
    plt.show()


def calculate_peak_deuteration_mapi(ins:INS, baseline=0.15, baseline_error=0.0):

    df3_lowcut = 28.8
    df3_highcut = 30.7
    df4_lowcut = df3_highcut
    df4_highcut = 33.0
    df5_lowcut = df4_highcut
    df5_highcut = 35.0
    df6_lowcut = 36.0
    df6_highcut = 39.0

    df = ins.dataframes[0].copy()
    df[df.columns[1]] = df[df.columns[1]] - baseline

    df3 = df[(df[df.columns[0]] >= df3_lowcut) & (df[df.columns[0]] <= df3_highcut)]
    df4 = df[(df[df.columns[0]] >= df4_lowcut) & (df[df.columns[0]] <= df4_highcut)]
    df5 = df[(df[df.columns[0]] >= df5_lowcut) & (df[df.columns[0]] <= df5_highcut)]
    df6 = df[(df[df.columns[0]] >= df6_lowcut) & (df[df.columns[0]] <= df6_highcut)]

    df3_area = scipy.integrate.simpson(df3[df3.columns[1]], x=df3[df3.columns[0]]) / 3
    df4_area = scipy.integrate.simpson(df4[df4.columns[1]], x=df4[df4.columns[0]]) / 4
    df5_area = scipy.integrate.simpson(df5[df5.columns[1]], x=df5[df5.columns[0]]) / 5
    df6_area = scipy.integrate.simpson(df6[df6.columns[1]], x=df6[df6.columns[0]]) / 6

    total_area = df3_area + df4_area + df5_area + df6_area

    df3_ratio = df3_area / total_area
    df4_ratio = df4_area / total_area
    df5_ratio = df5_area / total_area
    df6_ratio = df6_area / total_area

    deuteration = 1 * df3_ratio + (2/3) * df4_ratio + (1/3) * df5_ratio + 0 * df6_ratio
    protonation = 0 * df3_ratio + (1/3) * df4_ratio + (2/3) * df5_ratio + 1 * df6_ratio

    # Error propagation

    df3_area_error = 0
    df4_area_error = 0
    df5_area_error = 0
    df6_area_error = 0
    for error in df3['Error']:
        df3_area_error += error**2
    for error in df4['Error']:
        df4_area_error += error**2
    for error in df5['Error']:
        df5_area_error += error**2
    for error in df6['Error']:
        df6_area_error += error**2
    df3_area_error = np.sqrt(df3_area_error + baseline_error**2)
    df4_area_error = np.sqrt(df4_area_error + baseline_error**2)
    df5_area_error = np.sqrt(df5_area_error + baseline_error**2)
    df6_area_error = np.sqrt(df6_area_error + baseline_error**2)

    total_area_error = np.sqrt(df3_area_error**2 + df4_area_error**2 + df5_area_error**2 + df6_area_error**2)

    df3_error = abs(df3_area) * np.sqrt((df3_area_error/df3_area)**2 + (total_area_error/total_area)**2)
    df4_error = abs(df4_area) * np.sqrt((df4_area_error/df4_area)**2 + (total_area_error/total_area)**2)
    df5_error = abs(df5_area) * np.sqrt((df5_area_error/df5_area)**2 + (total_area_error/total_area)**2)
    df6_error = abs(df6_area) * np.sqrt((df6_area_error/df6_area)**2 + (total_area_error/total_area)**2)

    deuteration_error = np.sqrt(df3_error**2 + df4_error**2 + df5_error**2)
    protonation_error = np.sqrt(df6_error**2 + df5_error**2 + df4_error**2)

    print(f"DDD:  {round(df3_ratio,2)}  +-  {round(df3_error,2)}")
    print(f"DDH:  {round(df4_ratio,2)}  +-  {round(df4_error,2)}")
    print(f"DHH:  {round(df5_ratio,2)}  +-  {round(df5_error,2)}")
    print(f"HHH:  {round(df6_ratio,2)}  +-  {round(df6_error,2)}")
    print(f"Total deuteration:  {round(deuteration,2)}  +-  {round(deuteration_error,2)}")
    print(f"Total protonation:  {round(protonation,2)}  +-  {round(protonation_error,2)}")


def get_baseline(ins:INS, lowcut=27, highcut=35):
    df = ins.dataframes[0]
    df_range = df[(df[df.columns[0]] >= lowcut) & (df[df.columns[0]] <= highcut)]
    x = df_range[df.columns[0]]
    y = df_range['S(Q,E)']
    error_range = df_range['Error']

    # Perform a weighted least squares fit
    degree = 1
    weights = 1.0 / error_range**2
    coefficients = np.polyfit(x, y, degree, w=weights)
    polynomial = np.poly1d(coefficients)

    # Calculate the baseline
    baseline = polynomial(x)

    # Calculate the standard deviation of the residuals
    residuals = y - baseline
    error_std = np.std(residuals)

    baseline_value = np.mean(baseline)

    return baseline_value, error_std


### MAIN ###


ins_data = INS(
    filenames=['CH3ND3PbI3_1.5GPa.csv', 'CH3NH3PbI3_1.5GPa.csv'],
    title=None,
    save_as=None,
    units_in='cm',
    units='meV',
    x_low_lim=0.0,
    x_top_lim=120,
    y_low_lim=-0.01,
    y_top_lim=0.06,
    y_offset=True,
    log=False,
    hide_y_axis=True,
    legend=['CH3ND3PbI3 1.5 GPa','CH3NH3PbI3 1.5 GPa'],
    scale_range=None,
    scale_y=1.0,
    figsize=(7,4)
    )

plot_ins(ins_data)

