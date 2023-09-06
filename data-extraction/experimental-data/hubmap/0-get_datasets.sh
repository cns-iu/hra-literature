#!/bin/bash

# Fetch the datasets from HuBMAP and Convert TSV to CSV
curl -O https://entity.api.hubmapconsortium.org/datasets/prov-info
 
awk 'BEGIN {FS="\t"; OFS=","} { $1=$1; print }' prov-info > data/experimetal/hubmap_datasets_all.csv

echo "Conversion completed for datasets. The CSV file is saved as hubmap_datasets_all.csv."


