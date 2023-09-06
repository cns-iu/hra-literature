import json
import csv
import pandas as pd

def get_data_schema(obj, path=""):
    paths = []
    schema = {}

    if isinstance(obj, dict):
        for k, v in obj.items():
            new_path = f"{path}.{k}" if path else k
            sub_schema, sub_paths = get_data_schema(v, new_path)
            schema[k] = sub_schema
            paths.extend(sub_paths)
    elif isinstance(obj, list):
        if len(obj) > 0:
            elem_type = type(obj[0]).name
            sub_schema, sub_paths = get_data_schema(obj[0], f"{path}")
            schema = {"type": "list", "element_type": elem_type, "items": sub_schema}
            paths.extend(sub_paths)
        else:
            schema = {"type": "list", "element_type": "undefined", "items": {}}
    else:
        schema = {"type": type(obj).name}

    if path:
        paths.append({"path": path, "type": schema})

    return schema, paths

#read the source file
csv_file_path = 'path_to_file.csv'
with open(csv_file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    csv_data = [dict(row) for row in reader]

json_data = json.dumps(csv_data)
data = json.loads(json_data)

schema, paths = get_data_schema(data)
key_paths = []

for item in paths:
    if len(item['type'].keys()) == 1 and 'type' in item['type'].keys():
        key_paths.append([item['path'], item['type']['type']])

# Save the schema and key paths to JSON and CSV files
with open('data_schema_nih_funding_19985_2021.json', 'w') as f:
    json.dump(schema, f, indent=4)
df = pd.DataFrame(key_paths, columns=['path', 'type'])
df.to_csv("key_paths.csv", index=False)

