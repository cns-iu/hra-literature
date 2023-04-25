import requests
import json
url = "https://www.ebi.ac.uk/biostudies/api/v1/search"
params = {"query": "atlas"}

response = requests.get(url, params=params)

if response.ok:
    data = response.json()
    with open("biostudy_atlas_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Data written to file.")
    # Process the data
else:
    print(f"Error: {response.status_code} - {response.reason}")
