# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
data = pd.read_csv('data/results/app1/merged_output.csv')

# Calculate avg cit
data['avg_cit'] = data['cit_ct'] / data['pub_ct']

# Sort data alphabetically by organ
data_alpha_sorted = data.sort_values(by='organ')

# Create the heatmap with organs sorted alphabetically
plt.figure(figsize=(10, 15))
sns.heatmap(data_alpha_sorted[['organ', 'avg_cit']].set_index('organ'),
            cmap="Reds",
            annot=True,
            fmt=".2f",
            linewidths=0.7,
            linecolor='white',
            cbar_kws={'label': 'Average Citations'})

# Set the title and display the plot
plt.title('Average Citations by Organ (Alphabetically Sorted)')
plt.show()
