import maat as mt
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score



'''
Tool to analyze MAI ATR data.\n
Working on Maat v1.1.0
'''

mt.run_here()

atr = mt.Spectra(
    type='ATR',
    title='ATR of H exchange in CH$_3$ND$_3$I at 75% RH over time',
    save_as=None,
    filename=[
        'data/ATR/MAI-ND_KS169_ref_ATR_raw.csv',
        'data/ATR/MAI-ND_KS169_10min@75%RH_ATR_raw.csv',
        'data/ATR/MAI-ND_KS169_30min@75%RH_ATR_raw.csv',
        'data/ATR/MAI-ND_KS169_60min@75%RH_ATR_raw.csv',
        'data/ATR/MAI-ND_KS169_120min@75%RH_ATR_raw.csv',
        'data/ATR/MAI-ND_KS169_360min@75%RH_ATR_raw.csv',
        'data/ATR/MAI-ND_KS169_900min@75%RH_ATR_raw.csv',
        'data/ATR/MAI_comGCSM_ATR_raw.csv'
        ],
    units_in=['cm-1'],
    units='cm-1',
    plotting=mt.Plotting(
        low_xlim=None,
        top_xlim=None,
        low_ylim=None,
        top_ylim=None,
        vline=None,
        figsize=None,
        offset=True,
        log_xscale=False,
        normalize=False,
        show_yticks=False,
        scale_factor=0.5,
        legend=[
            'MAI-ND_KS169',
            't = 10 min',
            't = 30 min',
            't = 60 min',
            't = 120 min',
            't = 360 min',
            't = 900 min',
            'MAI (GreatCell Solar Materials)'
            ],
        legend_title='Deuteration over time',
        ),
    scale_range=mt.ScaleRange(
        xmin=None,
        xmax=None,
        ymin=None,
        ymax=None,
        index=0,
        ),
    )

# Peak locations
# The protonated amine peak will be used as a reference for the deuteration levels.
peak_NH3 = [2600, 3350]
plateau_NH3 = [peak_NH3[0], 4000]
# We will extract the area under the dsCH3, dasCH3, and vCH3 peaks. We use the deuterated peaks as reference.
peak_dsCH3 = [2770, 2800]
peak_dasCH3 = [2865, 2895]
peak_vCH3 =[2945, 2975]
plateau_CH3 = [peak_dsCH3[1], peak_dasCH3[0]]

atr.plotting.vline = peak_NH3


# Normalize the height of the vCH3 peak
# 0
ymin_ND = -0.019
ymax_ND = 0.075
# 1
ymin_10 = -0.004
ymax_10 = 0.097
# 2
ymin_30 = 0.008
ymax_30 = 0.105
# 3
ymin_60 = 0.019
ymax_60 = 0.118
# 4
ymin_120 = 0.05
ymax_120 = 0.156
# 5
ymin_360 = 0.097
ymax_360 = 0.219
# 6
ymin_900 = 0.1975
ymax_900 = 0.3489
# 7
ymin_NH = 0.22
ymax_NH = 0.375

atr.scale_range.ymin = [ymin_ND, ymin_10, ymin_30, ymin_60, ymin_120, ymin_360, ymin_900, ymin_NH]
atr.scale_range.ymax = [ymax_ND, ymax_10, ymax_30, ymax_60, ymax_120, ymax_360, ymax_900, ymax_NH]
atr = mt.tools.normalize(atr)


baseline_CH3, baseline_CH3_error = mt.fit.plateau(atr, plateau_CH3, 0)

area_dsCH3, area_dsCH3_error = mt.fit.area_under_peak(atr, [peak_dsCH3[0], peak_dsCH3[1], baseline_CH3, baseline_CH3_error], 0, True)
area_dasCH3, area_dasCH3_error = mt.fit.area_under_peak(atr, [peak_dasCH3[0], peak_dasCH3[1], baseline_CH3, baseline_CH3_error], 0, True)
area_vCH3, area_vCH3_error = mt.fit.area_under_peak(atr, [peak_vCH3[0], peak_vCH3[1], baseline_CH3, baseline_CH3_error], 0, True)


baseline_ND, baseline_ND_error = mt.fit.plateau(atr, plateau_NH3, 0)
baseline_10, baseline_10_error = mt.fit.plateau(atr, plateau_NH3, 1)
baseline_30, baseline_30_error = mt.fit.plateau(atr, plateau_NH3, 2)
baseline_60, baseline_60_error = mt.fit.plateau(atr, plateau_NH3, 3)
baseline_120, baseline_120_error = mt.fit.plateau(atr, plateau_NH3, 4)
baseline_360, baseline_360_error = mt.fit.plateau(atr, plateau_NH3, 5)
baseline_900, baseline_900_error = mt.fit.plateau(atr, plateau_NH3, 6)
baseline_NH, baseline_NH_error = mt.fit.plateau(atr, plateau_NH3, 7)

