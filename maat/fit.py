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

