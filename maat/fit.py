from .core import *


def plateau(spectra:Spectra, cuts=[27,35], df_index:int=0):
    df = spectra.dataframe[df_index]
    df_range = df[(df[df.columns[0]] >= cuts[0]) & (df[df.columns[0]] <= cuts[1])]
    x = df_range[df.columns[0]]
    y = df_range[df.columns[1]]

    if 'Error' in df_range.columns:

        error_range = df_range['Error']

        # Perform a weighted least squares fit
        degree = 1
        weights = 1.0 / error_range**2
        coefficients = np.polyfit(x, y, degree, w=weights)
        polynomial = np.poly1d(coefficients)

    else:
        # Perform a least squares fit
        degree = 1
        coefficients = np.polyfit(x, y, degree)
        polynomial = np.poly1d(coefficients)

    # Calculate the baseline
    baseline = polynomial(x)

    # Calculate the standard deviation of the residuals
    residuals = y - baseline
    error_std = np.std(residuals)

    baseline_value = np.mean(baseline)

    return baseline_value, error_std


def area_under_peak(spectra:Spectra, peak:list, df_index:int=0):
    '''area, area_error = area_under_peak(spectra, peak=[xmin, xmax, baseline=0.0, baseline_error=0.0], df_index=0)'''
    if len(peak) < 2:
        raise ValueError("area_under_peak: peak must have at least two values: [xmin, xmax]")
    xmin = peak[0]
    xmax = peak[1]
    baseline = peak[2] if len(peak) >= 3 else 0.0
    baseline_error = peak[3] if len(peak) >= 4 else 0.0

    df = spectra.dataframe[df_index]
    df_range = df[(df[df.columns[0]] >= xmin) & (df[df.columns[0]] <= xmax)]
    x = df_range[df.columns[0]].to_numpy()
    y = df_range[df.columns[1]].to_numpy() - baseline
    area = scipy.integrate.simpson(y, x)

    if 'Error' in df_range.columns:
        point_errors = df_range['Error'].to_numpy()
    else:
        point_errors = np.zeros_like(y)
    total_errors = np.sqrt(point_errors**2 + baseline_error**2)
    area_error = np.sqrt(scipy.integrate.simpson(total_errors**2, x))

    return area, area_error

