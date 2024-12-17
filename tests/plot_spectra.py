import maat as mt
# Run the code in the same directory as this script
try:
    import thoth as th
    th.call.here()
except:
    print("Remember to check the file paths and all of that!")
# Load the example data, customizing the plotting options
ins = mt.Spectra(
    type='INS',
    filename='ins.csv',
    units_in='cm-1',
    units='meV',
    plotting=mt.Plotting(
        title='Calculated MAPbI$_3$ INS',
        xlim=[8,500],
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

