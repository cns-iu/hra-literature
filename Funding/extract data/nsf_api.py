import requests
import json

url = 'http://api.nsf.gov/services/v1/awards.json'
params = {'keyword': 'large+intestine',
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


with open('awards_results.json', 'w') as f:
    json.dump(all_results, f, indent=4)

print('Total count: {} results'.format(len(all_results)))
