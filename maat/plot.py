from .core import *
from . import tools


def spectra(spectrum:Spectra):

    strings_to_delete_from_name = ['.csv', '.dat', '.txt', '_INS', '_ATR', '_FTIR', '_temp', '_RAMAN', '_Raman', '/data/', 'data/', '/INS/', 'INS/', '/FTIR/', 'FTIR/', '/ATR/', 'ATR/', '_smooth', '_smoothed', '_subtracted', '_cellsubtracted']

    sdata = deepcopy(spectrum)
    scale_factor = sdata.plotting.scale_factor if hasattr(sdata, 'plotting') and sdata.plotting.scale_factor else 1.0

    if hasattr(sdata, 'plotting') and sdata.plotting.figsize:
        fig, ax = plt.subplots(figsize=sdata.plotting.figsize)
    else:
        fig, ax = plt.subplots()

    if sdata.plotting.normalize is True:
        sdata = tools.normalize(sdata)
    normalized_dataframes = sdata.dataframe

    all_y_values = []
    for df in normalized_dataframes:
        df_trim = df
        if hasattr(sdata, 'plotting') and sdata.plotting.low_xlim is not None:
            df_trim = df_trim[(df_trim[df_trim.columns[0]] >= sdata.plotting.low_xlim)]
        if hasattr(sdata, 'plotting') and sdata.plotting.top_xlim is not None:
            df_trim = df_trim[(df_trim[df_trim.columns[0]] <= sdata.plotting.top_xlim)]
        all_y_values.extend(df_trim[df_trim.columns[1]].tolist())
    calculated_low_ylim = min(all_y_values)
    calculated_top_ylim = max(all_y_values) * scale_factor

    ymax_on_range = None
    if hasattr(sdata, 'scale_range') and sdata.scale_range is not None:
        df_index = sdata.scale_range.index if sdata.scale_range.index else 0
        df0 = sdata.dataframe[df_index]
        if sdata.scale_range.xmin:
            df0 = df0[(df0[df0.columns[0]] >= sdata.scale_range.xmin)]
        if sdata.scale_range.xmax:
            df0 = df0[(df0[df0.columns[0]] <= sdata.scale_range.xmax)]
        ymax_on_range = df0[df0.columns[1]].max()
    if sdata.plotting.zoom_range and ymax_on_range is not None:
        calculated_top_ylim = ymax_on_range * scale_factor

    low_ylim = calculated_low_ylim if not hasattr(sdata, 'plotting') or sdata.plotting.low_ylim is None else sdata.plotting.low_ylim
    top_ylim = calculated_top_ylim if not hasattr(sdata, 'plotting') or sdata.plotting.top_ylim is None else sdata.plotting.top_ylim
    
    low_xlim = None
    top_xlim = None
    if hasattr(sdata, 'plotting') and sdata.plotting is not None:
        low_xlim = sdata.plotting.low_xlim
        top_xlim = sdata.plotting.top_xlim

    if hasattr(sdata, 'plotting') and sdata.plotting.offset is True:
        number_of_plots = len(sdata.dataframe)
        height = top_ylim - low_ylim
        top_ylim = top_ylim * number_of_plots
        for i, df in enumerate(sdata.dataframe):
            reverse_i = (number_of_plots - 1) - i
            df[df.columns[1]] = df[df.columns[1]] + (reverse_i * height)
    elif hasattr(sdata, 'plotting') and isinstance(sdata.plotting.offset, float):
        for i, df in enumerate(sdata.dataframe):
            df[df.columns[1]] = df[df.columns[1]] + sdata.plotting.offset

    for df, name in zip(sdata.dataframe, sdata.filename):
        clean_name = name
        for string in strings_to_delete_from_name:
            clean_name = clean_name.replace(string, '')
        clean_name = clean_name.replace('_', ' ')
        if hasattr(sdata, 'plotting') and hasattr(sdata.plotting, 'legend') and sdata.plotting.legend is not None:
            if len(sdata.plotting.legend) == len(sdata.filename):
                clean_name = sdata.plotting.legend[sdata.filename.index(name)]
            elif len(sdata.plotting.legend) == 1:
                clean_name = sdata.plotting.legend[0]
            else:
                raise ValueError("len(Spectra.plotting.legend) does not match len(Spectra.filename)")
        df.plot(x=df.columns[0], y=df.columns[1], label=clean_name, ax=ax)

        # TO-ADD: horizontal lines

    if hasattr(sdata, 'plotting') and sdata.plotting.vline is not None and sdata.plotting.vline_error is not None:
        for vline, vline_error in zip(sdata.plotting.vline, sdata.plotting.vline_error):
            ax.fill_betweeb(df[df.columns[0]], vline - vline_error, vline + vline_error, color='gray', alpha=0.5)
    elif hasattr(sdata, 'plotting') and sdata.plotting.vline is not None:
        for vline in sdata.plotting.vline:
            ax.axvline(x=vline, color='gray', alpha=0.5, linestyle='--')

    ax.set_ylim(bottom=low_ylim)
    ax.set_ylim(top=top_ylim)
    ax.set_xlim(left=low_xlim)
    ax.set_xlim(right=top_xlim)

    plt.title(sdata.title)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])

    if hasattr(sdata, 'plotting'):
        if sdata.plotting.log_xscale:
            ax.set_xscale('log')
        if not sdata.plotting.show_yticks:
            ax.set_yticks([])
        if sdata.plotting.legend is not False:
            ax.legend()
        else:
            ax.legend().set_visible(False)

    if sdata.save_as:
        root = os.getcwd()
        save_name = os.path.join(root, sdata.save_as)
        plt.savefig(save_name)
    
    plt.show()

