#!/bin/bash

# Decompress the JSONL file and filter its content using jq
# Then write the filtered output to a CSV file


zcat data/openalex/orcid-authors-institution.jsonl.gz | \
  jq -r '[ 
      .id, 
      .orcid,  
      .last_known_institution.country_code, 
      .last_known_institution.ror, 
      .last_known_institution.id, 
      .last_known_instittution.display_name, 
      .last_known_institution.type
    ] | @csv' \
> data/institutions/orcid-authors-institution.csv

unpigz -c data/openalex/institutions.jsonl.gz | \
  jq -rc '[
      .id, 
      .ror, 
      .display_name, 
      .country_code, 
      .type
    ] | @csv' \
> data/institutions/institutions_soa.csv