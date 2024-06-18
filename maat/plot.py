from .core import *


def spectra(mdata:MData):
    
    if mdata.figsize:
        fig, ax = plt.subplots(figsize=mdata.figsize)
    else:
        fig, ax = plt.subplots()

    if getattr(mdata, 'scale_range', None) and mdata.scale_range[0] and mdata.scale_range[1]:
        scale_factor = 1.0
        first_cut = mdata.scale_range[0]
        second_cut = mdata.scale_range[1]
        if mdata.scale_range[2]:
            scale_factor = mdata.scale_range[2]
        df0 = mdata.dataframe[0]
        df0 = df0[(df0[df0.columns[0]] >= first_cut) & (df0[df0.columns[0]] <= second_cut)]
        max_value_on_range = df0[df0.columns[1]].max()
        ax.set_ylim(top=(scale_factor*max_value_on_range))

    normalized_dataframes = []
    for df in mdata.dataframe:
        if getattr(mdata, 'scale_range', None) and mdata.scale_range[0] and mdata.scale_range[1]:
            df_range = df[(df[df.columns[0]] >= first_cut) & (df[df.columns[0]] <= second_cut)]
            i_max_value_on_range = df_range[df_range.columns[1]].max()
            df[df.columns[1]] =  df[df.columns[1]] * max_value_on_range / i_max_value_on_range
        normalized_dataframes.append(df)

    all_y_values = []
    if mdata.low_ylim is None or mdata.top_ylim is None:
        for df in normalized_dataframes:
            df_trim = df
            if mdata.low_xlim is not None:
                df_trim = df_trim[(df_trim[df_trim.columns[0]] >= mdata.low_xlim)]
            if mdata.top_xlim is not None:
                df_trim = df_trim[(df_trim[df_trim.columns[0]] <= mdata.top_xlim)]
            all_y_values.extend(df_trim[df_trim.columns[1]].tolist())
        calculated_low_ylim = min(all_y_values)
        calculated_top_ylim = max(all_y_values)
        if mdata.low_ylim is None:
            mdata.low_ylim = calculated_low_ylim
        if mdata.top_ylim is None:
            mdata.top_ylim = calculated_top_ylim
    low_ylim = mdata.low_ylim
    top_ylim = mdata.top_ylim

    for df, name in zip(mdata.dataframe, mdata.filename):
        if mdata.offset is True:# and (mdata.low_ylim is not None) and (mdata.top_ylim is not None):
            number_of_plots = len(mdata.dataframe)
            height = top_ylim - low_ylim
            df[df.columns[1]] = (df[df.columns[1]] / number_of_plots) + (mdata.filename.index(name) * height) / number_of_plots

        strings_to_delete_from_name = ['.csv', '_INS', '_ATR', '_FTIR', '_temp']
        name_clean = name.replace('_', ' ')
        for string in strings_to_delete_from_name:
            name_clean = name_clean.replace(string, '')
        if mdata.legend and isinstance(mdata.legend, list):
            name_clean = mdata.legend[mdata.filename.index(name)]
        df.plot(x=df.columns[0], y=df.columns[1], label=name_clean, ax=ax)

    if mdata.low_xlim is not None:
        ax.set_xlim(left=mdata.low_xlim)
    if mdata.top_xlim is not None:
        ax.set_xlim(right=mdata.top_xlim)
    if mdata.low_ylim is not None:
        ax.set_ylim(bottom=mdata.low_ylim)
    if mdata.top_ylim is not None:
        ax.set_ylim(top=mdata.top_ylim)

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

