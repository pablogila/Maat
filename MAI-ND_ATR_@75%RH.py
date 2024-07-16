import maat as mt
from math import sqrt


'''
Tool to analyze MAI ATR data.\n
Working on Maat v1.0.2
'''


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
            'MAI-ND (KS169)',
            't = 10 min',
            't = 30 min',
            't = 60 min',
            't = 120 min',
            't = 360 min',
            'MAI (GreatCell Solar Materials)'
            ],
        ),
    scale_range=mt.ScaleRange(
        xmin=None,
        xmax=None,
        ymin=None,
        ymax=None,
        index=0,
        ),
    )

# Peaks
peak_C =[2945, 2975]
peak_extra = [2865, 2895]
baseline_extra = -0.0225
peak_H = [2800, 3350]
plateau = [peak_H[0], 4000]


# Normalize the height of the C peak
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
ymin_NH = 0.22
ymax_NH = 0.375


atr.scale_range.ymin = [ymin_ND, ymin_10, ymin_30, ymin_60, ymin_120, ymin_360, ymin_NH]
atr.scale_range.ymax = [ymax_ND, ymax_10, ymax_30, ymax_60, ymax_120, ymax_360, ymax_NH]

atr = mt.tools.normalize(atr)

atr.plotting.vline = peak_H

baseline_ND, baseline_ND_error = mt.fit.plateau(atr, plateau, 0)
baseline_10, baseline_10_error = mt.fit.plateau(atr, plateau, 1)
baseline_30, baseline_30_error = mt.fit.plateau(atr, plateau, 2)
baseline_60, baseline_60_error = mt.fit.plateau(atr, plateau, 3)
baseline_120, baseline_120_error = mt.fit.plateau(atr, plateau, 4)
baseline_360, baseline_360_error = mt.fit.plateau(atr, plateau, 5)
baseline_NH, baseline_NH_error = mt.fit.plateau(atr, plateau, 6)

baseline_C = ymin_ND
baseline_C_error = baseline_ND_error
baseline_extra_error = baseline_ND_error

area_C, area_C_error = mt.fit.area_under_peak(atr, [peak_C[0], peak_C[1], baseline_C, baseline_C_error], 0)
area_extra, area_extra_error = mt.fit.area_under_peak(atr, [peak_extra[0], peak_extra[1], baseline_extra, baseline_extra_error], 0)

area_ND, area_ND_error = mt.fit.area_under_peak(atr, [peak_H[0], peak_H[1], baseline_ND, baseline_ND_error], 0)
area_10, area_10_error = mt.fit.area_under_peak(atr, [peak_H[0], peak_H[1], baseline_10, baseline_10_error], 1)
area_30, area_30_error = mt.fit.area_under_peak(atr, [peak_H[0], peak_H[1], baseline_30, baseline_30_error], 2)
area_60, area_60_error = mt.fit.area_under_peak(atr, [peak_H[0], peak_H[1], baseline_60, baseline_60_error], 3)
area_120, area_120_error = mt.fit.area_under_peak(atr, [peak_H[0], peak_H[1], baseline_120, baseline_120_error], 4)
area_360, area_360_error = mt.fit.area_under_peak(atr, [peak_H[0], peak_H[1], baseline_360, baseline_360_error], 5)
area_NH, area_NH_error = mt.fit.area_under_peak(atr, [peak_H[0], peak_H[1], baseline_NH, baseline_NH_error], 6)

area_ND = area_ND - area_C - area_extra
area_10 = area_10 - area_C - area_extra
area_30 = area_30 - area_C - area_extra
area_60 = area_60 - area_C - area_extra
area_120 = area_120 - area_C - area_extra
area_360 = area_360 - area_C - area_extra
area_NH = area_NH - area_C - area_extra


area_ND_error = sqrt(area_ND_error**2 + area_C_error**2 + area_extra_error**2)
area_10_error = sqrt(area_10_error**2 + area_C_error**2 + area_extra_error**2)
area_30_error = sqrt(area_30_error**2 + area_C_error**2 + area_extra_error**2)
area_60_error = sqrt(area_60_error**2 + area_C_error**2 + area_extra_error**2)
area_120_error = sqrt(area_120_error**2 + area_C_error**2 + area_extra_error**2)
area_360_error = sqrt(area_360_error**2 + area_C_error**2 + area_extra_error**2)
area_NH_error = sqrt(area_NH_error**2 + area_C_error**2 + area_extra_error**2)


deuteration_ND, deuteration_ND_error = mt.fit.ratio_areas(area_ND, area_NH, area_ND_error, area_NH_error)
deuteration_10, deuteration_10_error = mt.fit.ratio_areas(area_10, area_NH, area_10_error, area_NH_error)
deuteration_30, deuteration_30_error = mt.fit.ratio_areas(area_30, area_NH, area_30_error, area_NH_error)
deuteration_60, deuteration_60_error = mt.fit.ratio_areas(area_60, area_NH, area_60_error, area_NH_error)
deuteration_120, deuteration_120_error = mt.fit.ratio_areas(area_120, area_NH, area_120_error, area_NH_error)
deuteration_360, deuteration_360_error = mt.fit.ratio_areas(area_360, area_NH, area_360_error, area_NH_error)


print('MAI-ND deuteration levels over time at 75% Relative Humidity')
print(f'Initial:  {deuteration_ND:.2f} ± {deuteration_ND_error:.2f}')
print(f'10 min:   {deuteration_10:.2f} ± {deuteration_10_error:.2f}')
print(f'30 min:   {deuteration_30:.2f} ± {deuteration_30_error:.2f}')
print(f'60 min:   {deuteration_60:.2f} ± {deuteration_60_error:.2f}')
print(f'120 min:  {deuteration_120:.2f} ± {deuteration_120_error:.2f}')
print(f'360 min:  {deuteration_360:.2f} ± {deuteration_360_error:.2f}')

mt.plot.spectra(atr)

