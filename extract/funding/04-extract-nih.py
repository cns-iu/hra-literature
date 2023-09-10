import requests
import json

url = 'https://api.reporter.nih.gov/v2/projects/search'
all_years = range(1985, 2024)

for year in all_years:
    payload = {
        "criteria": {
            # "advanced_text_search": { "searchField": "projecttitle", "searchText": "adipose","operator":"advanced" },
            "fiscal_years":[year],
            # "agencies":["NCI","NCCIH","NCATS","FIC","FDA","ALLCDC","AHRQ"]
        },
        "offset": 0,
        "limit": 500,
    }

    
    # response = requests.post(url, headers=headers, json=payload)
    all_results = []

    while True:
        response = requests.post(url, json=payload)
        print(response)
        if response.status_code == 200:
            data = response.json()
            print(payload['offset'])
            results = data['results']
            all_results.extend(results)
            current_offset = payload['offset'] + payload['limit']
            if len(results) < payload['limit']:
                break
            payload['offset'] = payload['limit']+payload['offset']
        else:
            print('Error：', response.status_code)
            break

    filename = f'data/funding/nih/awards_results_{year}.json'
    with open(filename, 'w') as f:
        json.dump(all_results, f, indent=4)