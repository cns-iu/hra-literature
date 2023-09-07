#!/bin/bash

# Directory where the files will be saved
DIR="data/funding/ec"

# Create the directory if it doesn't exist
mkdir -p $DIR

# Download CIHR funding data
# URLs are available from EU datasets at "https://data.europa.eu/data/datasets?locale=en&page=1&limit=10&query=horizon%20project"
URLS=(
"https://cordis.europa.eu/data/cordis-fp7projects-xlsx.zip"
"https://cordis.europa.eu/data/FP6/cordis-fp6projects.xlsx"
"https://cordis.europa.eu/data/FP5/cordis-fp5projects.xlsx"
"https://cordis.europa.eu/data/FP4/cordis-fp4projects.xlsx"
"https://cordis.europa.eu/data/FP3/cordis-fp3projects.xlsx"
"https://cordis.europa.eu/data/FP2/cordis-fp2projects.xlsx"
"https://cordis.europa.eu/data/FP1/cordis-fp1projects.xlsx"
"https://cordis.europa.eu/data/cordis-h2020projects-xlsx.zip"
"https://cordis.europa.eu/data/cordis-HORIZONprojects-xlsx.zip"
)

for url in "${URLS[@]}"
do
    # Download the file
    wget -P $DIR $url

    # If the downloaded file is a ZIP file
    if [[ $url == *.zip ]]; then
        # Extract xlsx/project.xlsx from the zip
        unzip "$DIR/$(basename $url)" "xlsx/project.xlsx" -d $DIR

        # Rename the extracted file to match the original ZIP name (but with .xlsx extension)
        mv "$DIR/xlsx/project.xlsx" "$DIR/$(basename $url .zip).xlsx"

        # Remove the original ZIP file and the temporary xlsx directory
        rm "$DIR/$(basename $url)"
        rmdir "$DIR/xlsx"
    fi
done