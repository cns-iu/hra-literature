import pandas as pd

# Load the files
dataset_mapping = pd.read_csv('data/experimental/dataset_mapping.csv')
gtex_datasets = pd.read_csv('data/experimental/gtex_datasets.csv')
hubmap_datasets = pd.read_csv('data/experimental/hubmap_datasets.csv')
cxg_datasets = pd.read_csv('data/experimental/cxg_healthy_human_adult_datasets.csv', encoding='ISO-8859-1')

# Define a function to rename columns based on the mapping table and the portal name
def rename_columns(df, portal):
    mapping = dataset_mapping[dataset_mapping['portal'] == portal]
    rename_dict = dict(zip(mapping['source'], mapping['target']))
    df = df.rename(columns=rename_dict)
    return df

# Rename columns for each dataset
gtex_datasets_renamed = rename_columns(gtex_datasets, 'gtex')
hubmap_datasets_renamed = rename_columns(hubmap_datasets, 'hubmap')
cxg_datasets_renamed = rename_columns(cxg_datasets, 'cxg')

# Add a source column to each dataset
gtex_datasets_renamed['source'] = 'gtex'
hubmap_datasets_renamed['source'] = 'hubmap'
cxg_datasets_renamed['source'] = 'cxg'

# Concatenate the datasets vertically
merged_datasets = pd.concat([gtex_datasets_renamed, hubmap_datasets_renamed, cxg_datasets_renamed], ignore_index=True, sort=False)

# Replace NaN values with empty string
merged_datasets_filled = merged_datasets.fillna('')

# Save the modified dataset as a CSV file
output_path_filled = 'data/experimental/merged_datasets_filled.csv'
merged_datasets_filled.to_csv(output_path_filled, index=False)

# #change into json format
# def aggregate_values_v2(x):
#     # If any value in the series is a string that looks like a list (starts with '[' and ends with ']'),
#     # return the first such value
#     for item in x:
#         if isinstance(item, str) and item.startswith('[') and item.endswith(']'):
#             return item
#     return list(set(x))

# # Grouping by 'dataset_id' and aggregating the rest of the columns with the new aggregation function
# agg_data_v2 = merged_datasets_filled.groupby('dataset_id').agg(aggregate_values_v2).reset_index()

# # Convert the updated dataframe to a JSON format
# json_data_v2 = agg_data_v2.to_json(orient='records')

# # Save the transformed JSON data to a file
# json_file_path_v2 = '\HRALit KG\\datasets\\dataset_metadata_v2.json'
# with open(json_file_path_v2, 'w') as f:
#     f.write(json_data_v2)
