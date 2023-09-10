import json
import pandas as pd
from collections import defaultdict

# the 5th release metadata file (ccf-asctb-all.json) are given in https://ccf-ontology.hubmapconsortium.org/v2.2.1/ccf-asctb.json
file_path = 'ccf-asctb-all.json'

# Function to extract the required information
def extract_data(json_content):
    extracted_data = defaultdict(list)

    # Iterating through the first-degree keys representing organ names
    for organ, content in json_content.items():
        # Iterating through the list inside "data" to extract references
        for data_item in content['data']:
            references = data_item['references']
            if references:
                for ref in references:
                    extracted_data['organ'].append(organ)
                    extracted_data['id'].append(ref.get('id', ''))
                    extracted_data['doi'].append(ref.get('doi', ''))
                    extracted_data['notes'].append(ref.get('notes', ''))
                    extracted_data['type'].append('reference')
            else:
                # Handling the case where "references" is empty
                extracted_data['organ'].append(organ)
                extracted_data['id'].append('none')
                extracted_data['doi'].append('')
                extracted_data['notes'].append('')
                extracted_data['type'].append('reference')

        # Extracting general_publications from metadata
        general_publications = content['metadata'].get('general_publications', [])
        if general_publications:
            for pub in general_publications:
                extracted_data['organ'].append(organ)
                extracted_data['id'].append('')
                extracted_data['doi'].append(pub)
                extracted_data['notes'].append('')
                extracted_data['type'].append('general_publication')
        else:
            # Handling the case where "general_publications" is empty
            extracted_data['organ'].append(organ)
            extracted_data['id'].append('none')
            extracted_data['doi'].append('')
            extracted_data['notes'].append('')
            extracted_data['type'].append('general_publication')

    return extracted_data


# Reading the JSON file
with open(file_path, 'r') as file:
    json_content = json.load(file)

# Extracting the required information
extracted_data = extract_data(json_content)

# Creating a DataFrame from the extracted data
df = pd.DataFrame.from_dict(extracted_data)

# Defining the CSV file path
csv_file_path = 'data/publication/hra-refs-organs.csv'

# Writing the DataFrame to the CSV file
df.to_csv(csv_file_path, index=False)

