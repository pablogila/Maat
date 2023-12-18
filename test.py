import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# Generate a DataFrame with 100 rows and 5 columns of random numbers
data = pd.DataFrame(np.random.rand(100, 5), columns=['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])

# Extract volumes and pressures from the data
x = data['Column1'].values
y1 = data['Column2'].values
y2 = data['Column3'].values

# Define the font properties
font_title = {'family': 'Verdana', 'weight': 'bold', 'size': 16}
font_label = {'family': 'Verdana', 'weight': 'bold', 'size': 12}
font_notes = {'family': 'Verdana', 'weight': 'normal', 'size': 12}

# Plotting the results
plt.plot(x, y1, 'bo', label='dataset 1')
plt.plot(x, y2, 'r-', label=r'2$^{nd}$ dataset')
plt.ylabel(r'Y label ($\AA^3$)', fontdict=font_label)
plt.yticks(weight = 'bold')
plt.xlabel('X label (GPa)', fontdict=font_label)
plt.xticks(weight = 'bold')
# change all spines
for axis in ['top','bottom','left','right']:
    plt.gca().spines[axis].set_linewidth(1.5)
# increase tick width
plt.tick_params(width=1.5)
plt.title('Bulk modulus at 295 K -- OSIRIS & XPRESS', fontdict=font_title)
plt.legend()

# Add text annotations for the fitted parameters, std errors, chi-square and goodness of fit
statistics_text = 'hola'
parameters_text = 'adios'
plt.text(0.05, 0.05, parameters_text, transform=plt.gca().transAxes, fontdict=font_notes, color='black')
plt.text(0.05, 0.20, statistics_text, transform=plt.gca().transAxes, fontdict=font_notes, color='black')

# Save figure to png in desired location
plt.savefig(r"figure.png", bbox_inches='tight', dpi=500)

plt.show()

