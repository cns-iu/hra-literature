#!/bin/bash
source .venv/bin/activate

mkdir -p data/openalex

echo "Extracting funders..."
zcat data/s3_openalex/data/funders/*/*.gz | \
  jq '{id:.id, display_name:.display_name, country_code:.country_code, grants_count:.grants_count, works_count:.works_count }' -c | \
  gzip -9 -c \
  > data/openalex/funders.jsonl.gz

echo "Extracting work grants..."
zcat data/s3_openalex/data/works/*/*.gz | \
  jq '{id:.id,pmid:.ids.pmid,grants:.grants}' -c | \
  grep -v '\[\]' | grep -v null | \
  gzip -9 -c \
  > data/openalex/pmid-works-grants.jsonl.gz
