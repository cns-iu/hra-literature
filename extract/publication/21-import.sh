#!/bin/bash

# Database connection details
DB_NAME=$(awk -F "=" '/dbname/ {print $2}' db_config.ini | tr -d ' ')
DB_USER=$(awk -F "=" '/user/ {print $2}' db_config.ini | tr -d ' ')
DB_PASS=$(awk -F "=" '/password/ {print $2}' db_config.ini | tr -d ' ')
DB_HOST=$(awk -F "=" '/host/ {print $2}' db_config.ini | tr -d ' ')
DB_PORT=$(awk -F "=" '/port/ {print $2}' db_config.ini | tr -d ' ')

# Path to CSV file
CITATION_PATH="data/publication/wos-citation.csv"
PMID_PATH="data/publication/wosid-pmid.csv"

# SQL command to create the table
SQL1_CMD="CREATE TABLE uid_cit_count (
    uid varchar,
    citation_ct int8,
    pmid varchar
);"

SQL2_CMD="\COPY wos_citation(uid,citation_ct) FROM '$CITATION_PATH' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';"

SQL3_CMD="\COPY (select wosid,pmid from wosid_to_pmid) TO '$PMID_PATH' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';"

SQL4_CMD="create table wosid_to_pmid (uid varchar,pmid varchar);  "

SQL5_CMD="\COPY wosid_to_pmid FROM '$PMID_PATH' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';"

SQL6_CMD="update uid_cit_count set pmid=wosid_to_pmid.pmid from wosid_to_pmid where uid_cit_count.uid=wosid_to_pmid.uid"

# Execute the SQL command
PGPASSWORD=$DB_PASS psql -d $DB_NAME -U $DB_USER -h $DB_HOST -p $DB_PORT -c "$SQL1_CMD" -c "$SQL2_CMD"

PGPASSWORD=$DB_PASS psql -d "pubmed19" -U $DB_USER -h $DB_HOST -p $DB_PORT -c "$SQL3_CMD"

PGPASSWORD=$DB_PASS psql -d $DB_NAME -U $DB_USER -h $DB_HOST -p $DB_PORT -c "$SQL4_CMD" -c "$SQL5_CMD" -c "$SQL6_CMD"

echo "Wos_citation imported successfully!"
