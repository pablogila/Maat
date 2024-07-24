import maat as mt
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score


'''
Script to analyze deuterated MAI ATR data.\n
Working on Maat v1.2.0
'''

mt.run_here()

atr = mt.Spectra(
    type='ATR',
    title='ATR of H exchange in CH$_3$ND$_3$I at 75% RH over time',
    save_as=None,
    filename=[
        'data/ATR/MAI-ND_KS169_ref_ATR_corrected_raw.csv',
        'data/ATR/MAI-ND_KS169_10min@75%RH_ATR_corrected_raw.csv',
        'data/ATR/MAI-ND_KS169_30min@75%RH_ATR_corrected_raw.csv',
        'data/ATR/MAI-ND_KS169_60min@75%RH_ATR_corrected_raw.csv',
        'data/ATR/MAI-ND_KS169_120min@75%RH_ATR_corrected_raw.csv',
        'data/ATR/MAI-ND_KS169_360min@75%RH_ATR_corrected_raw.csv',
        'data/ATR/MAI-ND_KS169_900min@75%RH_ATR_corrected_raw.csv',
        'data/ATR/MAI_comGCSM_ATR_corrected_raw.csv'
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
        scale_factor=0.8,
        legend=[
            't = 1 min',
            't = 10 min',
            't = 30 min',
            't = 60 min',
            't = 120 min',
            't = 360 min',
            't = 900 min',
            'MAI (GreatCell Solar Materials)'
            ],
        legend_title='Sample MAI-ND_KS169 over time',
        ),
    scale_range=mt.ScaleRange(
        xmin=None,
        xmax=None,
        ymin=None,
        ymax=None,
        index=0,
        ),
    )

######################
##  Peak locations  ##
######################
# Two amine peaks are used to estimate the deuteration levels.
# The first amine peak (dNH3) is at 1560 cm-1, which is isolated, but quite small.
peak_dNH3 = [1520, 1600]
plateau_dNH3 = [peak_dNH3[1], 1800]
# The second amine peak (vNH3) is at 3080 cm-1, which is big and easy to identify, but comes with three additional CH3 peaks.
peak_vNH3 = [2650, 3300]
plateau_vNH3 = [peak_vNH3[1], 4000]
# To estimate the area from the second amine peak, we will subtract the area under the additional CH3 peaks, dsCH3, dasCH3, and vCH3 peaks.
peak_dsCH3 = [2770, 2800]
peak_dasCH3 = [2865, 2895]
peak_vCH3 =[2945, 2975]
plateau_CH3 = [peak_dsCH3[1], peak_dasCH3[0]]

# Show the range of the peaks in the plot
atr.plotting.vline = peak_dNH3 + peak_vNH3

# Before anything, we must normalize all the spectra. For that we use the height of the vCH3 peak.
# 0
ymin_ND = 0.035
ymax_ND = 0.405
# 1
ymin_10 = 0.124
ymax_10 = 0.563
# 2
ymin_30 = 0.173
ymax_30 = 0.609
# 3
ymin_60 = 0.231
ymax_60 = 0.693
# 4
ymin_120 = 0.4005
ymax_120 = 0.962
# 5
ymin_360 = 0.4787
ymax_360 = 0.959
# 6
ymin_900 = 0.5716
ymax_900 = 0.961
# 7
ymin_NH = 0.5846
ymax_NH = 0.9635

atr.scale_range.ymin = [ymin_ND, ymin_10, ymin_30, ymin_60, ymin_120, ymin_360, ymin_900, ymin_NH]
atr.scale_range.ymax = [ymax_ND, ymax_10, ymax_30, ymax_60, ymax_120, ymax_360, ymax_900, ymax_NH]
atr = mt.tools.normalize(atr)


