import pandas as pd
import os

# Define the path to the folder containing the files
folder_path = 'data/funding/nih'  # You should replace this with the path to your folder

# Load the 'organ.csv' file
organ_df = pd.read_csv('data/experimental/organ.csv')

# List all files in the folder
all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Dictionary to store total costs for each organ across all files
total_costs = {organ: 0 for organ in organ_df['organ']}

# Process each file in the folder
for file in all_files:
    
    file_path = os.path.join(folder_path, file)
    print(file_path)
    data_df = pd.read_csv(file_path, encoding='ISO-8859-1')

    # Only process files with "2022" or "2023" in their names
    if "2022" in file or "2023" in file:
        # Process the data and sum the costs for each organ
        for organ in organ_df['organ']:
            if "2022" in file or "2023" in file:
                mask = (data_df['project_title'].str.contains(organ, case=False, na=False) | 
                        data_df['abstract_text'].str.contains(organ, case=False, na=False) | 
                        data_df['pref_terms'].str.contains(organ, case=False, na=False) | 
                        data_df['terms'].str.contains(organ, case=False, na=False))
            filtered_df = data_df[mask]
            total_cost = filtered_df['direct_cost_amt'].sum() + filtered_df['indirect_cost_amt'].sum()
            total_costs[organ] += total_cost
    else:
        # Process the data and sum the costs for each organ
        for organ in organ_df['organ']:
            mask = (data_df['PROJECT_TERMS'].str.contains(organ, case=False, na=False) | 
                    data_df['PROJECT_TITLE'].str.contains(organ, case=False, na=False))
            filtered_df = data_df[mask]
            total_cost = filtered_df['TOTAL_COST'].sum()
            total_costs[organ] += total_cost

# Convert total costs dictionary to DataFrame
total_costs_df = pd.DataFrame(list(total_costs.items()), columns=['organ', 'total_cost'])

output_path = "data/results/app1/funding-cost/nih.csv"
total_costs_df.to_csv(output_path, index=False)