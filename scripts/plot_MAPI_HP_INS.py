import maat as mt
from math import sqrt


ins = mt.Spectra(
    type='INS',
    title='INS of MAPbI$_3$ under High Pressure at TOSCA',
    save_as=None,
    filename=[
        'data/INS/MAPI_comXPLT_INS_1.9GPa_smooth_cellsubtracted.csv',
        'data/INS/IREPA-ND-03_INS_1.9GPa_smooth_cellsubtracted.csv'
        ],
    units_in=['cm-1'],
    units='meV',
    plotting=mt.Plotting(
        low_xlim=3,
        top_xlim=50,
        low_ylim=None,
        top_ylim=None,
        vline=[30.35, 32.9],
        vline_error=None,
        figsize=None,
        offset=True,
        log_xscale=False,
        normalize=False,
        show_yticks=False,
        scale_factor = 1.0,
        legend=['CH$_3$NH$_3$PbI$_3$ 1.9GPa', 'CH$_3$ND$_3$PbI$_3$ 1.9GPa']
        ),
    scale_range=mt.ScaleRange(
        xmin=None,
        xmax=None,
        ymin=None,
        ymax=None,
        index=0,
        ),
    )

mt.plot.spectra(ins)

