from .core import *


def normalize(spectra:Spectra):
    sdata = deepcopy(spectra)
    df_index = scale_range.index if scale_range.index else 0
    df0 = sdata.dataframe[df_index]
    
    if getattr(sdata, 'scale_range', None) and scale_range.ymax:
        return _normalize_y(sdata)

    xmin = scale_range.xmin if scale_range.xmin else min(df0[df0.columns[0]])
    xmax = scale_range.xmax if scale_range.xmax else max(df0[df0.columns[0]])

    df0 = df0[(df0[df0.columns[0]] >= xmin) & (df0[df0.columns[0]] <= xmax)]
    ymax_on_range = df0[df0.columns[1]].max()
    normalized_dataframes = []
    for df in sdata.dataframe:
        df_range = df[(df[df.columns[0]] >= xmin) & (df[df.columns[0]] <= xmax)]
        i_ymax_on_range = df_range[df_range.columns[1]].max()
        df[df.columns[1]] =  df[df.columns[1]] * ymax_on_range / i_ymax_on_range
        normalized_dataframes.append(df)
    sdata.dataframe = normalized_dataframes
    return sdata


def _normalize_y(sdata:Spectra):
    return None  ## TO-IMPLEMENT
'''
    scale_range = sdata.scale_range
    ymax_on_range = None
    ymax = scale_range.ymax
    ymin = scale_range.ymin if scale_range.ymin else 0.0
    normalized_dataframes = []
    for df in sdata.dataframe:
        df[df.columns[1]] =  df[df.columns[1]] * (ymax - ymin)
        normalized_dataframes.append(df)
    sdata.dataframe = normalized_dataframes
    return sdata, ymax_on_range

    elif scale_range.ymax:
        ymax = scale_range.ymax
        ymin = scale_range.ymin if scale_range.ymin else 0.0
        normalized_dataframes = []
        for df in sdata.dataframe:
            df[df.columns[1]] =  df[df.columns[1]] * (ymax - ymin)
            normalized_dataframes.append(df)
        sdata.dataframe = normalized_dataframes
        return sdata, ymax_on_range
'''

