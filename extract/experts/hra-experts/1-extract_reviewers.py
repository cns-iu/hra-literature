import json
import csv
import pandas as pd

# Load the JSON data
with open('data/hra-v1.4-metadata.json', 'r') as file:
    data = json.load(file)
print(data)
# List of common organs
organs = [
    "trachea", "blood vasculature", "lymph node", "lung", "ureter", 
    "peripheral nervous system", "knee", "small intestine", "liver", 
    "uterus", "ovary", "thymus", "large intestine", "skin", "bone marrow", 
    "heart", "pelvis", "eye", "pancreas", "lymph vasculature", 
    "fallopian tube", "spinal cord", "brain", "spleen", "kidney", 
    "urinary bladder", "prostate", "placenta full term", "skeleton", 
    "muscular system", "vasculature", "palatine tonsil", "intestine", "larynx",
    "main bronchus", "mammary gland"
]

def identify_organ(name):
    """Identify the organ with priority to specific matches."""
    cleaned_name = name.lower().replace(" ", "").replace("-", "")
    
    # Prioritize matching "small intestine" and "large intestine"
    for organ in ["small intestine", "large intestine"]:
        if organ.replace(" ", "").replace("-", "") in cleaned_name:
            return organ.capitalize()
    
    # If neither above match, then check for "intestine"
    if "intestine" in cleaned_name:
        return "Intestine"
    
    # Check for other organs
    for organ in organs:
        if organ.replace(" ", "").replace("-", "") in cleaned_name:
            return organ.capitalize()
    
    return ""

# Extract the required information for each record
extracted_data = []
for record in data:
    for reviewer in record.get("reviewers", []):
        organ = identify_organ(record["name"])
        extracted_data.append({
            "orcid": reviewer.get("orcid", ""),
            "full_name": reviewer.get("fullName", ""),
            "first_name": reviewer.get("firstName", ""),
            "last_name": reviewer.get("lastName", ""),
            "version": record.get("version", ""),
            "name": record.get("name", ""),
            "type": record.get("type", ""),
            "organ": organ,
            "hubmap_id": record.get("hubmapId", "")
        })

# Write the extracted data to a CSV file
output_csv_path = "data/experts/hra_reviewers.csv"
df = pd.DataFrame(extracted_data)
df.to_csv(output_csv_path, index=False)

# # os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
# with open(output_csv_path, 'w', newline='') as csvfile:
#     fieldnames = ["orcid", "full_name", "first_name", "last_name", "version", "name", "type", "organ", "hubmap_id"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in extracted_data:
#         writer.writerow(row)
