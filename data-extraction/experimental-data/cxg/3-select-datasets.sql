\copy (
    SELECT 
        dataset_id,
        cxg_dataset_id,
        tissue_general,
        tissue_general_ontology_term_id,
        tissue,
        tissue_ontology_term_id,
        suspension_type,
        donor_id,
        dataset_title,
        dataset_h5ad_path,
        dataset_total_cell_count,
        collection_id,
        collection_name,
        collection_doi
    FROM 
        cxg_cell_metadata
    WHERE 
        development_stage ~ '(\d+)-year-old human stage'
        AND SUBSTRING(development_stage, '\d+')::integer >= 19
        AND disease = 'normal'
    GROUP BY 
        dataset_id,
        cxg_dataset_id,
        tissue_general,
        tissue_general_ontology_term_id,
        tissue,
        tissue_ontology_term_id,
        suspension_type,
        donor_id,
        dataset_title,
        dataset_h5ad_path,
        dataset_total_cell_count,
        collection_id,
        collection_name,
        collection_doi
) TO data/experimental/cxg_healthy_human_adult_datasets.csv DELIMITER E',' CSV HEADER ENCODING 'SQL-ASCII';
