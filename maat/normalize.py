'''
This module contains functions to normalize data and other variables.
'''


from .classes import *
from .fit import *
from .constants import *


def unit_str(unit:str):
    for key, value in unit_keys.items():
        if unit in value:
            return key
    print(f"WARNING: Unknown unit '{unit}'")
    return unit


def spectra(spectra:Spectra):
    sdata = deepcopy(spectra)
    if hasattr(sdata, 'scale_range') and sdata.scale_range is not None:
        scale_range = sdata.scale_range
        if scale_range.ymax:
            return _spectra_y(sdata)
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


def _spectra_y(sdata:Spectra):
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


def area(spectra:Spectra):
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
    area_df0, _ = area_under_peak(sdata, peak=[xmin,xmax], df_index=df_index, min_as_baseline=True)
    normalized_dataframes = []
    for df_i, df in enumerate(sdata.dataframe):
        area_df, _ = area_under_peak(sdata, peak=[xmin,xmax], df_index=df_i, min_as_baseline=True)
        scaling = area_df0 / area_df
        df[df.columns[1]] =  df[df.columns[1]] * scaling
        normalized_dataframes.append(df)
    sdata.dataframe = normalized_dataframes
    return sdata