area_ND, area_ND_error = mt.fit.area_under_peak(atr, [peak_NH3[0], peak_NH3[1], baseline_ND, baseline_ND_error], 0, True)
area_10, area_10_error = mt.fit.area_under_peak(atr, [peak_NH3[0], peak_NH3[1], baseline_10, baseline_10_error], 1, True)
area_30, area_30_error = mt.fit.area_under_peak(atr, [peak_NH3[0], peak_NH3[1], baseline_30, baseline_30_error], 2, True)
area_60, area_60_error = mt.fit.area_under_peak(atr, [peak_NH3[0], peak_NH3[1], baseline_60, baseline_60_error], 3, True)
area_120, area_120_error = mt.fit.area_under_peak(atr, [peak_NH3[0], peak_NH3[1], baseline_120, baseline_120_error], 4, True)
area_360, area_360_error = mt.fit.area_under_peak(atr, [peak_NH3[0], peak_NH3[1], baseline_360, baseline_360_error], 5, True)
area_900, area_900_error = mt.fit.area_under_peak(atr, [peak_NH3[0], peak_NH3[1], baseline_900, baseline_900_error], 6, True)
area_NH, area_NH_error = mt.fit.area_under_peak(atr, [peak_NH3[0], peak_NH3[1], baseline_NH, baseline_NH_error], 7, True)

area_ND = area_ND - area_dsCH3 - area_dasCH3 - area_vCH3
area_10 = area_10 - area_dsCH3 - area_dasCH3 - area_vCH3
area_30 = area_30 - area_dsCH3 - area_dasCH3 - area_vCH3
area_60 = area_60 - area_dsCH3 - area_dasCH3 - area_vCH3
area_120 = area_120 - area_dsCH3 - area_dasCH3 - area_vCH3
area_360 = area_360 - area_dsCH3 - area_dasCH3 - area_vCH3
area_900 = area_900 - area_dsCH3 - area_dasCH3 - area_vCH3
area_NH = area_NH - area_dsCH3 - area_dasCH3 - area_vCH3


area_ND_error = sqrt(area_ND_error**2 + area_dsCH3_error**2 + area_dasCH3_error**2 + area_vCH3_error**2)
area_10_error = sqrt(area_10_error**2 + area_dsCH3_error**2 + area_dasCH3_error**2 + area_vCH3_error**2)
area_30_error = sqrt(area_30_error**2 + area_dsCH3_error**2 + area_dasCH3_error**2 + area_vCH3_error**2)
area_60_error = sqrt(area_60_error**2 + area_dsCH3_error**2 + area_dasCH3_error**2 + area_vCH3_error**2)
area_120_error = sqrt(area_120_error**2 + area_dsCH3_error**2 + area_dasCH3_error**2 + area_vCH3_error**2)
area_360_error = sqrt(area_360_error**2 + area_dsCH3_error**2 + area_dasCH3_error**2 + area_vCH3_error**2)
area_900_error = sqrt(area_900_error**2 + area_dsCH3_error**2 + area_dasCH3_error**2 + area_vCH3_error**2)
area_NH_error = sqrt(area_NH_error**2 + area_dsCH3_error**2 + area_dasCH3_error**2 + area_vCH3_error**2)


deuteration_ND, deuteration_ND_error = mt.fit.ratio_areas(area_ND, area_NH, area_ND_error, area_NH_error, True)
deuteration_10, deuteration_10_error = mt.fit.ratio_areas(area_10, area_NH, area_10_error, area_NH_error, True)
deuteration_30, deuteration_30_error = mt.fit.ratio_areas(area_30, area_NH, area_30_error, area_NH_error, True)
deuteration_60, deuteration_60_error = mt.fit.ratio_areas(area_60, area_NH, area_60_error, area_NH_error, True)
deuteration_120, deuteration_120_error = mt.fit.ratio_areas(area_120, area_NH, area_120_error, area_NH_error, True)
deuteration_360, deuteration_360_error = mt.fit.ratio_areas(area_360, area_NH, area_360_error, area_NH_error, True)
deuteration_900, deuteration_900_error = mt.fit.ratio_areas(area_900, area_NH, area_900_error, area_NH_error, True)


atr.plotting.legend[0] = atr.plotting.legend[0] + f' ({deuteration_ND:.2f} ± {deuteration_ND_error:.2f})'
atr.plotting.legend[1] = atr.plotting.legend[1] + f' ({deuteration_10:.2f} ± {deuteration_10_error:.2f})'
atr.plotting.legend[2] = atr.plotting.legend[2] + f' ({deuteration_30:.2f} ± {deuteration_30_error:.2f})'
atr.plotting.legend[3] = atr.plotting.legend[3] + f' ({deuteration_60:.2f} ± {deuteration_60_error:.2f})'
atr.plotting.legend[4] = atr.plotting.legend[4] + f' ({deuteration_120:.2f} ± {deuteration_120_error:.2f})'
atr.plotting.legend[5] = atr.plotting.legend[5] + f' ({deuteration_360:.2f} ± {deuteration_360_error:.2f})'
atr.plotting.legend[6] = atr.plotting.legend[6] + f' ({deuteration_900:.2f} ± {deuteration_900_error:.2f})'


