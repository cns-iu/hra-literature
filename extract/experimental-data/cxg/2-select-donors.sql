\copy (
    SELECT 
        (dataset_id || '-' || donor_id) AS donors,
        self_reported_ethnicity,
        self_reported_ethnicity_ontology_term_id,
        sex,
        sex_ontology_term_id,
        suspension_type,
        development_stage
    FROM 
        cxg_cell_metadata
    WHERE 
        development_stage ~ '(\d+)-year-old human stage'
        AND SUBSTRING(development_stage, '\d+')::integer >= 19
        AND disease = 'normal'
    GROUP BY 
        donors,
        self_reported_ethnicity,
        self_reported_ethnicity_ontology_term_id,
        sex,
        sex_ontology_term_id,
        suspension_type,
        development_stage
) TO data/experimental/cxg_donors_metadata.csv DELIMITER E',' CSV HEADER ENCODING 'SQL-ASCII';
