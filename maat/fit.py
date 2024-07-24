from .core import *

'''
This module contains functions for fitting and analyzing data.
'''


def plateau(spectra:Spectra, cuts:list, df_index:int=0):
    '''Fit the mean value of a plateau and its standard deviation.'''
    df = spectra.dataframe[df_index]
    df_range = df[(df[df.columns[0]] >= cuts[0]) & (df[df.columns[0]] <= cuts[1])]
    mean = df_range[df.columns[1]].mean()
    std = df_range[df.columns[1]].std()
    return mean, std


def area_under_peak(spectra:Spectra, peak:list, df_index:int=0, errors_as_in_baseline:bool=True, min_as_baseline:bool=False):
    '''
    peak:list=[xmin, xmax, baseline=0, baseline_error=0]\n
    If the dataset has no 'Error' column, the error in each point is assumed\n
    to be the same as the baseline error if `errors_as_in_baseline = True`,\n
    otherwise it is assumed to be zero.\n
    If `min_as_baseline = True` and baseline=0, the baseline is assumed to be the minimum value.\n
    Also, if `min_as_baseline=True` and there are negative areas after applying the baseline,\n
    the baseline will be set to the minimum value.
    '''
    if len(peak) < 2:
        raise ValueError("area_under_peak: peak must have at least two values: [xmin, xmax]")
    xmin = peak[0]
    xmax = peak[1]
    baseline = peak[2] if len(peak) >= 3 else 0.0
    baseline_error = peak[3] if len(peak) >= 4 else 0.0

    df = spectra.dataframe[df_index]
    df_range = df[(df[df.columns[0]] >= xmin) & (df[df.columns[0]] <= xmax)]
    x = df_range[df.columns[0]].to_numpy()
    y = df_range[df.columns[1]].to_numpy()
    
    min_y = y.min()
    if min_as_baseline and (baseline == 0 or baseline > min_y):
        baseline = min_y

    y = y - baseline

    area = scipy.integrate.simpson(y, x)

    if 'Error' in df_range.columns:
        point_errors = df_range['Error'].to_numpy()
    else: # Assume the error in each point is the same as the baseline error
        if errors_as_in_baseline == True:
            point_errors = np.full_like(y, baseline_error)
        else:
            point_errors = np.zeros_like(y)
    total_errors = np.sqrt(point_errors**2 + baseline_error**2)
    area_error = np.sqrt(scipy.integrate.simpson(total_errors**2, x))

    return area, area_error


def ratio_areas(area:float, area_total:float, area_error:float=0.0, area_total_error:float=0.0, inverse_ratio:bool=False):
    '''
    To check the ratio between two areas, e.g. to estimate deuteration levels from ATR data.\n
    The ratio is calculated as `area / area_total`. This behavior is modified if `inverse_ratio = True`,\n
    so that the ratio is calculated as `(area_total - area) / area_total`.\n
    Notice that changing the ratio calculation also affects the error propagation.
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


def mean_with_errors(values, errors):
    '''Calculate the mean value and corresponding errors.'''
    values = np.array(values)
    errors = np.array(errors)
    mean_value = np.mean(values)
    total_error = np.sqrt(np.sum(np.square(errors)))
    return mean_value, total_error

