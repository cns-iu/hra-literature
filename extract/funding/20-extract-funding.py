import pandas as pd
import json
import os
import ijson
import numpy as np

def process_ardc_data(folder_path):
    records=[]
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)

            organ = os.path.splitext(os.path.basename(file_path))[0].replace("_", " ")
            source = "ardc"
            fiscal_year = None 
            for record in data:
                id_value = record.get("id", "")
                title = record.get("title", "")
                funding_amount = record.get("fundingAmount", "")
                start_date = record.get("startDate", "")
                end_date = record.get("endDate", "")
                records.append([id_value, title, funding_amount, fiscal_year, start_date, end_date, source, organ])

    return records

def process_cihr_data(folder_path):
    results = []
    # Iterate over each file in the folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        # Load the current grants dataset
        grants_df = pd.read_csv(file_path)
        
        # Ensure that the relevant columns are treated as strings to facilitate the search operation
        grants_df['ResearchClassEN'] = grants_df['ResearchClassEN'].astype(str)
        grants_df['TitreApplicationTitle'] = grants_df['TitreApplicationTitle'].astype(str)
        grants_df['Keywords-MotsClés'] = grants_df['Keywords-MotsClés'].astype(str)

        # Iterate over each organ
        for organ in organs_df['organ']:
            # Filter the grants_df for rows that contain the organ in the specified columns
            matching_rows = grants_df[
                grants_df['ResearchClassEN'].str.contains(organ, case=False, na=False) |
                grants_df['TitreApplicationTitle'].str.contains(organ, case=False, na=False) |
                grants_df['Keywords-MotsClés'].str.contains(organ, case=False, na=False)
            ]
            matching_results = []
            for _, row in matching_rows.iterrows():
                matching_results.append({
                    "organ": organ,
                    "source": "cihr",
                    "id": row["Key-Clé"],
                    "title": row["TitreApplicationTitle"],
                    "fundingAmount": row["TotalAwardAmount-MontantSubventionTotal"],
                    "fiscalYear": row["FiscalYear-AnnéeFinancière"],
                    "startDate": row["FirstPaymentFY-AFduPremierVersement"],
                    "endDate": row["LastPaymentFY-AFduDernierVersement"]
                })
            
            results.extend(matching_results)

    return results


def process_ec_data(folder_path):
    results = []
    # Iterate over each file in the folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        # Load the current grants dataset
        grants_df = pd.read_excel(file_path)
        
        grants_df['title'] = grants_df['title'].astype(str)
        grants_df['topics'] = grants_df['topics'].astype(str)
        grants_df['objective'] = grants_df['objective'].astype(str)

        if not any(keyword in file_path.lower() for keyword in ["fp7", "h2000", "horizon"]):
            grants_df['subjects'] = grants_df['subjects'].astype(str)
        # Ensure that the relevant columns are treated as strings to facilitate the search operation
        grants_df['title'] = grants_df['title'].astype(str)
        grants_df['topics'] = grants_df['topics'].astype(str)
        grants_df['objective'] = grants_df['objective'].astype(str)

        # Iterate over each organ
        for organ in organs_df['organ']:
            # Filter the grants_df for rows that contain the organ in the specified columns
            if any(keyword in file_path.lower() for keyword  in ["fp7", "h2000", "horizon"]):
                matching_rows = grants_df[
                    grants_df['title'].str.contains(organ, case=False, na=False) |
                    grants_df['topics'].str.contains(organ, case=False, na=False) |
                    grants_df['objective'].str.contains(organ, case=False, na=False) 
                ]
            else:
                matching_rows = grants_df[
                    grants_df['title'].str.contains(organ, case=False, na=False) |
                    grants_df['topics'].str.contains(organ, case=False, na=False) |
                    grants_df['objective'].str.contains(organ, case=False, na=False) |
                    grants_df['subjects'].str.contains(organ, case=False, na=False)
                ]
            matching_results = []
            for _, row in matching_rows.iterrows():
                matching_results.append({
                    "organ": organ,
                    "source": "ec",
                    "id": row["rcn"],
                    "title": row["title"],
                    "fundingAmount": row["totalCost"],
                    "fiscalYear": None,
                    "startDate": row["startDate"],
                    "endDate": row["endDate"]
                })
            
            results.extend(matching_results)

    return results

def process_nsf_data(folder_path):
    records=[]
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)

            organ = os.path.splitext(os.path.basename(file_path))[0].replace("_", " ")
            source = "nsf"
            fiscal_year = None 
            for record in data:
                id_value = record.get("id", "")
                title = record.get("title", "")
                funding_amount = record.get("estimatedTotalAmt", "")
                start_date = record.get("startDate", "")
                end_date = record.get("expDate", "")
                records.append([id_value, title, funding_amount, fiscal_year, start_date, end_date, source, organ])
    return records



columns = ["id", "title", "fundingAmount", "fiscalYear", "startDate", "endDate", "source", "organ"]

organs_df = pd.read_csv('data/experimental/organ.csv')

# Process each source separately
# nih_df = pd.DataFrame(process_nih_data('data/funding/nih'), columns=columns)
ardc_df = pd.DataFrame(process_ardc_data('data/funding/ardc'), columns=columns)
cihr_df = pd.DataFrame(process_cihr_data('data/funding/cihr'), columns=columns)
ec_df = pd.DataFrame(process_ec_data('data/funding/ec'), columns=columns)
# kaken_df = pd.DataFrame(process_kaken_data('data/funding/kaken'), columns=columns)
nsf_df = pd.DataFrame(process_nsf_data('data/funding/nsf'), columns=columns)

# Concatenate the DataFrames into one
merged_df = pd.concat([ardc_df, cihr_df, nsf_df, ec_df], ignore_index=True)
# merged_df = pd.concat([nih_df], ignore_index=True)

# Define the output CSV file name
csv_file_name = "data/funding/additional_funding_meta.csv"

# Write the merged data to a CSV file
merged_df.to_csv(csv_file_name, index=False)

print(f"CSV file '{csv_file_name}' has been created with the merged data.")
