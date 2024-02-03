#!/bin/bash

HOST=$(awk -F "=" '/host/ {print $2}' db_config.ini)
PORT=$(awk -F "=" '/port/ {print $2}' db_config.ini)
DBNAME=$(awk -F "=" '/dbname/ {print $2}' db_config.ini)
USER=$(awk -F "=" '/user/ {print $2}' db_config.ini)

pg_dump \
  -h $HOST \
  -U $USER  \
  -d $DBNAME \
  -p $PORT \
  -t hralit_asctb_publication \
  -t hralit_author \
  -t hralit_author_institution \
  -t hralit_creator \
  -t hralit_dataset \
  -t hralit_digital_objects \
  -t hralit_donor \
  -t hralit_funder_cleaned \
  -t hralit_funding \
  -t hralit_institution \
  -t hralit_anatomical_structures \
  -t hralit_biomarkers \
  -t hralit_cell_types \
  -t hralit_triple \
  -t hralit_asctb_linkage \
  -t hralit_pub_funding_funder \
  -t hralit_publication \
  -t hralit_publication_author \
  -t hralit_reviewer \
  -t hralit_other_publication \
  -t hralit_organ \
  -t hralit_publication_subject \
  -f data/db/hralit.sql
