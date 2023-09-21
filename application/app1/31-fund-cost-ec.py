import os
import pandas as pd

def compute_total_funding_for_file(file_path, organ):
    
    df = pd.read_excel(file_path)
    
    # Convert the 'totalCost' column to numeric
    df['totalCost'] = pd.to_numeric(df['totalCost'], errors='coerce')
    
    # Initialize a filter for matched rows
    filter_matched_rows = df['title'].str.contains(organ, case=False, na=False)
    
    # Check for special file names
    if any(keyword in file_path.lower() for keyword in ["fp7", "h2000", "horizon"]):
        if df['title'].dtype == 'object':
            filter_matched_rows |= df['title'].str.contains(organ, case=False, na=False)
        if df['topics'].dtype == 'object':
            filter_matched_rows |= df['topics'].str.contains(organ, case=False, na=False)
        if df['objective'].dtype == 'object':
            filter_matched_rows |= df['objective'].str.contains(organ, case=False, na=False)
    else:
        if df['title'].dtype == 'object':
            filter_matched_rows |= df['title'].str.contains(organ, case=False, na=False)
        if df['subjects'].dtype == 'object':
            filter_matched_rows |= df['subjects'].str.contains(organ, case=False, na=False)
        if df['topics'].dtype == 'object':
            filter_matched_rows |= df['topics'].str.contains(organ, case=False, na=False)
        if df['objective'].dtype == 'object':
            filter_matched_rows |= df['objective'].str.contains(organ, case=False, na=False)
    
    # Return the sum of 'totalCost' for the matched rows
    return df[filter_matched_rows]['totalCost'].sum()
# Define the directory containing your Excel files
xlsx_directory = 'data/funding/ec'

# Initialize an empty list to store results
results = []

# Load the list of organs
organs = pd.read_csv('data/experimental/organ.csv')['organ'].tolist()

# Iterate over each organ
for organ in organs:
    total_cost = 0
    # Iterate over each file in the directory
    for filename in os.listdir(xlsx_directory):
        if filename.endswith('.xlsx'):
            total_cost += compute_total_funding_for_file(os.path.join(xlsx_directory, filename), organ)
    results.append([organ, total_cost])

# Convert results to DataFrame
results_df = pd.DataFrame(results, columns=['organ', 'total_cost'])

# Save results to CSV
results_df.to_csv('data/results/app1/funding-cost/ec.csv', index=False)
