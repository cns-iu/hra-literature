import pandas as pd
import os

# Path to the folder containing all grant files
folder_path = 'data/funding/cihr'  # Change this to the path of your folder

# Load the organs dataset
organs_df = pd.read_csv('data/experimental/organ.csv')

# Initialize an empty list to store the results for all files
all_results = []

# Iterate over each file in the folder
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    
    # Load the current grants dataset
    grants_df = pd.read_csv(file_path)
    
    # Ensure that the relevant columns are treated as strings to facilitate the search operation
    grants_df['ResearchClassEN'] = grants_df['ResearchClassEN'].astype(str)
    grants_df['TitreApplicationTitle'] = grants_df['TitreApplicationTitle'].astype(str)
    grants_df['Keywords-MotsClés'] = grants_df['Keywords-MotsClés'].astype(str)

    # Initialize an empty list to store the results for the current file
    results = []

    # Iterate over each organ
    for organ in organs_df['organ']:
        # Filter the grants_df for rows that contain the organ in the specified columns
        matching_rows = grants_df[
            grants_df['ResearchClassEN'].str.contains(organ, case=False, na=False) |
            grants_df['TitreApplicationTitle'].str.contains(organ, case=False, na=False) |
            grants_df['Keywords-MotsClés'].str.contains(organ, case=False, na=False)
        ]
        
        # Sum the TotalAwardAmount-MontantSubventionTotal for the matching rows
        total_cost = matching_rows['TotalAwardAmount-MontantSubventionTotal'].sum()
        
        # Append the result to the results list
        results.append((organ, total_cost))

    # Convert the results to a DataFrame and append to the all_results list
    results_df = pd.DataFrame(results, columns=["organ", "total_cost"])
    all_results.append(results_df)

# Combine all results into a single DataFrame
final_results_df = pd.concat(all_results, ignore_index=True)

# Save the combined results to a CSV file
output_path = 'data/results/app1/funding-cost/cihr.csv'
final_results_df.to_csv(output_path, index=False)
