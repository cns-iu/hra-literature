import json
import pandas as pd


# Function to extract and structure data for different entities
def extract_entity_data(entity_data, entity_type, organ_key):
    first_table_data = []
    second_table_data = []

    for entry in entity_data:
        id_value = entry.get('id', '')
        rdfs_label = entry.get('rdfs_label', '')
        name = entry.get('name', '')
        b_type = entry.get('b_type', '')  # Specific to biomarkers

        # Append to first table
        if entity_type == 'biomarkers':
            first_table_data.append([id_value, rdfs_label, name, b_type])
        else:
            first_table_data.append([id_value, rdfs_label, name])

        # Append to second table with organ key
        if entity_type == 'biomarkers':
            second_table_data.append([organ_key, id_value, rdfs_label, name, b_type])
        else:
            second_table_data.append([organ_key, id_value, rdfs_label, name])

    return first_table_data, second_table_data


# Read the JSON file
with open('data/ontology/ccf-asctb-all.json', 'r') as f:
    data = json.load(f)

# Initialize empty lists to hold data for the six tables
first_tables = {'anatomical_structures': [], 'cell_types': [], 'biomarkers': []}
second_tables = {'anatomical_structures': [], 'cell_types': [], 'biomarkers': []}

# Iterate through each organ key in the JSON data
for organ_key in data.keys():
    organ_data = data[organ_key].get('data', [])

    # Extract the relevant information and populate the lists for each entity type
    for entry in organ_data:
        for entity_type in ['anatomical_structures', 'cell_types', 'biomarkers']:
            entity_data = entry.get(entity_type, [])

            first_table_data, second_table_data = extract_entity_data(entity_data, entity_type, organ_key)

            first_tables[entity_type].extend(first_table_data)
            second_tables[entity_type].extend(second_table_data)

# Create DataFrames and save them to CSV
for entity_type in ['anatomical_structures', 'cell_types', 'biomarkers']:
    first_table_columns = ['id', 'rdfs_label', 'name', 'b_type'] if entity_type == 'biomarkers' else ['id','rdfs_label','name']
    second_table_columns = ['organ', 'id', 'rdfs_label', 'name', 'b_type'] if entity_type == 'biomarkers' else ['organ','id','rdfs_label','name']

    # Convert lists to DataFrames and drop duplicates
    first_table_df = pd.DataFrame(first_tables[entity_type], columns=first_table_columns).drop_duplicates()
    second_table_df = pd.DataFrame(second_tables[entity_type], columns=second_table_columns).drop_duplicates()

    # Save to CSV
    first_csv_path = f'data/ontology/asct_{entity_type}.csv'
    second_csv_path = f'data/ontology/organ_{entity_type}.csv'

    first_table_df.to_csv(first_csv_path, index=False)
    second_table_df.to_csv(second_csv_path, index=False)
