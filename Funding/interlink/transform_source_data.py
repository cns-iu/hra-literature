import pandas as pd
import json


def transform_source_file(source_file_path, file_type, dataset_name, mapping_table_path):
    mapping_table = pd.read_csv(mapping_table_path)

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

json_output_file_path = transform_source_file('path_to_file.json', 'json', 'your_dataset_name',
                                              'mapping_table.csv')
csv_output_file_path = transform_source_file('path_to_file.csv', 'csv', 'your_dataset_name',
                                             'mapping_table.csv')
