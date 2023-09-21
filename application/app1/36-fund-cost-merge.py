import pandas as pd
import os

# Specify the folder path
folder_path = 'data/results/app1/funding-cost'  # Replace this with your folder path

# List all CSV files in the folder
all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.csv')]

# Initialize an empty DataFrame to store the merged results
merged_df = None

# Process each file
for file in all_files:
    # Construct the full path to the file
    file_path = os.path.join(folder_path, file)
    
    # Load the file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Check if 'organ' column exists in the DataFrame
    if 'organ' not in df.columns:
        continue
    
    # Keep only the 'organ' and 'total_cost' columns
    
    # Rename the 'total_cost' column to the file's name (without the .csv extension)
    column_name = os.path.splitext(file)[0]
    df = df.rename(columns={'total_cost': column_name})

    if merged_df is None:
        merged_df = df
    else:
        merged_df = pd.merge(merged_df, df, on='organ', how='outer')


merged_df = merged_df.drop_duplicates(subset='organ', keep='first')

merged_df = merged_df.sort_values(by='organ', ascending=True)

# Fill any NaN values with 0 (optional)
merged_df = merged_df.fillna(0)

# Save the merged DataFrame to a new CSV file (optional)
output_path = "data/results/app1/funding-cost/merged_results.csv"  # Replace this with your desired save path
merged_df.to_csv(output_path, index=False)
