# import os
# import ijson
# import pandas as pd

# # Path to the directory containing the JSON files
# folder_path = "data/funding/kaken"

# # Get the list of all JSON files in the directory
# json_files = [file for file in os.listdir(folder_path) if file.endswith('.json')]

# # Initialize an empty list to store the results
# results = []

# # Function to extract totalCost from a single item (record) in the JSON
# def extract_total_cost_from_item(item):
#     total_costs = [entry['overallAwardAmount']['totalCost'] for entry in item['summary'] if '@xml:lang' in entry and entry['@xml:lang'] == 'ja' and 'overallAwardAmount' in entry and 'totalCost' in entry['overallAwardAmount']]
#     return sum(map(int, total_costs))

# # Iterate over each JSON file and process it
# for json_file in json_files:
#     total_cost_for_file = 0
    
#     # Stream the JSON file using ijson
#     with open(os.path.join(folder_path, json_file), "r") as file:
#         # Parse each item in the JSON array
#         items = ijson.items(file, 'item')
#         for item in items:
#             total_cost_for_file += extract_total_cost_from_item(item)
    
#     # Process the filename string
#     filename_processed = json_file.replace("_kaken.json", "").replace("_", " ")
    
#     # Append the results to the results list
#     results.append({
#         "organ": filename_processed,
#         "total_cost": total_cost_for_file
#     })

# # Convert the results list to a DataFrame
# df = pd.DataFrame(results)

# # Save the DataFrame to a CSV file
# output_filename_pandas = "data/results/app1/funding-cost/kaken.csv"
# df.to_csv(output_filename_pandas, index=False)


import requests
import json
import xmltodict
import pandas as pd

# Set the request URL and parameters
url = 'https://kaken.nii.ac.jp/opensearch/'
params = {
    'appid': 'XU5sddkHCLzYbyxjABoB',
    'format':'xml',
    'rw':500,
}
df = pd.read_csv('data/experimental/organ.csv')

for keyword in df['organ']:
    if keyword not in ['blood vasculature']:
        print(keyword)
        params['kw'] = keyword
        st=1
        all_total_costs = []
        
        while True:
            print(st)
            params['st'] = st
            response = requests.get(url, params=params)
            data = response.text
            xml_obj = xmltodict.parse(data)
            
            # Check if 'grantAward' and 'summary' exist in the parsed data
            if 'grantAward' in xml_obj.get('grantAwards', {}) and 'summary' in xml_obj['grantAwards']['grantAward']:
                summary = xml_obj['grantAwards']['grantAward']['summary']
                total_costs = [
                    entry['overallAwardAmount']['totalCost'] 
                    for entry in summary 
                    if entry.get('@xml:lang') == 'ja' 
                    and 'overallAwardAmount' in entry 
                    and 'totalCost' in entry['overallAwardAmount']
                ]
                all_total_costs.extend(total_costs)
            
            if 500 > len(xml_obj.get('grantAwards', {}).get('grantAward', [])):
                break
                
            st += 500

        with open(f'data/funding/kaken/{keyword}.json', 'w') as f:
            json.dump(all_total_costs, f, indent=4)
