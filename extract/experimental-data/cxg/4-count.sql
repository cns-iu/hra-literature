#count tissue_general_ontology
select count(distinct(tissue_general_ontology_term_id)) from cxg_cell_metadata where development_stage ~ '(\d+)-year-old human stage'AND SUBSTRING(development_stage, '\d+')::integer >= 19 and disease='normal';

#count tissue_ontology
select count(distinct(tissue_ontology_term_id)) from cxg_cell_metadata where development_stage ~ '(\d+)-year-old human stage'AND SUBSTRING(development_stage, '\d+')::integer >= 19 and disease='normal';

#count CT_ontology
select count(distinct(cell_type_ontology_term_id)) from cxg_cell_metadata where development_stage ~ '(\d+)-year-old human stage'AND SUBSTRING(development_stage, '\d+')::integer >= 19 and disease='normal';

#count gene
select count(distinct(feature_id)) from cxg_gene_metadata;

#count publications
select count(distinct(collection_doi)) from cxg_datasets where dataset_id in (select dataset_id from cxg_cell_metadata where development_stage ~ '(\d+)-year-old human stage'AND SUBSTRING(development_stage, '\d+')::integer >= 19 and disease='normal');

#count datasets for healthy human adults
select count(distinct(dataset_id)) from cxg_datasets where dataset_id in (select dataset_id from cxg_cell_metadata where development_stage ~ '(\d+)-year-old human stage'AND SUBSTRING(development_stage, '\d+')::integer >= 19 and disease='normal');

#count AS-CT
with a as(select cell_type_ontology_term_id,tissue_ontology_term_id,tissue_general_ontology_term_id from cxg_cell_metadata where development_stage ~ '(\d+)-year-old human stage'AND SUBSTRING(development_stage, '\d+')::integer >= 19 and disease='normal'),b as (select cell_type_ontology_term_id,tissue_ontology_term_id,tissue_general_ontology_term_id from a group by cell_type_ontology_term_id,tissue_ontology_term_id,tissue_general_ontology_term_id )select count(*) from b;

#count experts(orcid_id) in cxg for healthy human adults
with a as (select distinct(collection_doi) from cxg_datasets where dataset_id in (select dataset_id from cxg_cell_metadata where development_stage ~ '(\d+)-year-old human stage'AND SUBSTRING(development_stage, '\d+')::integer >= 19 and disease='normal')), b as (select uid from uid_identifier where identifier_value in (select collection_doi from a)) select count(distinct(identifier)) from pmid_author where pmid in (select pmid from wosid_to_pmid);
