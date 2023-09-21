import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import t

# Load the data
data = pd.read_csv('data/results/app1/pub-trend.csv')

# Filter out the data for the year 2023
filtered_data = data[data['pubyear'] != 2023]

# Extract the columns of interest from the filtered data
filtered_years = filtered_data['pubyear'].values
filtered_pubs = filtered_data['pubmed_pubs'].values

# Normalize the filtered years for regression analysis
normalized_filtered_years = filtered_years - filtered_years.min()

# Apply a logarithmic transformation to the y-axis
log_filtered_pubs = np.log(filtered_pubs)

# Reshape the data for regression analysis
X = normalized_filtered_years.reshape(-1, 1)
y = log_filtered_pubs

# Perform linear regression
model = LinearRegression()
model.fit(X, y)
predicted = model.predict(X)

# Calculate residuals
residuals = y - predicted
# Calculate standard deviation of residuals
std_error = residuals.std()

# Calculate the 95% prediction intervals
degree_freedom = len(X) - 2
t_value = t.ppf(0.975, degree_freedom)  # 95% quantile for t-distribution
prediction_interval_upper = predicted + t_value * std_error
prediction_interval_lower = predicted - t_value * std_error

# Convert the prediction intervals back from log scale to original scale
prediction_interval_upper_original = np.exp(prediction_interval_upper)
prediction_interval_lower_original = np.exp(prediction_interval_lower)

# Visualize the results
plt.figure(figsize=(12,7))
plt.scatter(filtered_years, filtered_pubs, color='blue', s=10, label='Data points')
plt.plot(filtered_years, np.exp(predicted), color='purple', label='Linear Regression (on log-transformed data)')
plt.fill_between(filtered_years, prediction_interval_lower_original, prediction_interval_upper_original, color='orange', alpha=0.3, label='95% Prediction Interval')

# Formatting the plot
plt.yscale('log')
plt.title('Log-transformed Number of Publications Over the Years with Regression Analysis')
plt.xlabel('Year')
plt.ylabel('Number of Publications (log scale)')
# plt.legend()
# plt.grid(True, which="both", ls="--")
plt.grid(False)
plt.tight_layout()
plt.show()

# Compute the overall growth rate and doubling time
growth_rate = (np.exp(model.coef_[0]) - 1) * 100
doubling_time = np.log(2) / model.coef_[0]
print(f"Overall growth rate: {growth_rate:.2f}%")
print(f"Doubling time: {doubling_time:.2f} years")