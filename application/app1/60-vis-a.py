import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import colorsys
import math

# Load the Excel file
data = pd.read_csv('data/results/app1/merged_output.csv')
# Melt the data into long format
data_long = data.melt(id_vars='organ', var_name='funder', value_name='funding')

# Calculate the total funding provided by each funder
total_funding_by_funder = data_long.groupby('funder')['funding'].sum()
# Calculate the proportion of each funding amount relative to the total for each funder
data_long['funding_proportion'] = data_long.apply(lambda row: row['funding'] / total_funding_by_funder[row['funder']], axis=1)
# Calculate the logarithm of the funding proportion to reduce the discrepancy between large and small values
data_long['funding_proportion_log'] = np.log1p(data_long['funding_proportion'])

# Convert RGB color to hex color
# color_rgb = [131, 99, 161] #purple
# color_rgb = [228, 123, 38] #orange
# color_rgb = [32, 110, 158] #blue
color_rgb = [53, 144, 58] #green
color_hex = '#%02x%02x%02x' % (color_rgb[0], color_rgb[1], color_rgb[2])

# Further adjust figure size to reduce scale distance in x-axis
plt.figure(figsize=(6, 15))

data_filtered = data_long[data_long['funding_proportion_log'] != 0]

# Create bubble chart with reversed axes and further reduced x-axis scale distance
# Use the darkened color for the bubbles
bubble = sns.scatterplot(data=data_long, y='organ', x='funder', size='funding_proportion_log', sizes=(30, 400),
                         legend=False, alpha=0.6, edgecolors=None, marker="o", color=color_hex)

# Remove grid lines
bubble.grid(False)

plt.savefig("data/results/app1/fig-1-a.png")

plt.show()