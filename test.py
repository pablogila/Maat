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
    legend=['CH3NH3PbI3 test','CH3ND3PbI3 test'],
    scale_range=[None, None, 1.0],
    atoms=mt.MAPI,
    )

mt.plot.spectra(ins)

