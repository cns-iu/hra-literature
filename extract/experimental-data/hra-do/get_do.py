import json
import pandas as pd

# Load the JSON data from the provided file
with open("data/hra-v1.4-metadata.json", 'r') as file:
    data = json.load(file)

# Extract the desired fields from the data
records = []
for item in data:
    record = {
        'type': item.get('type', ''),
        'name': item.get('name', ''),
        'version': item.get('version', ''),
        'title': item.get('title', ''),
        'license': item.get('license', ''),
        'publisher': item.get('publisher', ''),
        'hubmap_id': item.get('hubmapId', ''),  
        'doi': item.get('doi', '')
    }
    records.append(record)

# Convert the records to a DataFrame
df = pd.DataFrame(records)

# Save the DataFrame to a CSV file
output_path = "data/experimental/hra_do_5th_release.csv"
df.to_csv(output_path, index=False)
