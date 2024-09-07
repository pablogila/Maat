from .core import *
from .fit import *

'''
This module contains functions to manipulate data.
'''

def normalize(spectra:Spectra):
    sdata = deepcopy(spectra)
    if hasattr(sdata, 'scale_range') and sdata.scale_range is not None:
        scale_range = sdata.scale_range
        if scale_range.ymax:
            return _normalize_y(sdata)
    else:
        scale_range = ScaleRange()

    df_index = scale_range.index if scale_range.index else 0
    df0 = sdata.dataframe[df_index]

    if scale_range.xmin is None:
        scale_range.xmin = min(df0[df0.columns[0]])
    if scale_range.xmax is None:
        scale_range.xmax = max(df0[df0.columns[0]])

    sdata.scale_range = scale_range

    xmin = scale_range.xmin
    xmax = scale_range.xmax

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
    if not len(sdata.scale_range.ymax) == len(sdata.dataframe):
        raise ValueError("normalize: len(ymax) does not match len(dataframe)")
    scale_range = sdata.scale_range
    ymax = scale_range.ymax
    ymin = scale_range.ymin if scale_range.ymin else [0.0]
    if len(ymin) == 1:
        ymin = ymin * len(sdata.dataframe)
    index = scale_range.index if scale_range.index else 0
    reference_height = ymax[index] - ymin[index]
    normalized_dataframes = []
    for i, df in enumerate(sdata.dataframe):
        height = ymax[i] - ymin[i]
        df[df.columns[1]] =  df[df.columns[1]] * reference_height / height
        normalized_dataframes.append(df)
    sdata.dataframe = normalized_dataframes
    return sdata


def normalize_area(spectra:Spectra):
    sdata = deepcopy(spectra)
    if hasattr(sdata, 'scale_range') and sdata.scale_range is not None:
        scale_range = sdata.scale_range
        if scale_range.ymax:
            return _normalize_y(sdata)
    else:
        scale_range = ScaleRange()

    df_index = scale_range.index if scale_range.index else 0
    df0 = sdata.dataframe[df_index]

    if scale_range.xmin is None:
        scale_range.xmin = min(df0[df0.columns[0]])
    if scale_range.xmax is None:
        scale_range.xmax = max(df0[df0.columns[0]])

    sdata.scale_range = scale_range

    xmin = scale_range.xmin
    xmax = scale_range.xmax

    df0 = df0[(df0[df0.columns[0]] >= xmin) & (df0[df0.columns[0]] <= xmax)]
    area_df0 = area_under_peak(df0, peak=[xmin,xmax])
    normalized_dataframes = []
    for df in sdata.dataframe:
        df_range = df[(df[df.columns[0]] >= xmin) & (df[df.columns[0]] <= xmax)]
        area_df = area_under_peak(df_range, peak=[xmin,xmax])
        scaling = area_df0[0] / area_df[0]
        df[df.columns[1]] =  df[df.columns[1]] * scaling
        normalized_dataframes.append(df)
    sdata.dataframe = normalized_dataframes
    return sdata

