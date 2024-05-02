import pandas as pd
import matplotlib.pyplot as plt
import os

mev_to_cm = 8.0655
cm_to_mev = 1.0 / mev_to_cm

filename = 'MAPI_comercial.csv'
name = 'MAPI_comercial'
folder = 'data'
root = os.path.dirname(os.path.abspath(__file__))
cwd = os.getcwd()
file = os.path.join(root, folder, filename)
column = 0  # X or Y, 0 or 1

df = pd.read_csv(file)

# Multiply each element of the first column by cm_to_mev for df1
df[df.columns[column]] = df[df.columns[column]] * cm_to_mev

# Normalize df
df_range = df[(df[df.columns[column]] >= 30) & (df[df.columns[column]] <= 50)]
max_df = df_range[df_range.columns[2]].max()

# Sort the dataframes
# df = df.sort_values(by=df.columns[column])

# Plot the data from both files on the same axes
ax = df.plot(x=df.columns[column], y=df.columns[2], label=name)

# Set the limits for the axes
ax.set_xlim([0, 50])
ax.set_ylim([0, 2 * max_df])

# Set the labels for the axes
plt.xlabel('Energy / meV')
plt.ylabel('Intensity')
plt.title('MAPI INS')

# Show the plot
plt.show()

