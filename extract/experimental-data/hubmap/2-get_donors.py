import pandas as pd
import requests
import json

def extract_unique_donor_ids(file_path):

    with open(file_path, 'r') as file:
        data = json.load(file)

    # Extract all "donor_hubmap_id" values
    donor_ids = [item["donor_hubmap_id"] for item in data if "donor_hubmap_id" in item]

    # Remove duplicates
    unique_donor_ids = list(set(donor_ids))
    
    return unique_donor_ids


sample_data_path='data/experimetal/hubmap_samples_all.csv'

# Get the list of donor_id
hbm_ids = extract_unique_donor_ids(sample_data_path)

# Define the API endpoint
base_url = "https://entity.api.hubmapconsortium.org/entities/{}"

# List to store the extracted data
data_list = []

# Loop through each HBM ID to make the API call
for hbm_id in hbm_ids:
    response = requests.get(base_url.format(hbm_id), headers={'accept': 'application/json'})
    if response.status_code == 200:
        json_data = response.json()
        metadata = json_data.get("metadata", {})

        # Check if metadata is a list and has at least one item
        if isinstance(metadata, list) and len(metadata) > 0:
            metadata = metadata[0]

        organ_donor_data = metadata.get("organ_donor_data", [])

        for record in organ_donor_data:
            data_list.append({
                "HBM_ID": hbm_id,
                "Grouping Concept": record.get("grouping_concept_preferred_term", ""),
                "Preferred Term": record.get("preferred_term", ""),
                "Data Value": record.get("data_value", ""),
                "Units": record.get("units", "")
            })

# Convert the data list to a DataFrame and save to CSV
output_df = pd.DataFrame(data_list)
output_df.to_csv("data/experimetal/humbmap_donors_data.csv", index=False)



##aggregates and reshapes
# Load the output_data.csv file
output_data_df = pd.read_csv("data/experimetal/humbmap_donors_data.csv")

# Convert NaN values to empty strings for aggregation
output_data_df = output_data_df.fillna("")

# Aggregate the duplicate rows
aggregated_data = output_data_df.groupby(['HBM_ID', 'Grouping Concept']).agg({
    'Preferred Term': lambda x: '; '.join(sorted(set(x))),
    'Data Value': lambda x: '; '.join(sorted(set(x))),
    'Units': lambda x: '; '.join(sorted(set(x)))
}).reset_index()

# Pivot the aggregated data
pivot_preferred_term = aggregated_data.pivot(index='HBM_ID', columns='Grouping Concept', values='Preferred Term')
pivot_data_value = aggregated_data.pivot(index='HBM_ID', columns='Grouping Concept', values='Data Value')
pivot_units = aggregated_data.pivot(index='HBM_ID', columns='Grouping Concept', values='Units')

# Rename columns for merging
pivot_preferred_term.columns = [f"{col}_Preferred Term" for col in pivot_preferred_term.columns]
pivot_data_value.columns = [f"{col}_Data Value" for col in pivot_data_value.columns]
pivot_units.columns = [f"{col}_Units" for col in pivot_units.columns]

# Merge the pivoted dataframes on HBM_ID
merged_df = pd.concat([pivot_preferred_term, pivot_data_value, pivot_units], axis=1).reset_index()

# Save the transformed data to a new CSV file
merged_df.to_csv("data/experimetal/humbmap_donors_cleaned_data.csv", index=False)

