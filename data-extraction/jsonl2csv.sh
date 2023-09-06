#!/bin/bash

# Decompress the JSONL file and filter its content using jq
# Then write the filtered output to a CSV file

zcat pmid-works-grants.jsonl.gz | \
  jq -r '[
      .id, 
      .pmid 
    ] + (
      .grants[] | [
        .funder, 
        .funder_display_name, 
        .award_id
      ]
    ) | @csv' \
> pmid-works-grants.csv

zcat data/orcid-authors-institution.jsonl.gz | \
  jq -r '[ 
      .id, 
      .orcid,  
      .last_known_institution.country_code, 
      .last_known_institution.ror, 
      .last_known_institution.id, 
      .last_known_instittution.display_name, 
      .last_known_institution.type
    ] | @csv' \
> orcid-authors-institution.csv

unpigz -c ./drive-download-20230831T135906Z-001/institutions.jsonl.gz | \
  jq -rc '[
      .id, 
      .ror, 
      .display_name, 
      .country_code, 
      .type
    ] | @csv' \
> institutions_soa.csv

unpigz -c ./drive-download-20230831T135906Z-001/funders.jsonl.gz | \
  jq -rc '[
      .id, 
      .display_name, 
      .country_code, 
      .grants_count, 
      .works_count
    ] | @csv' \
> funders_soa.csv
