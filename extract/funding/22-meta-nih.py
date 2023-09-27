import pandas as pd
import json
import os
import ijson
import numpy as np
import jsonlines


def process_nih_data(folder_path):
    results = []
    # Iterate over each file in the folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        print(file)
        
        # Load the current grants dataset
        grants_df = pd.read_csv(file_path, encoding='ISO-8859-1')

        # if "2022" in file or "2023" in file:
        if "2022" in file or "2023" in file:
        
            for organ in organs_df['organ']:
                matching_rows = (grants_df['project_title'].str.contains(organ, case=False, na=False) | 
                        grants_df['abstract_text'].str.contains(organ, case=False, na=False) | 
                        grants_df['pref_terms'].str.contains(organ, case=False, na=False) | 
                        grants_df['terms'].str.contains(organ, case=False, na=False))

                matching_results = []
                for _, row in grants_df[matching_rows].iterrows(): 
                    matching_results.append({
                        "organ": organ,
                        "source": "nih",
                        "id": row["project_num"],
                        "title": row["project_title"],
                        "fundingAmount": row["direct_cost_amt"] + row["indirect_cost_amt"],
                        "fiscalYear": row["fiscal_year"],
                        "startDate": row["budget_start"],
                        "endDate": row["budget_end"]
                    })
                results.extend(matching_results)
        else:
            for organ in organs_df['organ']:
                matching_rows = (grants_df['PROJECT_TERMS'].str.contains(organ, case=False, na=False) | 
                        grants_df['PROJECT_TITLE'].str.contains(organ, case=False, na=False))

                matching_results = []
                for _, row in grants_df[matching_rows].iterrows(): 
                    matching_results.append({
                        "organ": organ,
                        "source": "nih",
                        "id": row["APPLICATION_ID"],
                        "title": row["PROJECT_TITLE"],
                        "fundingAmount": row["TOTAL_COST"],
                        "fiscalYear": row["FY"],
                        "startDate": row["BUDGET_START"],
                        "endDate": row["BUDGET_END"]
                    })
                results.extend(matching_results)
    return results

columns = ["id", "title", "fundingAmount", "fiscalYear", "startDate", "endDate", "source", "organ"]

organs_df = pd.read_csv('data/experimental/organ.csv')

nih_df = pd.DataFrame(process_nih_data('data/funding/nih'), columns=columns)

merged_df = pd.concat([nih_df], ignore_index=True)

# Define the output CSV file name
csv_file_name = "data/funding/additional_meta_nih.csv"

# Write the merged data to a CSV file
merged_df.to_csv(csv_file_name, index=False)

print(f"CSV file '{csv_file_name}' has been created with the merged data.")