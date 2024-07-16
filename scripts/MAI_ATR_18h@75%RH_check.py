import maat as mt
from math import sqrt


'''
Tool to analyze MAI ATR data.\n
Working on Maat v1.0.2
'''


atr = mt.Spectra(
    type='ATR',
    title='ATR MAI vs dried MAI previously under moisture',
    save_as=None,
    filename=[
        'data/ATR/MAI_comGCSM_ATR_raw.csv',
        'data/ATR/MAI_comGCSM_18h@75%RH_ATR_raw.csv'
        ],
    units_in=['cm-1'],
    units='cm-1',
    plotting=mt.Plotting(
        low_xlim=None,
        top_xlim=None,
        low_ylim=None,
        top_ylim=None,
        figsize=None,
        offset=True,
        log_xscale=False,
        normalize=True,
        show_yticks=False,
        scale_factor=1.1,
        legend=['MAI (GreatCell Solar Materials)', 'MAI 18h@75%RH']
        ),
    scale_range=mt.ScaleRange(
        xmin=None,
        xmax=None,
        ymin=None,
        ymax=None,
        index=0,
        ),
    )


ymin_MAI = 0.22
ymax_MAI = 0.375
ymin_18h = 0.22
ymax_18h = 0.353

atr.scale_range.ymin = [ymin_MAI, ymin_18h]
atr.scale_range.ymax = [ymax_MAI, ymax_18h]

mt.plot.spectra(atr)

