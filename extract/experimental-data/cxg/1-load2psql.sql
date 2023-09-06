-- create tables

CREATE TABLE cxg_cell_metadata (
    id                                       int8,
    soma_joinid                              int8,
    dataset_id                               VARCHAR,
    assay                                    VARCHAR,
    assay_ontology_term_id                   VARCHAR,
    cell_type                                VARCHAR,
    cell_type_ontology_term_id               VARCHAR,
    development_stage                        VARCHAR,
    development_stage_ontology_term_id       VARCHAR,
    disease                                  VARCHAR,
    disease_ontology_term_id                 VARCHAR,
    donor_id                                 VARCHAR,
    is_primary_data                          VARCHAR,
    self_reported_ethnicity                  VARCHAR,
    self_reported_ethnicity_ontology_term_id VARCHAR,
    sex                                      VARCHAR,
    sex_ontology_term_id                     VARCHAR,
    suspension_type                          VARCHAR,
    tissue                                   VARCHAR,
    tissue_ontology_term_id                  VARCHAR,
    tissue_general                           VARCHAR,
    tissue_general_ontology_term_id          VARCHAR
);

CREATE TABLE cxg_datasets (
    id                       BIGINT,
    soma_joinid              BIGINT,
    collection_id            VARCHAR,
    collection_name          VARCHAR,
    collection_doi           VARCHAR,
    dataset_id               VARCHAR,
    dataset_title            VARCHAR,
    dataset_h5ad_path        VARCHAR,
    dataset_total_cell_count int8
);

CREATE TABLE cxg_gene_metadata (
    id             int8,
    soma_joinid    int8,
    feature_id     VARCHAR,
    feature_name   VARCHAR,
    feature_length int8
);

CREATE TABLE cxg_summary (
    id                int8,
    soma_joinid       int8,
    organism          VARCHAR,
    category          VARCHAR,
    ontology_term_id  VARCHAR,
    unique_cell_count int8,
    total_cell_count  int8,
    label             VARCHAR
);


-- insert data
\copy cxg_datasets from data/experimental/cxg_datasets.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy cxg_summary from data/experimental/cxg_summary.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy cxg_cell_metadata from data/experimental/cxg_cell_metadata.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy cxg_gene_metadata from data/experimental/cxg_gene_metadata.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';