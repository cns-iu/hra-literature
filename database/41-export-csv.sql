-- export tables of hralit database in CSV format

\COPY (SELECT * FROM hralit_asct_publication) TO 'hralit/hralit_asct_publication.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_author) TO 'hralit/hralit_author.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_author_expertise) TO 'hralit/hralit_author_expertise.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_author_institution) TO 'hralit/hralit_author_institution.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_creator) TO 'hralit/hralit_creator.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_dataset) TO 'hralit/hralit_dataset.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_digital_object_5th_release) TO 'hralit/hralit_digital_object_5th_release.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_donor) TO 'hralit/hralit_donor.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_funder_cleaned) TO 'hralit/hralit_funder_cleaned.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_funding) TO 'hralit/hralit_funding.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_institution) TO 'hralit/hralit_institution.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_ontology_anatomical_structures) TO 'hralit/hralit_ontology_anatomical_structures.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_ontology_biomarkers) TO 'hralit/hralit_ontology_biomarkers.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_ontology_cell_types) TO 'hralit/hralit_ontology_cell_types.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_ontology_triangle) TO 'hralit/hralit_ontology_triangle.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_pub_funding_funder) TO 'hralit/hralit_pub_funding_funder.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_publication) TO 'hralit/hralit_publication.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_publication_author) TO 'hralit/hralit_publication_author.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_reviewer) TO 'hralit/hralit_reviewer.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
\COPY (SELECT * FROM hralit_publication_subject) TO 'hralit/hralit_publication_subject.csv' WITH CSV HEADER DELIMITER E',' ENCODING 'SQL-ASCII';
