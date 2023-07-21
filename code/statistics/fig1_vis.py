import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_excel('/mnt/data/test1.xlsx')

# Set up the figure size
plt.figure(figsize=(14, 6))

# Plot scatterplot for Expert and total_h-index
# Reduce the node size by dividing by a larger number
scatter = plt.scatter(data['organ'], data['Expert'], s=data['total_h-index']/100, alpha=0.5, edgecolors='none', marker='o', color='green')
plt.title('Expert vs total_h-index')
plt.xlabel('Organ')
plt.ylabel('Expert')
plt.xticks(rotation=90)
plt.yticks(range(0, int(data['Expert'].max()) + 1, 5000))  # Show less scale in y-axis

# Create a legend for the scatter plot
# Calculate the average, min and max sizes for the legend
avg_size = data['total_h-index'].mean()
min_size = data['total_h-index'].min()
max_size = data['total_h-index'].max()

# Create a legend with three example points, for min, avg and max total_h-index
legend_labels = [f'{min_size:.2f}', f'{avg_size:.2f}', f'{max_size:.2f}']
handles, _ = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = plt.legend(handles, legend_labels, 
                     title="total_h-index", 
                     loc='upper right', 
                     borderaxespad=0.)
plt.gca().add_artist(legend2)

plt.tight_layout()
plt.show()

#------------------
#Create Funding vs TotalCost

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_excel('fig1.xlsx')

# Set up the figure size
plt.figure(figsize=(14, 6))

# Plot scatterplot for Expert and total_h-index
# Reduce the node size by dividing by a larger number
scatter = plt.scatter(data['organ'], data['Dataset'], s=data['DS size'], alpha=0.5, edgecolors='none', marker='o', color='blue')
plt.title('Dataset vs DS size')
plt.xlabel('Organ')
plt.ylabel('Dataset')
plt.xticks(rotation=90)
plt.yticks(range(0, int(data['Dataset'].max()) + 1, 100))  # Show less scale in y-axis

for x, y, size in zip(data['organ'], data['Dataset'], data['DS size']):
    plt.plot([x, x], [0, y], linestyle=':', color='gray', alpha=0.5)

plt.tight_layout()
plt.show()

#------------------
#Create Funding vs TotalCost

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_excel('fig1.xlsx')

# Set up the figure size
plt.figure(figsize=(14, 6))

# Plot scatterplot for Expert and total_h-index
# Reduce the node size by dividing by a larger number
scatter = plt.scatter(data['organ'], data['Funding'], s=data['TotalCost']/200000000, alpha=0.5, edgecolors='none', marker='o', color='red')
plt.title('Funding')
plt.xlabel('Organ')
plt.ylabel('Funding')
plt.xticks(rotation=90)
plt.yticks(range(0, int(data['Funding'].max()) + 1, 100000))  # Show less scale in y-axis

for x, y, size in zip(data['organ'], data['Funding'], data['TotalCost']):
    plt.plot([x, x], [0, y], linestyle=':', color='gray', alpha=0.5)

plt.tight_layout()
plt.show()

#------------------
#Create Funding vs TotalCost

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_excel('fig1.xlsx')

# Set up the figure size
plt.figure(figsize=(14, 6))

# Plot scatterplot for Expert and total_h-index
# Reduce the node size by dividing by a larger number
scatter = plt.scatter(data['organ'], data['Publication'], s=data['citation']/40000, alpha=0.5, edgecolors='none', marker='o', color='purple')
plt.title('Publication')
plt.xlabel('Organ')
plt.ylabel('Publication')
plt.xticks(rotation=90)
plt.yticks(range(0, int(data['Publication'].max()) + 1, 200000))  # Show less scale in y-axis

for x, y, size in zip(data['organ'], data['Publication'], data['citation']):
    plt.plot([x, x], [0, y], linestyle=':', color='gray', alpha=0.5)

plt.tight_layout()
plt.show()

#------------------
#Create Funding Proportion by Organ and Funder

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import colorsys
import math

# Load the Excel file
data = pd.read_excel('/mnt/data/fig2.xlsx')

# Melt the data into long format
data_long = data.melt(id_vars='organ', var_name='funder', value_name='funding')

# Calculate the total funding provided by each funder
total_funding_by_funder = data_long.groupby('funder')['funding'].sum()

# Calculate the proportion of each funding amount relative to the total for each funder
data_long['funding_proportion'] = data_long.apply(lambda row: row['funding'] / total_funding_by_funder[row['funder']], axis=1)

# Calculate the logarithm of the funding proportion to reduce the discrepancy between large and small values
data_long['funding_proportion_log'] = np.log1p(data_long['funding_proportion'])

# Convert RGB color to hex color
color_rgb = [131, 99, 161]
color_hex = '#%02x%02x%02x' % (color_rgb[0], color_rgb[1], color_rgb[2])

# Convert RGB color to HSV, adjust Value (brightness), then convert back to RGB
color_rgb = [131/255, 99/255, 161/255]  # RGB values need to be in the range [0, 1]
color_hsv = colorsys.rgb_to_hsv(color_rgb[0], color_rgb[1], color_rgb[2])
color_hsv_dark = (color_hsv[0], color_hsv[1], color_hsv[2]*0.6)  # Reduce brightness to 60%
color_rgb_dark = colorsys.hsv_to_rgb(*color_hsv_dark)
color_hex_dark = '#%02x%02x%02x' % (int(color_rgb_dark[0]*255), int(color_rgb_dark[1]*255), int(color_rgb_dark[2]*255))

# Further adjust figure size to reduce scale distance in x-axis
plt.figure(figsize=(6, 15))

# Create bubble chart with reversed axes and further reduced x-axis scale distance
# Use the darkened color for the bubbles
bubble = sns.scatterplot(data=data_long, y='organ', x='funder', size='funding_proportion_log', sizes=(50, 1000), 
                         legend=False, alpha=0.6, edgecolors=None, marker="o", color=color_hex_dark)

# Remove grid lines
bubble.grid(False)

# Add labels and title
plt.ylabel("Organ")
plt.xlabel("Funder")
plt.title("Funding Proportion by Organ and Funder (Logarithmic Scale)")

# Rotate y-axis labels for better visibility
plt.yticks(rotation=45)

# Show the plot
plt.show()

# Calculate total funding by each funder
total_funding = data_long.groupby('funder')['funding'].sum().reset_index()

# Create bar chart
plt.figure(figsize=(10, 6))
bar = sns.barplot(x='funder', y='funding', data=total_funding, palette='coolwarm')

# Add labels and title
plt.xlabel("Funder")
plt.ylabel("Total Funding")
plt.title("Total Funding by Each Funder")

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Show the plot
plt.show()

