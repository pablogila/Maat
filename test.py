import maat as mt


ins = mt.Spectra(
    filename=['CH3NH3PbI3.csv', 'CH3ND3PbI3.csv', 'manley2020-CDND.csv'],
    title=None,
    type='INS',
    save_as=None,
    units_in=['cm', 'cm', 'mev'],
    units='meV',
    low_xlim=3,
    top_xlim=50,
    low_ylim=-0.1,
    top_ylim=None,
    figsize=(8,6),
    offset=True,
    log_xscale=False,
    show_yticks=False,
    legend=False,#['CH3NH3PbI3', 'CH3ND3PbI3', 'manley2020-CDND'],
    scale_range=[None, None, 1.0],
    atoms=mt.MAPI,
    )

mt.plot.spectra(ins)

peaks = {
    'h6d0' : [36.0, 39.0],
    'h5d1' : [33.0, 35.0],
    'h4d2' : [30.7, 33.0],
    'h3d3' : [28.8, 30.7],
}

peaks_manley = {
    'h6d0' : [0, 0],
    'h5d1' : [0, 0],
    'h4d2' : [0, 0],
    'h3d3' : [0, 0],
    'h2d4' : [0, 0],
    'h1d5' : [0, 0],
    'h0d6' : [0, 0],
}

# Protonated sample
baseline_H, baseline_error_H = mt.calculate.baseline(spectra=ins, cuts=[30,35], df_index=0)
mt.calculate.deuteration_mapi(ins=ins, peaks=peaks, baseline=baseline_H, baseline_error=baseline_error_H, df_index=0)

# Deuterated sample
baseline_D, baseline_error_D = mt.calculate.baseline(spectra=ins, cuts=[35,50], df_index=1)
mt.calculate.deuteration_mapi(ins=ins, peaks=peaks, baseline=baseline_D, baseline_error=baseline_error_D, df_index=1, )

