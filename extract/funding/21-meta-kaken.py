import pandas as pd
import json
import os
import ijson
import numpy as np

def process_kaken_data(folder_path):
    records=[]
    for filename in os.listdir(folder_path):
        print(filename)
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)

            f = open(file_path, 'rb')
            objects = ijson.items(f, 'item')

            organ = os.path.splitext(os.path.basename(file_path))[0].replace("_kaken", "").replace("_", " ")
            source = "kaken"
            start_date = None 
            end_date = None
            for record in objects:
                id_value = record.get("@id", "")
                for rec in record["summary"]: 
                    if rec.get('@xml:lang') == 'en' :
                        title = rec.get("title", "")
                        if 'projectStatus' in rec:
                            fiscal_year = rec["projectStatus"].get("@fiscalYear", "")
                        else:
                            fiscal_year = None
                        if 'overallAwardAmount' in rec:
                            funding_amount = rec["overallAwardAmount"].get("totalCost", "")
                records.append([id_value, title, funding_amount, fiscal_year, start_date, end_date, source, organ])                        
    return records

columns = ["id", "title", "fundingAmount", "fiscalYear", "startDate", "endDate", "source", "organ"]

organs_df = pd.read_csv('data/experimental/organ.csv')

kaken_df = pd.DataFrame(process_kaken_data('data/funding/kaken'), columns=columns)

merged_df = pd.concat([kaken_df], ignore_index=True)

# Define the output CSV file name
csv_file_name = "data/funding/additional_meta_kaken.csv"

# Write the merged data to a CSV file
merged_df.to_csv(csv_file_name, index=False)

print(f"CSV file '{csv_file_name}' has been created with the merged data.")