#################################################
##  Estimation from the 1st amine peak (dNH3)  ##
#################################################
# Baselines
baseline_dND, baseline_dND_error = mt.fit.plateau(atr, plateau_dNH3, 0)
baseline_d10, baseline_d10_error = mt.fit.plateau(atr, plateau_dNH3, 1)
baseline_d30, baseline_d30_error = mt.fit.plateau(atr, plateau_dNH3, 2)
baseline_d60, baseline_d60_error = mt.fit.plateau(atr, plateau_dNH3, 3)
baseline_d120, baseline_d120_error = mt.fit.plateau(atr, plateau_dNH3, 4)
baseline_d360, baseline_d360_error = mt.fit.plateau(atr, plateau_dNH3, 5)
baseline_d900, baseline_d900_error = mt.fit.plateau(atr, plateau_dNH3, 6)
baseline_dNH, baseline_dNH_error = mt.fit.plateau(atr, plateau_dNH3, 7)
# Areas
area_dND, area_dND_error = mt.fit.area_under_peak(atr, [peak_dNH3[0], peak_dNH3[1], baseline_dND, baseline_dND_error], 0, True)
area_d10, area_d10_error = mt.fit.area_under_peak(atr, [peak_dNH3[0], peak_dNH3[1], baseline_d10, baseline_d10_error], 1, True)
area_d30, area_d30_error = mt.fit.area_under_peak(atr, [peak_dNH3[0], peak_dNH3[1], baseline_d30, baseline_d30_error], 2, True)
area_d60, area_d60_error = mt.fit.area_under_peak(atr, [peak_dNH3[0], peak_dNH3[1], baseline_d60, baseline_d60_error], 3, True)
area_d120, area_d120_error = mt.fit.area_under_peak(atr, [peak_dNH3[0], peak_dNH3[1], baseline_d120, baseline_d120_error], 4, True)
area_d360, area_d360_error = mt.fit.area_under_peak(atr, [peak_dNH3[0], peak_dNH3[1], baseline_d360, baseline_d360_error], 5, True)
area_d900, area_d900_error = mt.fit.area_under_peak(atr, [peak_dNH3[0], peak_dNH3[1], baseline_d900, baseline_d900_error], 6, True)
area_dNH, area_dNH_error = mt.fit.area_under_peak(atr, [peak_dNH3[0], peak_dNH3[1], baseline_dNH, baseline_dNH_error], 7, True)
# Ratios
deuteration_dND, deuteration_dND_error = mt.fit.ratio_areas(area_dND, area_dNH, area_dND_error, area_dNH_error, True)
deuteration_d10, deuteration_d10_error = mt.fit.ratio_areas(area_d10, area_dNH, area_d10_error, area_dNH_error, True)
deuteration_d30, deuteration_d30_error = mt.fit.ratio_areas(area_d30, area_dNH, area_d30_error, area_dNH_error, True)
deuteration_d60, deuteration_d60_error = mt.fit.ratio_areas(area_d60, area_dNH, area_d60_error, area_dNH_error, True)
deuteration_d120, deuteration_d120_error = mt.fit.ratio_areas(area_d120, area_dNH, area_d120_error, area_dNH_error, True)
deuteration_d360, deuteration_d360_error = mt.fit.ratio_areas(area_d360, area_dNH, area_d360_error, area_dNH_error, True)
deuteration_d900, deuteration_d900_error = mt.fit.ratio_areas(area_d900, area_dNH, area_d900_error, area_dNH_error, True)


#################################################
##  Estimation from the 2nd amine peak (vNH3)  ##
#################################################

