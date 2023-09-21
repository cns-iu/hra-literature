import pandas as pd

# Load each table into separate DataFrames
pub_df = pd.read_csv('data/results/app1/pub-ct.csv')[['organ', 'pub_ct']]
expert_df = pd.read_csv('data/results/app1/expert-ct.csv')[['organ', 'expert_count']]
ins_df = pd.read_csv('data/results/app3/ins-ct.csv')[['organ', 'ins_ct']]
funding_df = pd.read_csv('data/results/app1/funding-ct.csv')[['organ', 'funding_count', 'funder_count']]
dataset_df = pd.read_csv('data/results/app3/dataset-ct-each.csv')[['organ', 'hubmap_ct', 'gtex_ct', 'cxg_ct']]

# Merge the DataFrames one by one
merged_df = pd.merge(pub_df, expert_df, on='organ', how='outer')
merged_df = pd.merge(merged_df, ins_df, on='organ', how='outer')
merged_df = pd.merge(merged_df, funding_df, on='organ', how='outer')
merged_df = pd.merge(merged_df, dataset_df, on='organ', how='outer')

# Output the merged DataFrame to a CSV file
merged_df.to_csv('data/results/app3/merged_output.csv', index=False)