-- ontology data: insert data from data-extraction step
\copy hralit_ontology_anatomical_structures from data/ontology/asct_anatomical_structures.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy hralit_ontology_cell_types from ata/ontology/asct_cell_types.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy hralit_ontology_biomarkers from ata/ontology/asct_biomarkers.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

--insert data for relationships

\copy hralit_ontology_triple from data/ontology/hralit_ontology_triple.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy hralit_asctb_linkage from data/ontology/asctb_linkage.csv WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';

-- experimental data:
-- donors, datasets, digital objects 5th release

\copy hralit_donor from data/experimental/harmonized_donor.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy hralit_dataset from data/experimental/merged_datasets.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy hralit_digital_object_5th_release from data/experimental/hra_do_5th_release.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy hralit_organ from data/experimental/organ.csv WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';