import maat as mt
# Run the code in the same directory as this script
mt.run_here()
# Load the example data, customizing the plotting options
ins = mt.Spectra(
    type='INS',
    filename='example.csv',
    units_in='cm-1',
    units='meV',
    plotting=mt.Plotting(
        title='Calculated MAPbI$_3$ INS',
        low_xlim=5,
        top_xlim=500,
        add_top=0.1,
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

