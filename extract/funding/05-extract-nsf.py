import requests
import json
import pandas as pd

def fetch_data_for_keyword(keyword):
    url = 'http://api.nsf.gov/services/v1/awards.json'
    params = {'keyword':  keyword.replace(" ", "+"),  # Convert spaces to "+" for URL encoding
            'printFields': 'rpp,offset,id,agency,awardeeCity,awardeeCountryCode,awardeeCounty,awardeeDistrictCode,awardeeName,awardeeStateCode,awardeeZipCode,cfdaNumber,coPDPI,date,startDate,expDate,estimatedTotalAmt,fundsObligatedAmt,dunsNumber,fundProgramName,parentDunsNumber,pdPIName,perfCity,perfCountryCode,perfCounty,perfDistrictCode,perfLocation,perfStateCode,perfZipCode,poName,primaryProgram,transType,title,awardee,poPhone,poEmail,awardeeAddress,perfAddress,publicationResearch,publicationConference,fundAgencyCode,awardAgencyCode,projectOutComesReport,abstractText,piFirstName,piMiddeInitial,piLastName,piPhone,piEmail'}

    all_results = []

    while True:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            print(data)
            results = data['response']['award']
            all_results.extend(results)
            if len(results) < 25:
                break
            params['offset'] = int(params.get('offset', 0)) + int(25)
        else:
            print('Error：', response.status_code)
            break
    
    # Save the results to a JSON file named after the keyword
    filename = f'data/funding/nsf/{keyword}_awards_results.json'
    with open(filename, 'w') as f:
        json.dump(all_results, f, indent=4)

    print(f'Total count for {keyword}: {len(all_results)} results')

# Read keywords using pandas
df = pd.read_csv('data/funding/organs.csv')
keywords = df.iloc[:, 0].tolist()  # Assuming keywords are in the first column

# Fetch data for each keyword
for keyword in keywords:
    fetch_data_for_keyword(keyword)
