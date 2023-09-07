import requests
import json

url = 'https://gtr.ukri.org/gtr/api/funds'
headers = {
    'Accept': 'application/vnd.rcuk.gtr.json-v7'
}
params = {'size': 20}
response = requests.get(url,headers=headers)
data = response.json()
page=1
all_results = []
while True:
    params['page'] = page
    response = requests.get(url,headers=headers,params=params)
    print(response)
    print(page)
    data = response.json()
    results = data['organisation']
    all_results.extend(results)
    if page >= data['totalPages']:
        break
    page += 1

with open('data/funding/ukri/awards_results.json', 'w') as f:
    json.dump(all_results, f, indent=4)