# CH3 baseline
baseline_CH3, baseline_CH3_error = mt.fit.plateau(atr, plateau_CH3, 0)
# CH3 areas and errors
area_dsCH3, area_dsCH3_error = mt.fit.area_under_peak(atr, [peak_dsCH3[0], peak_dsCH3[1], baseline_CH3, baseline_CH3_error], 0, True)
area_dasCH3, area_dasCH3_error = mt.fit.area_under_peak(atr, [peak_dasCH3[0], peak_dasCH3[1], baseline_CH3, baseline_CH3_error], 0, True)
area_vCH3, area_vCH3_error = mt.fit.area_under_peak(atr, [peak_vCH3[0], peak_vCH3[1], baseline_CH3, baseline_CH3_error], 0, True)
# CH3 total area and error
area_CH3 = area_dsCH3 + area_dasCH3 + area_vCH3
area_CH3_error = sqrt(area_dsCH3_error**2 + area_dasCH3_error**2 + area_vCH3_error**2)
# vNH3 baselines
baseline_vND, baseline_vND_error = mt.fit.plateau(atr, plateau_vNH3, 0)
baseline_v10, baseline_v10_error = mt.fit.plateau(atr, plateau_vNH3, 1)
baseline_v30, baseline_v30_error = mt.fit.plateau(atr, plateau_vNH3, 2)
baseline_v60, baseline_v60_error = mt.fit.plateau(atr, plateau_vNH3, 3)
baseline_v120, baseline_v120_error = mt.fit.plateau(atr, plateau_vNH3, 4)
baseline_v360, baseline_v360_error = mt.fit.plateau(atr, plateau_vNH3, 5)
baseline_v900, baseline_v900_error = mt.fit.plateau(atr, plateau_vNH3, 6)
baseline_vNH, baseline_vNH_error = mt.fit.plateau(atr, plateau_vNH3, 7)
# vNH3 areas and errors
area_vND, area_vND_error = mt.fit.area_under_peak(atr, [peak_vNH3[0], peak_vNH3[1], baseline_vND, baseline_vND_error], 0, True, True)
area_v10, area_v10_error = mt.fit.area_under_peak(atr, [peak_vNH3[0], peak_vNH3[1], baseline_v10, baseline_v10_error], 1, True, True)
area_v30, area_v30_error = mt.fit.area_under_peak(atr, [peak_vNH3[0], peak_vNH3[1], baseline_v30, baseline_v30_error], 2, True, True)
area_v60, area_v60_error = mt.fit.area_under_peak(atr, [peak_vNH3[0], peak_vNH3[1], baseline_v60, baseline_v60_error], 3, True, True)
area_v120, area_v120_error = mt.fit.area_under_peak(atr, [peak_vNH3[0], peak_vNH3[1], baseline_v120, baseline_v120_error], 4, True, True)
area_v360, area_v360_error = mt.fit.area_under_peak(atr, [peak_vNH3[0], peak_vNH3[1], baseline_v360, baseline_v360_error], 5, True, True)
area_v900, area_v900_error = mt.fit.area_under_peak(atr, [peak_vNH3[0], peak_vNH3[1], baseline_v900, baseline_v900_error], 6, True, True)
area_vNH, area_vNH_error = mt.fit.area_under_peak(atr, [peak_vNH3[0], peak_vNH3[1], baseline_vNH, baseline_vNH_error], 7, True, True)
# Subtract the CH3 area from the vNH3 areas
area_vND = area_vND - area_CH3
area_v10 = area_v10 - area_CH3
area_v30 = area_v30 - area_CH3
area_v60 = area_v60 - area_CH3
area_v120 = area_v120 - area_CH3
area_v360 = area_v360 - area_CH3
area_v900 = area_v900 - area_CH3
area_vNH = area_vNH - area_CH3
# Propagate the errors
area_vND_error = sqrt(area_vND_error**2 + area_CH3_error**2)
area_v10_error = sqrt(area_v10_error**2 + area_CH3_error**2)
area_v30_error = sqrt(area_v30_error**2 + area_CH3_error**2)
area_v60_error = sqrt(area_v60_error**2 + area_CH3_error**2)
area_v120_error = sqrt(area_v120_error**2 + area_CH3_error**2)
area_v360_error = sqrt(area_v360_error**2 + area_CH3_error**2)
area_v900_error = sqrt(area_v900_error**2 + area_CH3_error**2)
area_vNH_error = sqrt(area_vNH_error**2 + area_CH3_error**2)
# Ratios
deuteration_vND, deuteration_vND_error = mt.fit.ratio_areas(area_vND, area_vNH, area_vND_error, area_vNH_error, True)
deuteration_v10, deuteration_v10_error = mt.fit.ratio_areas(area_v10, area_vNH, area_v10_error, area_vNH_error, True)
deuteration_v30, deuteration_v30_error = mt.fit.ratio_areas(area_v30, area_vNH, area_v30_error, area_vNH_error, True)
deuteration_v60, deuteration_v60_error = mt.fit.ratio_areas(area_v60, area_vNH, area_v60_error, area_vNH_error, True)
deuteration_v120, deuteration_v120_error = mt.fit.ratio_areas(area_v120, area_vNH, area_v120_error, area_vNH_error, True)
deuteration_v360, deuteration_v360_error = mt.fit.ratio_areas(area_v360, area_vNH, area_v360_error, area_vNH_error, True)
deuteration_v900, deuteration_v900_error = mt.fit.ratio_areas(area_v900, area_vNH, area_v900_error, area_vNH_error, True)

