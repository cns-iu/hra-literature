import pandas as pd
import json
import os

def transform_source_file(source_file_path, file_type, dataset_name):
    mapping_table = pd.read_csv("data/funding/mapping_tables.csv")

    if file_type.lower() == 'json':
        with open(source_file_path) as f:
            source_data = json.load(f)
    elif file_type.lower() == 'csv':
        source_data = pd.read_csv(source_file_path).to_dict('records')
    else:
        raise ValueError("Invalid file type. Only 'json' and 'csv' are supported.")

    # Filter the mapping table for the specified dataset
    mapping_table_filtered = mapping_table[mapping_table['Dataset_name'] == dataset_name]

    transformed_data = []

    # Iterate over each record in the source data
    for record in source_data:
        transformed_record = {}

        # Iterate over each row in the mapping table
        for _, row in mapping_table_filtered.iterrows():
            # Get the source and target fields
            source_field = row['Source']
            target_field = row['Target']

            # If the source field exists in the record, add it to the transformed record
            # Handle nested fields
            if '.' in source_field:
                nested_fields = source_field.split('.')
                temp_value = record
                for field in nested_fields:
                    if isinstance(temp_value, dict) and field in temp_value:
                        temp_value = temp_value[field]
                    else:
                        temp_value = None
                        break

                # Convert list or dict to string
                if isinstance(temp_value, (list, dict)):
                    temp_value = str(temp_value)

                transformed_record[target_field] = temp_value

            # If the source field exists in the record, add it to the transformed record
            elif source_field in record:
                if isinstance(record[source_field], (list, dict)):
                    transformed_record[target_field] = str(record[source_field])
                else:
                    transformed_record[target_field] = record[source_field]
            else:
                transformed_record[target_field] = None

        transformed_data.append(transformed_record)


    df_transformed = pd.DataFrame(transformed_data)

    # Save the DataFrame to a CSV file
    output_file_path = source_file_path.rsplit('.', 1)[0] + '_transformed.csv'
    df_transformed.to_csv(output_file_path, index=False)

    return output_file_path

base_directory = 'data/funding' 

for dirpath, dirnames, filenames in os.walk(base_directory):

    dataset_name = os.path.basename(dirpath).upper() 

    for filename in filenames:
        if dataset_name == "NIH":
            if "2022" in filename or "2023" in filename:
                dataset_name = "NIH_2023"
            else:
                dataset_name = "NIH_2021"

        if dataset_name == "EC":
            if "h2000" in filename or "horizon" in filename:
                dataset_name = "EC_2027"
            else: 
                dataset_name = "EC_2013"


        file_path = os.path.join(dirpath, filename)
        
        if filename.endswith('.csv'):
            output_file_path = transform_source_file(file_path, 'csv', dataset_name)
            
        elif filename.endswith('.json'):
            output_file_path = transform_source_file(file_path, 'json', dataset_name)
            
        elif filename.endswith('.xlsx'):
            # Convert xlsx to csv
            df = pd.read_excel(file_path)
            csv_path = file_path.rsplit('.', 1)[0] + '.csv'
            df.to_csv(csv_path, index=False)
            
            output_file_path = transform_source_file(csv_path, 'csv', dataset_name)
            
        else:
            continue  # Skip files that aren't CSV, JSON, or XLSX

