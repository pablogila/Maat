import maat as mt
# Run the code in the same directory as this script
mt.run_here()
# Load the example data, customizing the plotting options
ins = mt.Spectra(
    type='INS',
    filename='ins.csv',
    units_in='cm-1',
    units='meV',
    plotting=mt.Plotting(
        title='Calculated MAPbI$_3$ INS',
        xlim=[5,100],
        margins=[0,0.1],
        vline=[35.5, 110],
        figsize=(8, 4.5),
        log_xscale=True,
        show_yticks=False,
        ylabel='S(Q,E) / a.u.',
        legend=['Calculation']
        )
    )
# Plot the data
mt.plot.spectra(ins)

