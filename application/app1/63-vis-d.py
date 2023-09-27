# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the provided CSV file into a DataFrame
trend_data = pd.read_csv('data/results/app1/pub-trend.csv')

# Applying a rolling average with a window size of 5 years for smoothing
smoothed_data = trend_data.copy()
for column in smoothed_data.columns[1:]:
    smoothed_data[column] = smoothed_data[column].rolling(window=5).mean()

# Plotting the smoothed trend with a logarithmic scale and without grid lines
plt.figure(figsize=(14, 8))

for column in smoothed_data.columns[1:]:
    plt.plot(smoothed_data['pubyear'], smoothed_data[column], label=column,linewidth=8)

# Setting the y-axis to a logarithmic scale
plt.yscale('log')

# Defining the ticks for the logarithmic scale
ticks = [1, 10, 100, 1000, 10000, 100000, 1000000]
plt.yticks(ticks, ticks)

plt.title("Smoothed Publication Trend Over the Years (Without Grid Lines)")
plt.xlabel("Year")
plt.ylabel("Publication Count (Log Scale)")
plt.legend()
plt.grid(False)  # Removing the grid lines
plt.tight_layout()

plt.savefig("data/results/app1/fig-1-d.png")

plt.show()
