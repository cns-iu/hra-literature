#!/bin/bash
#Build diagram of HRAlit database using schemaspy

java -jar schemaspy-6.2.4.jar \
-dp postgresql-42.6.0.jar \
-t pgsql \
-db database_name \
-host host_name \
-port port_number \
-u username \
-p password \
-o outputDir \
-i "hralit_asct_publication|hralit_author|hralit_author_expertise|hralit_author_institution|hralit_creator|hralit_dataset|hralit_digital_object_5th_release|hralit_donor|hralit_funder_cleaned|hralit_funding|hralit_institution|hralit_ontology_anatomical_structures|hralit_ontology_biomarkers|hralit_ontology_cell_types|hralit_ontology_triple|hralit_pub_funding_funder|hralit_publication|hralit_publication_author|hralit_publication_subject|hralit_reviewer" \
-meta data/db/schemameta.xml \
-noimplied