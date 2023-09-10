import json
import csv
import pandas as pd
import os

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
base_directory = 'data/funding' 

for dirpath, dirnames, filenames in os.walk(base_directory):
    for filename in filenames:
        if filename.endswith('.csv'):
            csv_file_path = os.path.join(dirpath, filename)
            
            with open(csv_file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                csv_data = [dict(row) for row in reader]
            
            data = csv_data
            
        elif filename.endswith('.json'):
            json_file_path = os.path.join(dirpath, filename)
            
            with open(json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
        elif filename.endswith('.xlsx'):
            xlsx_file_path = os.path.join(dirpath, filename)
            
            # Assuming the data you want is in the first sheet. Modify if needed.
            df = pd.read_excel(xlsx_file_path, sheet_name=0)
            data = df.to_dict(orient='records')
            
        else:
            continue  # Skip files that aren't CSV, JSON, or XLSX
        
        schema, paths = get_data_schema(data)
        key_paths = []

        for item in paths:
            if len(item['type'].keys()) == 1 and 'type' in item['type'].keys():
                key_paths.append([item['path'], item['type']['type']])

        # Save the schema and key paths to JSON and CSV files
        json_filename = filename.rsplit('.', 1)[0] + '_schema.json'  # Get filename without extension and append '_schema.json'
        csv_filename = filename.rsplit('.', 1)[0] + '_key_paths.csv'
        
        with open(os.path.join(dirpath, json_filename), 'w') as f:
            json.dump(schema, f, indent=4)
        
        df = pd.DataFrame(key_paths, columns=['path', 'type'])
        df.to_csv(os.path.join(dirpath, csv_filename), index=False)
