'''This module manages the plotting of data.'''


from .classes import *
from . import normalize


def spectra(spectrum:Spectra):

    strings_to_delete_from_name = ['.csv', '.dat', '.txt', '_INS', '_ATR', '_FTIR', '_temp', '_RAMAN', '_Raman', '/data/', 'data/', '/csv/', 'csv/', '/INS/', 'INS/', '/FTIR/', 'FTIR/', '/ATR/', 'ATR/', '_smooth', '_smoothed', '_subtracted', '_cellsubtracted']
    normalize_area_keys = ['area', 'a', 'A']
    normalize_height_keys = ['height', 'y', 'Y', True]

    sdata = deepcopy(spectrum)

    if hasattr(sdata, 'plotting') and sdata.plotting.figsize:
        fig, ax = plt.subplots(figsize=sdata.plotting.figsize)
    else:
        fig, ax = plt.subplots()

    if sdata.plotting.normalize in normalize_height_keys:
        sdata = normalize.spectra(sdata)
    elif sdata.plotting.normalize in normalize_area_keys:
        sdata = normalize.area(sdata)

    calculated_low_ylim, calculated_top_ylim = _get_ylimits(sdata)

    low_ylim = calculated_low_ylim if not hasattr(sdata, 'plotting') or sdata.plotting.low_ylim is None else sdata.plotting.low_ylim
    top_ylim = calculated_top_ylim if not hasattr(sdata, 'plotting') or sdata.plotting.top_ylim is None else sdata.plotting.top_ylim
    
    low_xlim = None
    top_xlim = None
    if hasattr(sdata, 'plotting') and sdata.plotting is not None:
        low_xlim = sdata.plotting.low_xlim
        top_xlim = sdata.plotting.top_xlim

    number_of_plots = len(sdata.dataframe)
    height = top_ylim - low_ylim
    if hasattr(sdata, 'plotting') and sdata.plotting.offset is True:
        for i, df in enumerate(sdata.dataframe):
            reverse_i = (number_of_plots - 1) - i
            df[df.columns[1]] = df[df.columns[1]] + (reverse_i * height)
    elif hasattr(sdata, 'plotting') and (isinstance(sdata.plotting.offset, float) or isinstance(sdata.plotting.offset, int)):
        offset = sdata.plotting.offset
        for i, df in enumerate(sdata.dataframe):
            reverse_i = (number_of_plots - 1) - i
            df[df.columns[1]] = df[df.columns[1]] + (reverse_i * offset)
    _, calculated_top_ylim = _get_ylimits(sdata)
    top_ylim = calculated_top_ylim if not hasattr(sdata, 'plotting') or sdata.plotting.top_ylim is None else sdata.plotting.top_ylim

    if hasattr(sdata, 'plotting') and hasattr(sdata.plotting, 'legend'):
        if sdata.plotting.legend == False:
            for df in sdata.dataframe:
                df.plot(x=df.columns[0], y=df.columns[1], ax=ax)
        elif sdata.plotting.legend != None:
            if len(sdata.plotting.legend) == len(sdata.dataframe):
                for i, df in enumerate(sdata.dataframe):
                    if sdata.plotting.legend[i] == False:
                        continue  # Skip plots with False in the legend
                    clean_name = sdata.plotting.legend[i]
                    df.plot(x=df.columns[0], y=df.columns[1], label=clean_name, ax=ax)
            elif len(sdata.plotting.legend) == 1:
                clean_name = sdata.plotting.legend[0]
                for i, df in enumerate(sdata.dataframe):
                    df.plot(x=df.columns[0], y=df.columns[1], label=clean_name, ax=ax)
        elif sdata.plotting.legend == None and len(sdata.filename) == len(sdata.dataframe):
            for df, name in zip(sdata.dataframe, sdata.filename):
                clean_name = name
                for string in strings_to_delete_from_name:
                    clean_name = clean_name.replace(string, '')
                clean_name = clean_name.replace('_', ' ')
                df.plot(x=df.columns[0], y=df.columns[1], label=clean_name, ax=ax)

    plt.title(sdata.title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    add_top_ylim = 0
    add_low_ylim = 0
    if hasattr(sdata, 'plotting'):
        add_top_ylim = sdata.plotting.add_top_ylim
        add_low_ylim = sdata.plotting.add_low_ylim
        if sdata.plotting.log_xscale:
            ax.set_xscale('log')
        if not sdata.plotting.show_yticks:
            ax.set_yticks([])
        if sdata.plotting.legend != False:
            ax.legend(title=sdata.plotting.legend_title, fontsize=sdata.plotting.legend_size)
        else:
            ax.legend().set_visible(False)
    
    low_ylim = low_ylim - add_low_ylim
    top_ylim = top_ylim + add_top_ylim

    ax.set_ylim(bottom=low_ylim)
    ax.set_ylim(top=top_ylim)
    ax.set_xlim(left=low_xlim)
    ax.set_xlim(right=top_xlim)

    if hasattr(sdata, 'plotting') and sdata.plotting.vline is not None and sdata.plotting.vline_error is not None:
        for vline, vline_error in zip(sdata.plotting.vline, sdata.plotting.vline_error):
            lower_bound = vline - vline_error
            upper_bound = vline + vline_error
            ax.fill_between([lower_bound, upper_bound], low_ylim, top_ylim, color='gray', alpha=0.1)
    elif hasattr(sdata, 'plotting') and sdata.plotting.vline is not None:
        for vline in sdata.plotting.vline:
            ax.axvline(x=vline, color='gray', alpha=0.5, linestyle='--')

    if sdata.save_as:
        root = os.getcwd()
        save_name = os.path.join(root, sdata.save_as)
        plt.savefig(save_name)
    
    plt.show()


def _get_ylimits(spectrum:Spectra) -> tuple[float, float]:
    all_y_values = []
    for df in spectrum.dataframe:
        df_trim = df
        if hasattr(spectrum, 'plotting') and spectrum.plotting.low_xlim is not None:
            df_trim = df_trim[(df_trim[df_trim.columns[0]] >= spectrum.plotting.low_xlim)]
        if hasattr(spectrum, 'plotting') and spectrum.plotting.top_xlim is not None:
            df_trim = df_trim[(df_trim[df_trim.columns[0]] <= spectrum.plotting.top_xlim)]
        all_y_values.extend(df_trim[df_trim.columns[1]].tolist())
    calculated_low_ylim = min(all_y_values)
    calculated_top_ylim = max(all_y_values)

    ymax_on_range = None
    if hasattr(spectrum, 'scale_range') and spectrum.scale_range is not None:
        df_index = spectrum.scale_range.index if spectrum.scale_range.index else 0
        df0 = spectrum.dataframe[df_index]
        if spectrum.scale_range.xmin:
            df0 = df0[(df0[df0.columns[0]] >= spectrum.scale_range.xmin)]
        if spectrum.scale_range.xmax:
            df0 = df0[(df0[df0.columns[0]] <= spectrum.scale_range.xmax)]
        ymax_on_range = df0[df0.columns[1]].max()
    if hasattr(spectrum, 'plotting') and spectrum.plotting.zoom_range and ymax_on_range is not None:
        calculated_top_ylim = ymax_on_range

    return calculated_low_ylim, calculated_top_ylim

