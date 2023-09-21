import pandas as pd
import os

# Directory containing the CSV files
csv_directory = 'data/results/app1'  # Replace with the path to your CSV files

# List all CSV files in the directory
csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]

# Read the first CSV to start the merge
merged_df = pd.read_csv(os.path.join(csv_directory, csv_files[0]))

# Merge with the rest of the CSVs
for csv_file in csv_files[1:]:
    if csv_file not in ['pub-trend.csv']:
        # Read the next CSV
        df = pd.read_csv(os.path.join(csv_directory, csv_file))
        
        # Merge based on the 'organ' column
        merged_df = pd.merge(merged_df, df, on='organ', how='outer')

# Save the merged dataframe to a new CSV file
merged_df.to_csv('data/results/app1/merged_output.csv', index=False)
