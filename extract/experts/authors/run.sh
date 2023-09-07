#!/bin/bash

psql -h cns_host -U your_username -p port  -d wos_2018 -f 0-affi_geo.sql

psql -h cns_host -U your_username -p port -d your_database -f 1-insert.sql

psql -h cns_host -U your_username -p port  -d pubmed19 -f 2-career_age.sql

psql -h cns_host -U your_username -p port -d your_database -f 3-insert.sql

# extract the last affiliations for authors
psql -h cns_host -U your_username -p port -d your_database -f 40-record_last_aff.sql -f 50-insert.sql -f 60-export.sql

# extract all affiliations for authors
# psql -h cns_host -U your_username -p port -d your_database -f 41-record_all_aff.sql -f 51-insert.sql -f 61-export.sql
