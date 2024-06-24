from .core import *


def spectra(spectrum:Spectra):

    sdata = deepcopy(spectrum)

    if sdata.figsize:
        fig, ax = plt.subplots(figsize=sdata.figsize)
    else:
        fig, ax = plt.subplots()

    if getattr(sdata, 'scale_range', None) and sdata.scale_range[0] and sdata.scale_range[1]:
        scale_factor = 1.0
        first_cut = sdata.scale_range[0]
        second_cut = sdata.scale_range[1]
        if sdata.scale_range[2]:
            scale_factor = sdata.scale_range[2]
        df0 = sdata.dataframe[0]
        df0 = df0[(df0[df0.columns[0]] >= first_cut) & (df0[df0.columns[0]] <= second_cut)]
        max_value_on_range = df0[df0.columns[1]].max()
        ax.set_ylim(top=(scale_factor*max_value_on_range))

    normalized_dataframes = []
    for df in sdata.dataframe:
        if getattr(sdata, 'scale_range', None) and sdata.scale_range[0] and sdata.scale_range[1]:
            df_range = df[(df[df.columns[0]] >= first_cut) & (df[df.columns[0]] <= second_cut)]
            i_max_value_on_range = df_range[df_range.columns[1]].max()
            df[df.columns[1]] =  df[df.columns[1]] * max_value_on_range / i_max_value_on_range
        normalized_dataframes.append(df)

    all_y_values = []
    if sdata.low_ylim is None or sdata.top_ylim is None:
        for df in normalized_dataframes:
            df_trim = df
            if sdata.low_xlim is not None:
                df_trim = df_trim[(df_trim[df_trim.columns[0]] >= sdata.low_xlim)]
            if sdata.top_xlim is not None:
                df_trim = df_trim[(df_trim[df_trim.columns[0]] <= sdata.top_xlim)]
            all_y_values.extend(df_trim[df_trim.columns[1]].tolist())
        calculated_low_ylim = min(all_y_values)
        calculated_top_ylim = max(all_y_values)
        if sdata.low_ylim is None:
            sdata.low_ylim = calculated_low_ylim
        if sdata.top_ylim is None:
            sdata.top_ylim = calculated_top_ylim
    low_ylim = sdata.low_ylim
    top_ylim = sdata.top_ylim

    for df, name in zip(sdata.dataframe, sdata.filename):
        if sdata.offset is True:# and (sdata.low_ylim is not None) and (sdata.top_ylim is not None):
            number_of_plots = len(sdata.dataframe)
            height = top_ylim - low_ylim
            reverse_index = (number_of_plots - 1) - sdata.filename.index(name)
            df[df.columns[1]] = (df[df.columns[1]] / number_of_plots) + (reverse_index * height) / number_of_plots
            #df[df.columns[1]] = (df[df.columns[1]] / number_of_plots) + (sdata.filename.index(name) * height) / number_of_plots

        strings_to_delete_from_name = ['.csv', '_INS', '_ATR', '_FTIR', '_temp', '_RAMAN', '_Raman']
        name_clean = name.replace('_', ' ')
        for string in strings_to_delete_from_name:
            name_clean = name_clean.replace(string, '')
        if sdata.legend and isinstance(sdata.legend, list):
            name_clean = sdata.legend[sdata.filename.index(name)]
        df.plot(x=df.columns[0], y=df.columns[1], label=name_clean, ax=ax)

    if sdata.low_xlim is not None:
        ax.set_xlim(left=sdata.low_xlim)
    if sdata.top_xlim is not None:
        ax.set_xlim(right=sdata.top_xlim)
    if sdata.low_ylim is not None:
        ax.set_ylim(bottom=sdata.low_ylim)
    if sdata.top_ylim is not None:
        ax.set_ylim(top=sdata.top_ylim)

    plt.title(sdata.title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    if sdata.log_xscale:
        ax.set_xscale('log')
    if not sdata.show_yticks:
        ax.set_yticks([])
    if sdata.legend is not False:
        ax.legend()
    else:
        ax.legend().set_visible(False)

    if sdata.save_as:
        root = os.getcwd()
        save_name = os.path.join(root, sdata.save_as)
        plt.savefig(save_name)
    
    plt.show()

