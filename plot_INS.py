import pandas as pd
import matplotlib.pyplot as plt
import os

# Plot INS data. When exported from Mantid, the csv columns are:
# Energy / cm⁻¹, Counts, Error

# Conversion factors
mev_to_cm = 8.0655
cm_to_mev = 1.0 / mev_to_cm


class INS:
    def __init__(self, filenames, title=None, save_as='INS.svg', units=None, scale=True, xlim=50, ylim_scaling=2, log=False, legend=True):

        if units is None:
            self.units = ['cm'] * len(filenames)
        elif isinstance(units, str):
            self.units = [units] * len(filenames)
        elif isinstance(units, list) and len(units) == len(filenames):
            self.units = units
        elif isinstance(units, list) and len(units) == 1:
            self.units = units * len(filenames)
        else:
            raise ValueError("Units must be either a string, or a list of the same length as filenames.")

        self.title = title
        self.filenames = filenames
        self.dataframes = [self.read_ins(filename) for filename in filenames] if isinstance(filenames, list) else [self.read_ins(filenames)]
        self.xlim = xlim
        self.ylim_scaling = ylim_scaling
        self.log = log
        self.scale = scale
        self.legend = legend
        self.save_as = save_as


    def read_ins(self, filename):
        root = os.path.dirname(os.path.abspath(__file__))
        file = os.path.join(root, filename)
        df = pd.read_csv(file, comment='#')
        df = df.sort_values(by=df.columns[0])

        # Convert the energy to meV
        if self.units[self.filenames.index(filename)] == 'cm':
            df[df.columns[0]] = df[df.columns[0]] * cm_to_mev

        # if there are three columns, remove the third one
        if len(df.columns) > 2:
            df = df.drop(columns=df.columns[2])

        df.columns = ['Energy / meV', 'Intensity / a.u.']

        return df


def plot_ins(ins:INS):

    fig, ax = plt.subplots()

    if ins.log:
        ax.set_xscale('log')

    # Limit max intensity to INS.ylim_scaling times the MAPI peak of the 1st dataframe
    df0 = ins.dataframes[0]
    df_range = df0[(df0[df0.columns[0]] >= 30) & (df0[df0.columns[0]] <= 50)]
    max_df = df_range[df_range.columns[1]].max()

    ax.set_xlim([0, ins.xlim])
    ax.set_ylim([0, ins.ylim_scaling * max_df])

    strings_to_delete_from_name = ['.csv', '_INS', '_temp']
    for df, name in zip(ins.dataframes, ins.filenames):
        if ins.scale:
            df_range_i = df[(df[df.columns[0]] >= 30) & (df[df.columns[0]] <= 50)]
            max_df_i = df_range_i[df_range_i.columns[1]].max()
            df[df.columns[1]] = df[df.columns[1]] / max_df_i * max_df
        name_clean = name
        for string in strings_to_delete_from_name:
            name_clean = name_clean.replace(string, '')
        df.plot(x=df.columns[0], y=df.columns[1], label=name_clean, ax=ax)

    plt.title(ins.title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    if ins.legend:
        ax.legend()
    else:
        ax.legend().set_visible(False)

    root = os.path.dirname(os.path.abspath(__file__))
    save_name = os.path.join(root, ins.save_as)
    plt.savefig(save_name)
    plt.show()


### MAIN ###


ins_data = INS(filenames=['IREPA-ND-02_INS.csv', 'MAPI_comercial_INS.csv'], units=['cm','cm'], title=None)
plot_ins(ins_data)

