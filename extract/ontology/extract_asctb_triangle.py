import json
import pandas as pd


# Function to extract and structure data for different entities
def extract_entity_data(entity_data, ontology_type, organ_key, row_id):
    table_data = []

    for entry in entity_data:
        id_value = entry.get('id', '')
        rdfs_label = entry.get('rdfs_label', '')
        name = entry.get('name', '')
        b_type = entry.get('b_type', '')  # Specific to biomarkers

        # Append to table with row_id and ontology_type
        table_data.append([row_id, id_value, rdfs_label, name, b_type, organ_key, ontology_type])

    return table_data


# Read the JSON file
with open('data/ontology/ccf-asctb-all.json', 'r') as f:
    data = json.load(f)

# Initialize empty list to hold data for the new table with row_id and ontology_type
table_with_row_id_data = []

# Define a mapping for ontology_type abbreviations
ontology_type_mapping = {'anatomical_structures': 'AS', 'cell_types': 'CT', 'biomarkers': 'B'}

# Iterate through each organ key in the JSON data
for organ_key in data.keys():
    organ_data = data[organ_key].get('data', [])

    # Extract the relevant information and populate the list for each entity type
    for entry in organ_data:
        row_number = entry.get('rowNumber', '')
        row_id = f"{organ_key}_{row_number}"  # Concatenating organ and rowNumber

        for ontology_type in ['anatomical_structures', 'cell_types', 'biomarkers']:
            entity_data = entry.get(ontology_type, [])
            ontology_type_abbr = ontology_type_mapping.get(ontology_type, '')

            table_data = extract_entity_data(entity_data, ontology_type_abbr, organ_key, row_id)
            table_with_row_id_data.extend(table_data)

# Create DataFrame and save it to CSV
table_with_row_id_columns = ['row_id', 'id', 'rdfs_label', 'name', 'b_type', 'organ', 'ontology_type']
table_with_row_id_df = pd.DataFrame(table_with_row_id_data, columns=table_with_row_id_columns)

# Save to CSV
output_path = 'data/ontology/hralit_ontology_triangle.csv'
table_with_row_id_df.to_csv(output_path, index=False)