print('MAI-ND deuteration levels over time at 75% Relative Humidity')
print(f'Initial:  {deuteration_ND:.2f} ± {deuteration_ND_error:.2f}')
print(f'10 min:   {deuteration_10:.2f} ± {deuteration_10_error:.2f}')
print(f'30 min:   {deuteration_30:.2f} ± {deuteration_30_error:.2f}')
print(f'60 min:   {deuteration_60:.2f} ± {deuteration_60_error:.2f}')
print(f'120 min:  {deuteration_120:.2f} ± {deuteration_120_error:.2f}')
print(f'360 min:  {deuteration_360:.2f} ± {deuteration_360_error:.2f}')
print(f'900 min:  {deuteration_900:.2f} ± {deuteration_900_error:.2f}')

mt.plot.spectra(atr)



#############################################
## Fit of the deuterium exchange over time ##
#############################################
# Model for the H exchange
def model_1(t, a, b, c):
    return a * (np.log(t))**2 + b * np.log(t) + c
def model_2(t, a, b, c, d):
    return a * np.exp(-b * t) + c * np.exp(-d * t)     #######   EXPLORE THIS......

model = model_2

# Experimental data -> to % units
time = np.array([1, 10, 30, 60, 120, 360, 900])
deuteration = np.array([deuteration_ND, deuteration_10, deuteration_30, deuteration_60, deuteration_120, deuteration_360, deuteration_900]) * 100
deuteration_error = np.array([deuteration_ND_error, deuteration_10_error, deuteration_30_error, deuteration_60_error, deuteration_120_error, deuteration_360_error, deuteration_900_error]) * 100
# Fitting of the data to the model with scipy.curve_fit
popt, pcov = curve_fit(model, time, deuteration)
a, b, c, d = popt
# Calculation of R^2
deuteration_fitted = model(time, *popt)
R2 = r2_score(deuteration, deuteration_fitted)
print(f"Fitted parameters:  {popt},  R^2 = {R2}")
# HD fit for plotting
time_fit = np.linspace(min(time), max(time), 1000)
deuteration_fit = model(time_fit, *popt)
# Regression label to display in the plot. CHANGE ALONG WITH THE MODEL.
regression_text = f"$y = {a:+.1f} \cdot \ln(t)^2 {b:+.1f} \cdot \ln(t) {c:+.1f}$\n$R^2 = {R2:.2f}$"
#regression_text = f"$y = {a:+.5f} \cdot \exp(-{b:+.5f} sqrt(t) + {c:.5f}$\n$R^2 = {R2:.2f}$"
# Plotting
plt.text(x=1, y=10, s=regression_text, fontsize=10, bbox=None)
plt.plot(time, deuteration, 'o', label='ATR data')
plt.fill_between(time, deuteration - deuteration_error, deuteration + deuteration_error, color='C0', alpha=0.1)
plt.plot(time_fit, deuteration_fit, 'r', label='Fit')
plt.xlabel('Time / minutes')
plt.ylabel('Amine deuteration / %')
plt.title('Deuteration of CH$_3$ND$_3$I over time at 75% RH')
plt.ylim(0, 100)
plt.legend()
plt.xscale('log')
plt.show()

print(model(0, *popt))



''' BACKUP


# Data
time = np.array([1, 10, 30, 60, 120, 360, 900])
deuteration = np.array([deuteration_ND, deuteration_10, deuteration_30, deuteration_60, deuteration_120, deuteration_360, deuteration_900]) * 100
deuteration_error = np.array([deuteration_ND_error, deuteration_10_error, deuteration_30_error, deuteration_60_error, deuteration_120_error, deuteration_360_error, deuteration_900_error]) * 100

# Polynomial regression
coefficients = np.polyfit(np.log(time), deuteration, 2)  # 2nd degree for quadratic regression
quadratic_model = np.poly1d(coefficients)

a, b, c = coefficients
#c = 100
coefficients = a, b, c
regression = f"$y = {a:.1f} \cdot \log(t)^{2} {b:.1f} \cdot \log(t) + {c:.0f}$"
plt.text(x=1, y=0, s=regression, fontsize=10, bbox=None)

# Regression line
time_regression = np.linspace(min(time), max(time), 100)
deuteration_regression = quadratic_model(np.log(time_regression))

# Plotting
plt.plot(time, deuteration, 'o', label='ATR measurements')
plt.fill_between(time, deuteration - deuteration_error, deuteration + deuteration_error, color='C0', alpha=0.1)
plt.plot(time_regression, deuteration_regression, 'r', label='Fit')

plt.xlabel('Time / minutes')
plt.ylabel('Amine deuteration / %')
plt.title('Deuteration of CH$_3$ND$_3$I over time at 75% RH')
plt.xscale('log')
plt.legend()
plt.show()



'''