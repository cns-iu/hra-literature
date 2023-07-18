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
