import os
import json
import pandas as pd

# Compute the total funding amount from a given JSON file.
def compute_total_funding(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    funding_amounts = [entry['fundingAmount'] for entry in data if 'fundingAmount' in entry and entry['fundingAmount'] is not None]
    return sum(funding_amounts)

# Define the directory containing your JSON files
json_directory = 'data/funding/ardc'

# List to hold results
results = []

# Iterate over each file in the directory
for filename in os.listdir(json_directory):
    if filename.endswith('.json'):
        organ_name = filename.split('.')[0].replace('_', ' ')  
        total_amount = compute_total_funding(os.path.join(json_directory, filename))
        results.append([organ_name, total_amount])

# Convert the results to a DataFrame
df = pd.DataFrame(results, columns=['organ', 'total_cost'])

# Save the DataFrame to CSV
output_path = 'data/results/app1/funding-cost/ardc.csv'
df.to_csv(output_path, index=False)
