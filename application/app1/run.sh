#!/bin/bash

python3 application/app1/dataset-ct.py
python3 application/app1/30-fund-cost-ardc.py
python3 application/app1/31-fund-cost-ec.py
python3 application/app1/32-fund-cost-kaken.py
python3 application/app1/33-fund-cost-cihr.py
python3 application/app1/34-fund-cost-nsf.py
python3 application/app1/35-fund-cost-nih.py
python3 application/app1/36-fund-cost-merge.py
python3 application/app1/37-exchange.py


# Extract database config details
HOST=$(awk -F "=" '/host/ {print $2}' db_config.ini)
PORT=$(awk -F "=" '/port/ {print $2}' db_config.ini)
DBNAME=$(awk -F "=" '/dbname/ {print $2}' db_config.ini)
USER=$(awk -F "=" '/user/ {print $2}' db_config.ini)
PASSWORD=$(awk -F "=" '/password/ {print $2}' db_config.ini)

# Use psql to execute SQL commands
export PGPASSWORD=$PASSWORD

psql -h $HOST -p $PORT -d $DBNAME -U $USER -a -f application/app1/pub-trend.sql \
                                              -f application/app1/pub-ct.sql \
                                              -f application/app1/funding-ct.sql \
                                              -f application/app1/expert-ct.sql

psql -h $HOST -p $PORT -d $DBNAME -U $USER -a -f application/app1/50-pub-trend.sql

unset PGPASSWORD

