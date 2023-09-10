import requests
import json
import xmltodict
import pandas as pd

# Set the request URL and parameters
url = 'https://kaken.nii.ac.jp/opensearch/'
params = {
    'appid': 'your_appid',
    'format':'xml',
    'rw':500,
}
df = pd.read_csv('/data/funding/organs.csv')
for keyword in df['organs']:
    print(keyword)
    params['kw'] = keyword
    st=1
    all_results = []
    while True:
        print(st)
        params['st'] = st
        response = requests.get(url, params=params)
        data = response.text
        xml_obj = xmltodict.parse(data)
        results = xml_obj['grantAwards']['grantAward']
        all_results.extend(results)
        if 500 > len(xml_obj['grantAwards']['grantAward']):
            break
        st += 500

    with open(f'/data/funding/kaken/{keyword}.json', 'w') as f:
        json.dump(all_results, f, indent=4)
