zcat pmid-works-grants.jsonl.gz | jq -r '[ .id, .pmid ] + (.grants[] | [.funder, .funder_display_name, .award_id]) | @csv' > pmid-works-grants.csv

zcat data/orcid-authors-institution.jsonl.gz | jq '[.id, .orcid,  .last_known_institution.country_code, .last_known_institution.ror, .last_known_institution.id, .last_known_instittution.display_name, .last_known_institution.type]  | @csv' -r > orcid-authors-institution.csv
