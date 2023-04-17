import requests
import json
import pandas as pd


# 设置请求 URL 和参数
url = 'https://researchdata.edu.au/api/v2.0/registry/activities'
params = {
    'api_key':'ded8d31e8e38',
    'limit':1000
}
df = pd.read_csv('output.csv')

for keyword in df['kw']:
    encoded_keyword = keyword.replace('_', '%20')
    print(keyword)
    params['q'] = encoded_keyword
    offset=1
    all_results = []
    while True:
        print(offset)
        params['offset'] = offset
        response = requests.get(url, params=params)
        data = response.json()
        # print(json.dumps(data, indent=4))
        print(data['data']['numFound'])
        results = data['data']['records']
        print(len(data['data']['records']))
        all_results.extend(results)
        offset += 1000
        if 1000 > len(data['data']['records']):
            break

    with open(f'ardc_awards_results\\{keyword}.json', 'w') as f:
        json.dump(all_results, f, indent=4)
