"""Plot examples without installing NicePlots."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# import niceplots
import os


# Define style file
style_to_use = 'styles/niceplot.mplstyle'

# Check we are in examples dir
current_dir = os.getcwd().lower()
if (current_dir.endswith('NicePlots')):
    os.chdir('./examples')
# Create 'figures' folder if it does not exist
if (not os.path.exists('./figures')):
    os.makedirs('figures')

def example_function(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))


pparam = dict(xlabel='Voltage (mV)', ylabel=r'Current ($\mu$A)')

x = np.linspace(0.75, 1.25, 201)


plt.style.use(style_to_use)

#plt.rcParams.update({
#"font.family": "serif",   # specify font family here
#"font.serif": ["Times"],  # specify font here
#"font.size":12})          # specify font size here

fig, ax = plt.subplots()
for p in [10, 15, 20, 30, 50, 100]:
    ax.plot(x, example_function(x, p), label=p)
ax.legend(title='Legend')
ax.autoscale(tight=True)
ax.set(**pparam)
fig.savefig('figures/fig_qbsm.jpg', dpi=300)
plt.close()

