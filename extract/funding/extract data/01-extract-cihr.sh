#!/bin/bash

# Directory where files will be saved
DIR="data/funding/cihr"

# Create the directory if it doesn't exist
mkdir -p $DIR

# Download CIHR funding data
# URLs are available from CIHR Grants and Awards portal "https://open.canada.ca/data/en/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3"
URLS=(
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/b259cdfb-83c0-4d76-8488-dc7ad2ea9e07/download/cihr_grants_award_200102.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/5d03cf16-6e3f-4b31-859f-5cc060324cf7/download/cihr_grants_award_200203.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/b259cdfb-83c0-4d76-8488-dc7ad2ea9e07/download/cihr_grants_award_200102.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/81128d31-b8d9-42c2-a160-6c079d697ba7/download/cihr_grants_award_200405.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/535b013d-c6b0-4693-9d6c-324e0e520e7e/download/cihr_grants_award_200506.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/0c76de88-2b84-4c41-b4d7-c5dfc927e538/download/cihr_grants_award_200607.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/00e9ca04-23a2-4240-b254-97baff3872ed/download/cihr_grants_award_200708.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/baca6764-f29f-42e0-8951-72a5f5ba6b1c/download/cihr_grants_award_200809.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/446051b7-c617-43c1-92f2-7223194c7059/download/cihr_grants_award_200910.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/1ebfc49e-f6ce-401c-ad19-798d6b5eb00d/download/cihr_grants_award_201011.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/7cb41545-71e0-4bdd-b7c2-cfb7e26443b0/download/cihr_grants_award_201112.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/95e8e97a-4ca3-469c-ab4d-1754d3561f0c/download/cihr_grants_award_201213.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/fbd7cecd-f415-4519-8be5-ac1c31167d7a/download/cihr_grants_award_201314.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/add2c683-5b3c-4eab-ba5c-28a2d203c99b/download/cihr_grants_award_201415.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/6a9b4c80-b598-43fc-b57e-d9b8e578010f/download/cihr_grants_award_201516.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/67ed1593-e473-43a5-97f7-80a96cc49f47/download/cihr_grants_award_201617.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/b86f277c-8065-42be-b672-25d2c6ad13a5/download/cihr_grants_award_201718.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/1c2cc36f-4065-4f8d-937b-ea3c6249844b/download/cihr_grants_award_201819.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/161332d4-6caf-4b7f-9e3a-3596e17e0e2a/download/cihr_grants_award_201920.csv"
"https://open.canada.ca/data/dataset/49edb1d7-5cb4-4fa7-897c-515d1aad5da3/resource/42300f81-a00a-4f0f-9ba9-842bb0e1971e/download/cihr_grants_award_202021.csv"
)

# Loop through each URL and download the file
for url in "${URLS[@]}"
do
    wget -P $DIR $url
done