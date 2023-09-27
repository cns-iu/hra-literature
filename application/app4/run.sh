#!/bin/bash

python3 application/app4/0-author-gender-race.py
python3 application/app4/1-expert-race.py

# Extract database config details
HOST=$(awk -F "=" '/host/ {print $2}' db_config.ini)
PORT=$(awk -F "=" '/port/ {print $2}' db_config.ini)
DBNAME=$(awk -F "=" '/dbname/ {print $2}' db_config.ini)
USER=$(awk -F "=" '/user/ {print $2}' db_config.ini)
PASSWORD=$(awk -F "=" '/password/ {print $2}' db_config.ini)

# Use psql to execute SQL commands
export PGPASSWORD=$PASSWORD

psql -h $HOST -p $PORT -d $DBNAME -U $USER -a -f application/app4/2-author-geo.sql

unset PGPASSWORD

python3 application/app4/3-vis-geomap.py