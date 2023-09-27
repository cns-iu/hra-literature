import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the Excel file into a DataFrame
df = pd.read_csv('data/results/app1/funding-cost-each.csv')

# Set the organ name column as the index
df.set_index('organ', inplace=True)

# Get the count number columns
count_cols = df.columns.tolist()

# Define the scientific color palette
# scientific_colors = sns.color_palette('Paired',n_colors=len(count_cols))
##in funding data
# custom_colors =['#FB9A99','#7A47B3','#E31A1C','#B2DF8A','#1F78B4','#A6CEE3']
#in pub-exp-fund-ex
custom_colors =['#E31A1C','#FB9A99','#B2DF8A', '#33A02C', '#1F78B4','#A6CEE3']
scientific_colors = custom_colors[:len(count_cols)]

# Set the figure size
plt.figure(figsize=(10, 6))

# Plot the vertical bar chart
fig, ax = plt.subplots()
df[count_cols].plot(kind='bar', ax=ax, stacked=True, color=scientific_colors)

# Set the labels and title
ax.set_xlabel('Organ')
ax.set_ylabel('Total number')
# ax.set_title('Total number of four  for 34 organs')

# Display the legend
ax.legend()

# Set the y-axis labels in scientific notation
ax.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))

# Adjust the layout to show the x-axis labels fully
plt.tight_layout()

# Show the plot
plt.show()
