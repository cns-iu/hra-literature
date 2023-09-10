#!/bin/bash

# Database connection details
DB_NAME="your_dbname"
DB_USER="your_username"
DB_PASS="your_password"
DB_HOST="your_host"
DB_PORT="your_port"

# Path to CSV file
PUBMED_PATH="data/publication/pubmed-pubs.csv"
WOS_PATH="data/publication/wos-pubs.csv"

# SQL command to create the table
SQL1_CMD="CREATE TABLE pmid_34_organs (
    pmid varchar,
    organ varchar,
    uid varchar
);"

SQL2_CMD="CREATE TABLE uid_34_organs (
    uid varchar,
    organ varchar
);"

# Execute the SQL command
PGPASSWORD=$DB_PASS psql -d $DB_NAME -U $DB_USER -h $DB_HOST -p $DB_PORT -c "$SQL1_CMD"
PGPASSWORD=$DB_PASS psql -d $DB_NAME -U $DB_USER -h $DB_HOST -p $DB_PORT -c "$SQL2_CMD"

# Use \COPY to import the CSV data
PGPASSWORD=$DB_PASS psql -d $DB_NAME -U $DB_USER -h $DB_HOST -p $DB_PORT -c "\COPY pmid_34_organs FROM '$PUBMED_PATH' DELIMITER ',' CSV HEADER;"

PGPASSWORD=$DB_PASS psql -d $DB_NAME -U $DB_USER -h $DB_HOST -p $DB_PORT -c "\COPY uid_34_organs FROM '$WOS_PATH' DELIMITER ',' CSV HEADER;"


echo "Data imported successfully!"
