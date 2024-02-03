#!/bin/bash


# Extract values from db_config.ini
DB_NAME=$(awk -F "=" '/dbname/ {print $2}' db_config.ini)
DB_HOST=$(awk -F "=" '/host/ {print $2}' db_config.ini)
DB_PORT=$(awk -F "=" '/port/ {print $2}' db_config.ini)
DB_USER=$(awk -F "=" '/user/ {print $2}' db_config.ini)
DB_PASS=$(awk -F "=" '/password/ {print $2}' db_config.ini)

echo "DB_NAME: $DB_NAME"
echo "DB_HOST: $DB_HOST"

#Build diagram of HRAlit database using schemaspy
java -jar  data/db/schemaspy-6.2.4.jar \
-dp data/db/postgresql-42.6.0.jar \
-t pgsql \
-db $DB_NAME \
-host $DB_HOST \
-port $DB_PORT \
-u $DB_USER \
-p $DB_PASS \
-o data/db/outputDir \
-i "hralit_asctb_publication|hralit_author|hralit_author_institution|hralit_creator|hralit_dataset|hralit_digital_objects|hralit_donor|hralit_funder_cleaned|hralit_funding|hralit_institution|hralit_anatomical_structures|hralit_biomarkers|hralit_cell_types|hralit_triple|hralit_asctb_linkage|hralit_pub_funding_funder|hralit_publication|hralit_publication_author|hralit_publication_subject|hralit_reviewer|hralit_other_publication|hralit_organ|hralit_anatomical_structures" \
-meta data/db/schemameta.xml \
-noimplied
