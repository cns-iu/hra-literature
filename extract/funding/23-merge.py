import pandas as pd

def read_and_merge_csvs(file_paths):
    dfs = [pd.read_csv(file_path) for file_path in file_paths]
    merged_df = pd.concat(dfs, ignore_index=True)
    return merged_df

# List of paths to CSV files
file_paths = [
    "data/funding/additional_meta_kaken.csv",
    "data/funding/additional_funding_meta.csv",
    "data/funding/additional_meta_nih.csv"
]

# Read and merge the CSVs
merged_df = read_and_merge_csvs(file_paths)

# Save the merged dataframe to a single CSV file
output_file_name = "data/funding/merged_metadata.csv"
merged_df.to_csv(output_file_name, index=False)

print(f"Data merged and saved to {output_file_name}.")
