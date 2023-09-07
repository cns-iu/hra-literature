#!/bin/bash

# Decompress the JSONL file and filter its content using jq
# Then write the filtered output to a CSV file

zcat data/openalex/pmid-works-grants.jsonl.gz | \
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
> data/funders/pmid-works-grants.csv

unpigz -c data/openalex/funders.jsonl.gz | \
  jq -rc '[
      .id, 
      .display_name, 
      .country_code, 
      .grants_count, 
      .works_count
    ] | @csv' \
> data/funders/funders_soa.csv
