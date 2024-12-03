'''
## Description
This module contains functions for fitting and analyzing data.

## Index
- `mean_std()`
- `plateau()`
- `area_under_peak()`
- `ratio_areas()`

---
'''


from .constants import *
from .classes import *
import scipy
import numpy as np
from copy import deepcopy


def mean_std(list:list) -> tuple:
    '''
    Takes a `list` of values (int or float),
    and returns a tuple with the mean and standard deviation,
    calculated with numpy as:\n
    $\\sigma_{x}=\\sqrt{\\frac{\\sum{(x_{i}-{\\overline{x}})^2}}{n}}$
    '''
    for item in list:
        if item is not int or item is not float:
            raise ValueError(f'mean_std(list) requires float or int values. The following value is not valid: {item}')
    array = np.asarray(list)
    mean = array.mean()
    std = array.std()
    return mean, std


def plateau(spectra:Spectra, cuts=None, df_index:int=0):
    '''
    Fit the mean value and the error of a plateau in a `maat.classes.Spectra` object.
    If `maat.classes.Spectra.dataframe[df_index]` has an 'Error' column, those errors are also taken into account
    along with the standard deviation of the mean, else only the standard deviation is considered.
    The 'Error' column title can be any string in `maat.constants.file_keys['Error']`.\n
    Use as `maat.fit.plateau(spectra, cuts=[low_cut, high_cut], df_index=0)`.
    Note that `cuts`, `low_cut` and/or `top_cut` can be set to None.
    '''
    df = deepcopy(spectra.dataframe[df_index])
    if isinstance(cuts, list):
        low_cut = cuts[0]
        if len(cuts) > 1:
            top_cut = cuts[1]
        else:
            top_cut = None
    elif isinstance(cuts, float):  # If cuts is a float, it is considered as low_cut
        low_cut = cuts
        top_cut = None
    elif cuts is None:
        low_cut = None
        top_cut = None
    else:
        raise ValueError("plateau: cuts must be a float for the low_cut, or a list")
    if low_cut is not None:
        df = df[df[df.columns[0]] >= low_cut]
    if top_cut is not None:
        df = df[df[df.columns[0]] <= top_cut]
    mean = df[df.columns[1]].mean()
    std_mean = df[df.columns[1]].std()
    error_column = next((col for col in file_keys['Error'] if col in df.columns), None)  # Get the error column title
    if error_column:
        errors = df[error_column].to_numpy()
        std_data = np.sqrt(np.sum(errors**2)) / len(errors)
        std = np.sqrt(std_data**2 + std_mean**2)
    else:
        std = std_mean
    return mean, std


def area_under_peak(
    spectra:Spectra,
    peak:list,
    df_index:int=0,
    errors_as_in_baseline:bool=True,
    min_as_baseline:bool=False
    ):
    '''
    Calculate the area under a given peak.

    Peaks must be defined as `peak:list=[xmin, xmax, baseline=0, baseline_error=0]`.
    If the dataset has no `Error` column, the error for each point is assumed to be the same
    as the baseline error if `errors_as_in_baseline=True`, otherwise it is assumed to be zero.
    If `min_as_baseline=True` and `baseline=0`, the baseline is assumed to be the minimum value.
    Also, if `min_as_baseline=True` and there are negative areas even after applying the baseline,
    the baseline will be corrected to the minimum value.
    '''
    if len(peak) < 2:
        raise ValueError("area_under_peak: peak must have at least two values: [xmin, xmax]")
    xmin = peak[0]
    xmax = peak[1]
    baseline = peak[2] if len(peak) >= 3 else 0.0
    baseline_error = peak[3] if len(peak) >= 4 else 0.0

    df = deepcopy(spectra.dataframe[df_index])
    df_range = df[(df[df.columns[0]] >= xmin) & (df[df.columns[0]] <= xmax)]
    x = df_range[df.columns[0]].to_numpy()
    y = df_range[df.columns[1]].to_numpy()
    
    min_y = y.min()
    if min_as_baseline and (baseline == 0 or baseline > min_y):
        baseline = min_y

    y = y - baseline

    area = scipy.integrate.simpson(y, x=x)

    error_column = next((col for col in file_keys['Error'] if col in df_range.columns), None)  # Get the error column title
    if error_column:
        point_errors = df_range[error_column].to_numpy()
    else: # Assume the error in each point is the same as the baseline error
        if errors_as_in_baseline == True:
            point_errors = np.full_like(y, baseline_error)
        else:
            point_errors = np.zeros_like(y)
    total_errors = np.sqrt(point_errors**2 + baseline_error**2)
    area_error = np.sqrt(scipy.integrate.simpson(total_errors**2, x=x))

    return area, area_error


def ratio_areas(
    area:float,
    area_total:float,
    area_error:float=0.0,
    area_total_error:float=0.0,
    inverse_ratio:bool=False
):
    '''
    Check the ratio between two areas, e.g. to estimate deuteration levels from ATR data.
    The ratio is calculated as `area / area_total`. This behavior is modified if `inverse_ratio = True`,
    so that the ratio is calculated as `(area_total - area) / area_total`.
    Note that changing the ratio calculation also affects the error propagation.
    '''
    if inverse_ratio:
        ratio = (area_total - area) / area_total
        if ratio != 0.0:
            ratio_error = abs(ratio) * np.sqrt((np.sqrt(area_total_error**2 + area_error**2) / (area_total - area))**2 + (area_total_error / area_total)**2)
        else:
            ratio_error = None
    else:
        ratio = area / area_total
        if ratio != 0.0:
            ratio_error = abs(ratio) * np.sqrt((area_error / area)**2 + (area_total_error / area_total)**2)
        else:
            ratio_error = None
    
    return ratio, ratio_error