################################################
##  Mean estimation from the two amine peaks  ##
################################################
deuteration_ND, deuteration_ND_error = mt.fit.mean_with_errors([deuteration_dND, deuteration_vND], [deuteration_dND_error, deuteration_vND_error])
deuteration_10, deuteration_10_error = mt.fit.mean_with_errors([deuteration_d10, deuteration_v10], [deuteration_d10_error, deuteration_v10_error])
deuteration_30, deuteration_30_error = mt.fit.mean_with_errors([deuteration_d30, deuteration_v30], [deuteration_d30_error, deuteration_v30_error])
deuteration_60, deuteration_60_error = mt.fit.mean_with_errors([deuteration_d60, deuteration_v60], [deuteration_d60_error, deuteration_v60_error])
deuteration_120, deuteration_120_error = mt.fit.mean_with_errors([deuteration_d120, deuteration_v120], [deuteration_d120_error, deuteration_v120_error])
deuteration_360, deuteration_360_error = mt.fit.mean_with_errors([deuteration_d360, deuteration_v360], [deuteration_d360_error, deuteration_v360_error])
deuteration_900, deuteration_900_error = mt.fit.mean_with_errors([deuteration_d900, deuteration_v900], [deuteration_d900_error, deuteration_v900_error])

print('\nMAI-ND deuteration levels over time at 75% Relative Humidity:')
print('\nEstimations from dNH3 +- dNH3 error / vNH3 +- vNH3 error')
print(f'1 min:    {deuteration_dND:.2f} ± {deuteration_dND_error:.3f} / {deuteration_vND:.2f} ± {deuteration_vND_error:.3f}')
print(f'10 min:   {deuteration_d10:.2f} ± {deuteration_d10_error:.3f} / {deuteration_v10:.2f} ± {deuteration_v10_error:.3f}')
print(f'30 min:   {deuteration_d30:.2f} ± {deuteration_d30_error:.3f} / {deuteration_v30:.2f} ± {deuteration_v30_error:.3f}')
print(f'60 min:   {deuteration_d60:.2f} ± {deuteration_d60_error:.3f} / {deuteration_v60:.2f} ± {deuteration_v60_error:.3f}')
print(f'120 min:  {deuteration_d120:.2f} ± {deuteration_d120_error:.3f} / {deuteration_v120:.2f} ± {deuteration_v120_error:.3f}')
print(f'360 min:  {deuteration_d360:.2f} ± {deuteration_d360_error:.3f} / {deuteration_v360:.2f} ± {deuteration_v360_error:.3f}')
print(f'900 min:  {deuteration_d900:.2f} ± {deuteration_d900_error:.3f} / {deuteration_v900:.2f} ± {deuteration_v900_error:.3f}')
print('\nMean values:')
print(f'1 min:    {deuteration_ND:.2f} ± {deuteration_ND_error:.2f}')
print(f'10 min:   {deuteration_10:.2f} ± {deuteration_10_error:.2f}')
print(f'30 min:   {deuteration_30:.2f} ± {deuteration_30_error:.2f}')
print(f'60 min:   {deuteration_60:.2f} ± {deuteration_60_error:.2f}')
print(f'120 min:  {deuteration_120:.2f} ± {deuteration_120_error:.2f}')
print(f'360 min:  {deuteration_360:.2f} ± {deuteration_360_error:.2f}')
print(f'900 min:  {deuteration_900:.2f} ± {deuteration_900_error:.2f}')
print('')

