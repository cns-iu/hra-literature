# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the provided CSV file into a DataFrame
merged_data = pd.read_csv('data/results/app1/merged_output.csv')

# Compute the correlation matrix
correlation_matrix = merged_data.corr()

# Create a mask for the upper triangle of the correlation matrix
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

# Generate a heatmap of the correlation matrix using a diverging color palette
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, cmap='RdBu_r', center=0, linewidths=0.5, linecolor='white', mask=mask, annot=False)

# Set the title and display the plot
plt.title('Lower Triangle Correlation Heatmap (Diverging Color Palette)')

plt.savefig("data/results/app1/fig-1-e.png")

plt.show()
