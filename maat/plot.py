from .core import *


def spectra(mdata:MData):
    
    if mdata.figsize:
        fig, ax = plt.subplots(figsize=mdata.figsize)
    else:
        fig, ax = plt.subplots()

    if mdata.low_xlim:
        ax.set_xlim(left=mdata.low_xlim)
    if mdata.top_xlim:
        ax.set_xlim(right=mdata.top_xlim)
    if mdata.low_ylim:
        ax.set_ylim(bottom=mdata.low_ylim)
    if mdata.top_ylim:
        ax.set_ylim(top=mdata.top_ylim)

    if mdata.scale_range:
        scale_factor = 1.0
        if mdata.scale_range[2]:
            scale_factor = mdata.scale_range[2]
        df0 = mdata.dataframe[0]
        df0 = df0[(df0[df0.columns[0]] >= mdata.scale_range[0]) & (df0[df0.columns[0]] <= mdata.scale_range[1])]
        max_value_on_range = df0[df0.columns[1]].max()
        ax.set_ylim(top=scale_factor*max_value_on_range)

    strings_to_delete_from_name = ['.csv', '_INS', '_ATR', '_FTIR', '_temp']
    for df, name in zip(mdata.dataframe, mdata.filename):
        if mdata.scale_range:
            first_cut = mdata.scale_range[0]
            second_cut = mdata.scale_range[1]
            df_range = df[(df[df.columns[0]] >= first_cut) & (df[df.columns[0]] <= second_cut)]
            i_max_value_on_range = df_range[df_range.columns[1]].max()
            df[df.columns[1]] = max_value_on_range * (df[df.columns[1]] / i_max_value_on_range)
        
        if (mdata.offset is True) and (mdata.low_ylim is not None) and (mdata.top_ylim is not None):
            number_of_plots = len(mdata.dataframe)
            height = mdata.top_ylim - mdata.low_ylim
            df[df.columns[1]] = (df[df.columns[1]] / number_of_plots) + (mdata.filename.index(name) * height) / number_of_plots

        name_clean = name.replace('_', ' ')
        for string in strings_to_delete_from_name:
            name_clean = name_clean.replace(string, '')
        if mdata.legend and isinstance(mdata.legend, list):
            name_clean = mdata.legend[mdata.filename.index(name)]
        df.plot(x=df.columns[0], y=df.columns[1], label=name_clean, ax=ax)

    plt.title(mdata.title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    if mdata.log_xscale:
        ax.set_xscale('log')
    if not mdata.show_yticks:
        ax.set_yticks([])
    if mdata.legend:
        ax.legend()
    else:
        ax.legend().set_visible(False)

    if mdata.save_as:
        root = os.getcwd()
        save_name = os.path.join(root, mdata.save_as)
        plt.savefig(save_name)
    
    plt.show()