# Plotting of the spectra
atr.plotting.legend[0] = atr.plotting.legend[0] + f' ({deuteration_ND:.2f} ± {deuteration_ND_error:.2f})'
atr.plotting.legend[1] = atr.plotting.legend[1] + f' ({deuteration_10:.2f} ± {deuteration_10_error:.2f})'
atr.plotting.legend[2] = atr.plotting.legend[2] + f' ({deuteration_30:.2f} ± {deuteration_30_error:.2f})'
atr.plotting.legend[3] = atr.plotting.legend[3] + f' ({deuteration_60:.2f} ± {deuteration_60_error:.2f})'
atr.plotting.legend[4] = atr.plotting.legend[4] + f' ({deuteration_120:.2f} ± {deuteration_120_error:.2f})'
atr.plotting.legend[5] = atr.plotting.legend[5] + f' ({deuteration_360:.2f} ± {deuteration_360_error:.2f})'
atr.plotting.legend[6] = atr.plotting.legend[6] + f' ({deuteration_900:.2f} ± {deuteration_900_error:.2f})'
mt.plot.spectra(atr)


#############################################
## Fit of the deuterium exchange over time ##
#############################################
# Model for the H exchange, with 2 exponential decays:
# DDD -> DDH
# DDH -> DHH  (and  DHH -> HHH, yet we assume it to be negligible)
def model(t, A1, k1, A2, k2):
    return A1 * np.exp(-k1 * t) + A2 * np.exp(-k2 * t)
# Experimental data -> to % units
time = np.array([1, 10, 30, 60, 120, 360, 900])
deuteration = np.array([deuteration_ND, deuteration_10, deuteration_30, deuteration_60, deuteration_120, deuteration_360, deuteration_900]) * 100
deuteration_error = np.array([deuteration_ND_error, deuteration_10_error, deuteration_30_error, deuteration_60_error, deuteration_120_error, deuteration_360_error, deuteration_900_error]) * 100
# Fitting of the data to the model with scipy.curve_fit
popt, pcov = curve_fit(model, time, deuteration, p0=[50, 0.1, 50, 0])
A1, k1, A2, k2 = popt
# Calculation of R^2
deuteration_fitted = model(time, *popt)
R2 = r2_score(deuteration, deuteration_fitted)
print(f"Fitted parameters:  {popt},  R^2 = {R2}")
# Estimated initial deuteration at t=0
initial_deuteration = model(0, *popt)
initial_deuteration_error_pcov = sqrt(pcov[0, 0] + pcov[2, 2])  # Fitting error
initial_deuteration_error_exp = np.mean(deuteration_error)  # Experimental error
initial_deuteration_error = np.sqrt(initial_deuteration_error_exp**2 + initial_deuteration_error_pcov**2)  # Combined errors
print(f"Estimated initial deuteration at t=0: {initial_deuteration:.0f} ± {initial_deuteration_error:.0f} %")
# HD fit for plotting
time_fit = np.linspace(0, 10000, 100000)
deuteration_fit = model(time_fit, *popt)
# Regression label to display in the plot. CHANGE ALONG WITH THE MODEL.
regression_text = f"$D(t) = {A1:.1f} \cdot \exp(-{k1:.3f}) + {A2:.1f} \cdot \exp(-{k2:.3f})$\n$R^2 = {R2:.2f}$\nD(t=0) = {initial_deuteration:.0f} ± {initial_deuteration_error:.0f}%"
# Plotting
plt.text(x=0.15, y=5, s=regression_text, fontsize=10, bbox=None)
plt.plot(time, deuteration, 'o', label='ATR data')
plt.fill_between(time, deuteration - deuteration_error, deuteration + deuteration_error, color='C0', alpha=0.1)
plt.plot(time_fit, deuteration_fit, 'r', label='Fit')
plt.xlabel('Time / minutes')
plt.ylabel('Amine deuteration / %')
plt.title('Deuterium exchange of CH$_3$ND$_3$I over time at 75% RH')
plt.ylim(0, 100)
plt.xlim(0.1, 10000)
plt.legend()
plt.xscale('log')
plt.show()

