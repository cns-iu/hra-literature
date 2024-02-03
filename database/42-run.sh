#!/bin/bash

# database/30-diagrams.sh
# database/31-dot2svg.sh
# database/40-export-db.sh

# Extract database config details
HOST=$(awk -F "=" '/host/ {print $2}' db_config.ini)
PORT=$(awk -F "=" '/port/ {print $2}' db_config.ini)
DBNAME=$(awk -F "=" '/dbname/ {print $2}' db_config.ini)
USER=$(awk -F "=" '/user/ {print $2}' db_config.ini)
PASSWORD=$(awk -F "=" '/password/ {print $2}' db_config.ini)

# Use psql to execute SQL commands
export PGPASSWORD=$PASSWORD

psql -h $HOST -p $PORT -d $DBNAME -U $USER -a -f database/41-export-csv.sql

unset PGPASSWORD

