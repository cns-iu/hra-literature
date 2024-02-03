#!/bin/bash

# Database connection details
DB_NAME=$(awk -F "=" '/dbname/ {print $2}' db_config.ini | tr -d ' ')
DB_USER=$(awk -F "=" '/user/ {print $2}' db_config.ini | tr -d ' ')
DB_PASS=$(awk -F "=" '/password/ {print $2}' db_config.ini | tr -d ' ')
DB_HOST=$(awk -F "=" '/host/ {print $2}' db_config.ini | tr -d ' ')
DB_PORT=$(awk -F "=" '/port/ {print $2}' db_config.ini | tr -d ' ')

# Path to CSV file
PUBMED_PATH="data/publication/pubmed-pubs.csv"

# SQL command to create the table
SQL_CMD="CREATE TABLE pmid_31_organs (
    pmid varchar,
    organ varchar,
    uid varchar
);"

# Execute the SQL command
PGPASSWORD=$DB_PASS psql -d $DB_NAME -U $DB_USER -h $DB_HOST -p $DB_PORT -c "$SQL_CMD"

# Use \COPY to import the CSV data
PGPASSWORD=$DB_PASS psql -d $DB_NAME -U $DB_USER -h $DB_HOST -p $DB_PORT -c "\COPY pmid_31_organs FROM '$PUBMED_PATH' DELIMITER ',' CSV HEADER;"

echo "Data imported successfully!"
