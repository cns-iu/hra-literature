#!/bin/bash

# Database connection details
DB_NAME="wos_2018"
DB_USER=$(awk -F "=" '/user/ {print $2}' db_config.ini | tr -d ' ')
DB_PASS=$(awk -F "=" '/password/ {print $2}' db_config.ini | tr -d ' ')
DB_HOST=$(awk -F "=" '/host/ {print $2}' db_config.ini | tr -d ' ')
DB_PORT=$(awk -F "=" '/port/ {print $2}' db_config.ini | tr -d ' ')

# Path to CSV file
CITATION_PATH="data/publication/wos-citation.csv"

# SQL command to get the citation count and save to CSV
SQL_CMD="\COPY (
            with a as( 
                SELECT ref_id as uid, COUNT(DISTINCT uid) AS citation_ct 
                FROM wos_references  
                WHERE uid IS NOT NULL and ref_id IS NOT NULL  
                GROUP BY ref_id)
            select uid,citation_ct from a group by uid,citation_ct
) TO '$CITATION_PATH' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';"

# Execute the SQL command
PGPASSWORD=$DB_PASS psql -d $DB_NAME -U $DB_USER -h $DB_HOST -p $DB_PORT -c "$SQL_CMD"

echo "WoS-citation exported successfully to $OUTPUT_FILE!"

