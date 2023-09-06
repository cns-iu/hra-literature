#!/bin/bash

pg_dump \
  -h dbr.cns.iu.edu \
  -U yokong \
  -d yokong \
  -t hralit_asct_publication \
  -t hralit_author \
  -t hralit_author_expertise \
  -t hralit_author_institution \
  -t hralit_creator \
  -t hralit_dataset \
  -t hralit_digital_object_5th_release \
  -t hralit_donor \
  -t hralit_funder_cleaned \
  -t hralit_funding \
  -t hralit_institution \
  -t hralit_ontology_anatomical_structures \
  -t hralit_ontology_biomarkers \
  -t hralit_ontology_cell_types \
  -t hralit_ontology_triangle \
  -t hralit_pub_funding_funder \
  -t hralit_publication \
  -t hralit_publication_author \
  -t hralit_reviewer \
  -f hralit.sql
