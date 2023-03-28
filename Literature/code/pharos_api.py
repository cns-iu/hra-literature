import requests

url = "https://pharos-api.ncats.io/graphql"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# GraphQL Query
query = """

query diseaseDetails{
  disease(name:"asthma"){
    name
    mondoDescription
    uniprotDescription
    doDescription
    targetCounts {
      name
      value
    }
    children {
      name
      mondoDescription
    }
  }
}
"""

response = requests.post(url, json={"query": query}, headers=headers)
print(response.text)
response_data = response.json()
