import requests
import json
import xmltodict
import pandas as pd


# 设置请求 URL 和参数
url = 'https://kaken.nii.ac.jp/opensearch/'
params = {
    'appid': 'your_appid',
    'format':'xml',
    'rw':500,
}
df = pd.read_csv('output.csv')
for keyword in df['kw']:
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

    with open(f'{keyword}_kaken.json', 'w') as f:
        json.dump(all_results, f, indent=4)
