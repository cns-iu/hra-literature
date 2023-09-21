import requests
import json
import pandas as pd

def fetch_data_for_keyword(keyword):
    url = 'http://api.nsf.gov/services/v1/awards.json'
    params = {'keyword':  keyword.replace(" ", "+"),  # Convert spaces to "+" for URL encoding
              'printFields': 'estimatedTotalAmt'}
            # 'printFields': 'rpp,offset,id,agency,awardeeCity,awardeeCountryCode,awardeeCounty,awardeeDistrictCode,awardeeName,awardeeStateCode,awardeeZipCode,cfdaNumber,coPDPI,date,startDate,expDate,estimatedTotalAmt,fundsObligatedAmt,dunsNumber,fundProgramName,parentDunsNumber,pdPIName,perfCity,perfCountryCode,perfCounty,perfDistrictCode,perfLocation,perfStateCode,perfZipCode,poName,primaryProgram,transType,title,awardee,poPhone,poEmail,awardeeAddress,perfAddress,publicationResearch,publicationConference,fundAgencyCode,awardAgencyCode,projectOutComesReport,abstractText,piFirstName,piMiddeInitial,piLastName,piPhone,piEmail'}

    all_results = []

    while True:
        response = requests.get(url, params=params)
        print(response)
        print(response.text)
        if response.status_code == 200:
            print(response.text)
            data = response.json()
            results = data['response']['award']
            print(len(results))
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
df = pd.read_csv('data/experimental/organ.csv')
keywords = df.iloc[:, 0].tolist()  

# # Fetch data for each keyword
for keyword in keywords:
# for keyword in ['fallopian tube']:
    if keyword not in ['fallopian tube', 'lymph vasculature', 'main bronchus', 'muscular system', 
        'trachea','blood pelvis','blood vasculature','bone marrow', 'brain', 'eye', 'uterus','pelvis','heart']:
        print(keyword)
        fetch_data_for_keyword(keyword)
