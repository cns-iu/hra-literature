import requests
import json

#get the number of documents
url = "https://textpressocentral.org:18080/v1/textpresso/api/get_documents_count"
token = "your_taken_code"
keywords = "your_keyword"
doc_type = "document"
corpora = ["C. elegans","C. elegans Supplementals"]
headers = {
    "Content-Type": "application/json"
}

payload = {
    "token": token,
    "query": {
        "keywords": keywords,
        "type": doc_type,
        "case_sensitive": False,
        "sort_by_year": False,
        "count": 2,
        "corpora": corpora
    }
}

response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)

if response.status_code == 200:
    total_records = response.json()
    print(total_records)
else:
    print(f"request fail：{response.status_code}")

# get the information of documents
url = "https://textpressocentral.org:18080/v1/textpresso/api/search_documents"
records_per_request = 200

headers = {
    "Content-Type": "application/json"
}

num_requests = total_records // records_per_request + (1 if total_records % records_per_request != 0 else 0)

all_data = []

for i in range(num_requests):
    offset = i * records_per_request
    payload = {
        "token": token,
        "since_num":offset,
        "count":records_per_request,
        "query": {
            "keywords": keywords,
            "type": doc_type,
            "corpora": corpora,
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)

    if response.status_code == 200:
        data = response.json()
        print(data)
        all_data.extend(data)
    else:
        print(f"request fail：{response.status_code}")
        break

with open("output_all.json", "w") as output_file:
    json.dump(all_data, output_file)
