import pandas as pd
import json

# Load the CSV into a DataFrame
csv_path = '/mnt/data/donor_metadata.csv'
df = pd.read_csv(csv_path)

# Define a default context based on column names
context = {
    "@context": {
        col: f"http://example.org/property/{col}" for col in df.columns
    }
}

# Convert DataFrame to JSON-LD format
json_ld_data = df.to_dict(orient='records')
json_ld = {
    "@context": context["@context"],
    "@graph": json_ld_data
}

# Path to save the JSON-LD data
json_ld_path = "/mnt/data/donor_metadata.jsonld"

# Save the JSON-LD data to a file
with open(json_ld_path, 'w') as f:
    json.dump(json_ld, f, indent=4)

print(f"JSON-LD data saved to: {json_ld_path}")
