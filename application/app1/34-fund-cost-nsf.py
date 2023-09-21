import pandas as pd
import os
import json
from datetime import datetime

# Define a function to process a single file and return the total cost
# def process_file(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     total_cost = sum(int(record.get('estimatedTotalAmt', 0) or 0) for record in data)
#     return total_cost

def process_file(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Check the date condition
    total_cost = sum(int(entry.get('estimatedTotalAmt', 0) or 0) for entry in data if 'estimatedTotalAmt' in entry and entry['estimatedTotalAmt'] is not None and datetime.strptime(entry.get('date', '01/01/1900'), '%m/%d/%Y') <= datetime(2023, 3, 15) )
    # funding_amounts = [entry['estimatedTotalAmt'] 
    #                    for entry in data 
    #                    if 'estimatedTotalAmt' in entry 
    #                    and entry['estimatedTotalAmt'] is not None 
    #                    and datetime.strptime(entry.get('date', '01/01/1900'), '%m/%d/%Y') <= datetime(2023, 3, 15)]
    
    return total_cost

# Define the folder path
folder_path = "data/funding/nsf"

# Get all files in the folder
all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(".json")]

# Process each file and collect the results
results = []
for file_name in all_files:
    if file_name in ['main bronchus_awards_results.json', 'muscular system_awards_results.json', 'trachea_awards_results.json' ,'uterus_awards_results.json']:
        organ_name = file_name.replace("_awards_results", "").replace("_", " ").split(".")[0]
        total_cost = process_file(os.path.join(folder_path, file_name))
        results.append([organ_name, total_cost])

# Convert the results to a pandas DataFrame and save to CSV
df = pd.DataFrame(results, columns=["organ", "total_cost"])
output_file_path = "data/results/app1/funding-cost/nsf.csv"
df.to_csv(output_file_path, index=False)
