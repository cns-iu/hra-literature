#!/bin/bash

# Fetch the samples from HuBMAP
curl -O https://entity.api.hubmapconsortium.org/samples/prov-info

awk 'BEGIN {FS="\t"; OFS=","} { $1=$1; print }' prov-info > data/experimetal/hubmap_samples_all.csv

echo "Conversion completed for samples. The CSV file is saved as hubmap_samples_all.csv."