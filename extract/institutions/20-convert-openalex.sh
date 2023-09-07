#!/bin/bash
source .venv/bin/activate

mkdir -p data/openalex


echo "Extracting author institutions..."
zcat data/s3_openalex/data/authors/*/*.gz | \
  jq '{id:.id,orcid:.orcid,last_known_institution:.last_known_institution}' -c | \
  grep -v null | \
  gzip -9 -c \
  > data/openalex/orcid-authors-institution.jsonl.gz

echo "Extracting institutions..."
zcat data/s3_openalex/data/institutions/*/*.gz | \
  jq '{id:.id,ror:.ror,display_name:.display_name,country_code:.country_code,type:.type}' -c | \
  grep -v null | \
  gzip -9 -c \
  > data/openalex/institutions.jsonl.gz
