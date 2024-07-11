import maat as mt


'''
Tool to analyze MAPI deuteration with INS data from TOSCA and other papers,\n
based on the peaks of the disrotatory mode of the methylammonium cation.\n
Working on Maat v1.0.2
'''


ins = mt.Spectra(
    type='INS',
    title=None,
    save_as=None,
    filename=[
        'data/INS/IREPA-MAPI-12_INS_2.02g_cellsubtracted.csv',
        'data/INS/IREPA-ND-02_INS_1.284g_20K_cellsubtracted.csv',
        'data/INS/IREPA-ND-03_INS_2.672g_cellsubtracted.csv',
        'data/INS/manley2020-CDND_INS.csv'
        ],
    units_in=['cm', 'cm', 'cm', 'mev'],
    units='meV',
    plotting=mt.Plotting(
        low_xlim=3,
        top_xlim=50,
        low_ylim=-0.1,
        top_ylim=None,
        figsize=(7,10),
        offset=True,
        log_xscale=False,
        normalize=False,
        show_yticks=False,
        ),
    scale_range=mt.ScaleRange(
        xmin=None,
        xmax=None,
        index=0,
        ),
    )

peaks = {
    'baseline' : None,
    'baseline_error' : None,
    'h6d0' : [36.0, 39.0],
    'h5d1' : [33.0, 35.0],
    'h4d2' : [30.7, 33.0],
    'h3d3' : [28.8, 30.7],
    }

peaks_manley = {
    'baseline' : None,
    'baseline_error' : None,
    'h6d0' : [41, 43],
    'h5d1' : [41, 43],
    'h4d2' : [41, 43],
    'h3d3' : [34.7, 37.3],
    'h2d4' : [31.0, 33.0],
    'h1d5' : [28.0, 30.5],
    'h0d6' : [26.5, 28.0],
    }

plateau_H = [30, 35]
plateau_02 = [39, 50]
plateau_03 = [35, 50]
plateau_manley = [41, 43]

# Protonated sample
peaks['baseline'], peaks['baseline_error'] = mt.fit.plateau(spectra=ins, cuts=plateau_H, df_index=0)
deuteration_H = mt.deuteration.peaks_mapi(ins=ins, peaks=peaks, df_index=0)

# Deuterated samples

peaks['baseline'], peaks['baseline_error'] = mt.fit.plateau(spectra=ins, cuts=plateau_02, df_index=1)
deuteration_02 = mt.deuteration.peaks_mapi(ins=ins, peaks=peaks, df_index=1)

peaks['baseline'], peaks['baseline_error'] = mt.fit.plateau(spectra=ins, cuts=plateau_03, df_index=2)
deuteration_03 = mt.deuteration.peaks_mapi(ins=ins, peaks=peaks, df_index=2)

# Manley2020-CDND sample
peaks_manley['baseline'], peaks_manley['baseline_error'] = mt.fit.plateau(spectra=ins, cuts=plateau_manley, df_index=3)
deuteration_manley = mt.deuteration.peaks_mapi(ins=ins, peaks=peaks_manley, df_index=3)

ins.plotting.legend = ['MAPI-12: ' + deuteration_H, 'ND-02:    ' + deuteration_02, 'ND-03:    ' + deuteration_03, 'manley:  ' + deuteration_manley]

mt.plot.spectra(ins)

