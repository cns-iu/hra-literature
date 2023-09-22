import json
import csv

# Load the JSON data
with open("data/ontology/ccf-asctb-all.json", "r") as file:
    data = json.load(file)

# List to store the CSV data
csv_data = []
top_level_keys = list(data.keys())

# Rule 1: Extract relationships from anatomical_structures
for key in top_level_keys:
    for entry in data[key]["data"]:
        anatomical_structures = entry.get("anatomical_structures", [])
        for i in range(1, len(anatomical_structures)):
            source = anatomical_structures[i]
            target = anatomical_structures[i - 1]
            csv_data.append({
                "source_id": source.get("id", ""),
                "source_rdfs_label": source.get("rdfs_label", ""),
                "source_name": source.get("name", ""),
                "source_type": "AS",
                "relationship": "part_of",
                "target_id": target.get("id", ""),
                "target_rdfs_label": target.get("rdfs_label", ""),
                "target_name": target.get("name", ""),
                "target_type": "AS"
            })

# Rule 2, 3, and 4: Extract relationships from cell_types and biomarkers
for key in top_level_keys:
    for entry in data[key]["data"]:
        cell_types = entry.get("cell_types", [])
        biomarkers = entry.get("biomarkers", [])
        anatomical_structures = entry.get("anatomical_structures", [])
        
        # Targets for Rule 3 and 4
        ct_last = cell_types[-1] if cell_types else None
        as_last = anatomical_structures[-1] if anatomical_structures else None
        
        # Rule 2: cell_types relationships
        for i in range(1, len(cell_types)):
            source = cell_types[i]
            target = cell_types[0]
            csv_data.append({
                "source_id": source.get("id", ""),
                "source_rdfs_label": source.get("rdfs_label", ""),
                "source_name": source.get("name", ""),
                "source_type": "CT",
                "relationship": "is_a",
                "target_id": target.get("id", ""),
                "target_rdfs_label": target.get("rdfs_label", ""),
                "target_name": target.get("name", ""),
                "target_type": "CT"
            })
        
        # Rule 3: biomarkers relationships
        for b in biomarkers:
            if ct_last:
                csv_data.append({
                    "source_id": b.get("id", ""),
                    "source_rdfs_label": b.get("rdfs_label", ""),
                    "source_name": b.get("name", ""),
                    "source_type": "B",
                    "relationship": "characterizes",
                    "target_id": ct_last.get("id", ""),
                    "target_rdfs_label": ct_last.get("rdfs_label", ""),
                    "target_name": ct_last.get("name", ""),
                    "target_type": "CT"
                })

        # Rule 4: cell_types relationships with anatomical_structures
        for ct in cell_types:
            if as_last:
                csv_data.append({
                    "source_id": ct.get("id", ""),
                    "source_rdfs_label": ct.get("rdfs_label", ""),
                    "source_name": ct.get("name", ""),
                    "source_type": "CT",
                    "relationship": "located_in",
                    "target_id": as_last.get("id", ""),
                    "target_rdfs_label": as_last.get("rdfs_label", ""),
                    "target_name": as_last.get("name", ""),
                    "target_type": "AS"
                })

# Remove duplicates
unique_data_set = set(tuple(item.items()) for item in csv_data)
unique_csv_data = [dict(t) for t in unique_data_set]

# Write the updated data to a new CSV file
csv_file_updated_rules_path = "data/ontology/asctb_linkage.csv"
with open(csv_file_updated_rules_path, 'w', newline='') as csvfile:
    fieldnames = ['source_id', 'source_rdfs_label', 'source_name', 'source_type', 'relationship', 
                  'target_id', 'target_rdfs_label', 'target_name', 'target_type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in unique_csv_data:
        writer.writerow(row)
