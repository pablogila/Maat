import maat as mt

ins = mt.MData(
    filename=['CH3NH3PbI3.csv', 'CH3ND3PbI3.csv'],
    title=None,
    type='INS',
    save_as=None,
    units_in='cm',
    units='meV',
    low_xlim=3,
    top_xlim=50,
    low_ylim=-0.1,
    top_ylim=None,
    figsize=(7,4),
    offset=True,
    log_xscale=False,
    show_yticks=False,
    legend=['CH3NH3PbI3.csv', 'CH3ND3PbI3'],
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

# We test the deuteration for the protonated sample
baseline, baseline_error = mt.calculate.baseline(ins=ins, cuts=[30,35], df_index=0)
mt.calculate.deuteration_mapi(ins=ins, baseline=baseline, baseline_error=baseline_error, partial=True, peaks=peaks, df_index=0)

