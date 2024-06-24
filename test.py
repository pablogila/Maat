import maat as mt


ins = mt.Spectra(
    filename=['CH3NH3PbI3.csv', 'IREPA-ND-02_INS.csv', 'CH3ND3PbI3.csv', 'manley2020-CDND.csv'],
    title=None,
    type='INS',
    save_as=None,
    units_in=['cm', 'cm', 'cm', 'mev'],
    units='meV',
    low_xlim=3,
    top_xlim=50,
    low_ylim=-0.1,
    top_ylim=None,
    figsize=(7,10),
    offset=True,
    log_xscale=False,
    show_yticks=False,
    #legend=['CH3NH3PbI3', 'IREPA-MAPI-02', 'CH3ND3PbI3', 'manley2020-CDND'],
    #scale_range=[None, None, 1.0],
    atoms=mt.MAPI,
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
deuteration_H = mt.deuteration.mapi_peaks(ins=ins, peaks=peaks, df_index=0)

# Deuterated samples

peaks['baseline'], peaks['baseline_error'] = mt.fit.plateau(spectra=ins, cuts=plateau_02, df_index=1)
deuteration_02 = mt.deuteration.mapi_peaks(ins=ins, peaks=peaks, df_index=1)

peaks['baseline'], peaks['baseline_error'] = mt.fit.plateau(spectra=ins, cuts=plateau_03, df_index=2)
deuteration_03 = mt.deuteration.mapi_peaks(ins=ins, peaks=peaks, df_index=2)

# Manley2020-CDND sample
peaks_manley['baseline'], peaks_manley['baseline_error'] = mt.fit.plateau(spectra=ins, cuts=plateau_manley, df_index=3)
deuteration_manley = mt.deuteration.mapi_peaks(ins=ins, peaks=peaks_manley, df_index=3)

ins.legend = ['MAPI-12: ' + deuteration_H, 'ND-02:    ' + deuteration_02, 'ND-03:    ' + deuteration_03, 'manley:  ' + deuteration_manley]

mt.plot.spectra(ins)