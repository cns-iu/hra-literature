-- create tables for each entity type

create table hralit_asct_publication (
    organ varchar,
    id varchar,
    doi varchar,
    notes varchar,
    type varchar
);

create table hralit_author (
    orcid varchar,
    first_name varchar,
    last_name varchar,
    first_pubyear int8,
    career_age int8,
    involved_funding int8
);

create table hralit_creator (
    orcid varchar,
    full_name varchar,
    first_name varchar,
    last_name varchar,
    version varchar,
    name varchar,
    type varchar,
    organ varchar,
    hubmap_id varchar
);

create table hralit_dataset (
    dataset_id character varying,
    organ_gtex_id character varying,
    donor_id character varying,
    individual_id character varying,
    protocols_used character varying,
    rin_score_from_paxgene character varying,
    rin_score_from_frozen character varying,
    organ character varying,
    autolysis_score character varying,
    sample_ischemic_time character varying,
    sample_type character varying,
    pathology_notes character varying,
    source character varying,
    dataset_hubmap_id character varying,
    dataset_status character varying,
    dataset_group_name character varying,
    dataset_group_uuid character varying,
    dataset_date_time_created character varying,
    dataset_created_by_email character varying,
    dataset_date_time_modified character varying,
    dataset_modified_by_email character varying,
    lab_id_or_name character varying,
    dataset_data_types character varying,
    dataset_portal_url character varying,
    first_sample_hubmap_id character varying,
    first_sample_submission_id character varying,
    first_sample_uuid character varying,
    first_sample_type character varying,
    first_sample_portal_url character varying,
    organ_hubmap_id character varying,
    organ_submission_id character varying,
    organ_uuid character varying,
    donor_submission_id character varying,
    donor_uuid character varying,
    donor_group_name character varying,
    rui_location_hubmap_id character varying,
    rui_location_submission_id character varying,
    rui_location_uuid character varying,
    sample_metadata_hubmap_id character varying,
    sample_metadata_submission_id character varying,
    sample_metadata_uuid character varying,
    processed_dataset_uuid character varying,
    dataset_title character varying,
    dataset_h5ad_path character varying,
    dataset_total_cell_count character varying,
    collection_id character varying,
    collection_name character varying,
    publication_doi character varying,
    organ_ontology character varying,
    anatomical_structure character varying,
    anatomical_structure_ontology character varying,
    suspension_type character varying
);

create table hralit_digital_object_5th_release(
    type varchar,
    name varchar,
    version varchar,
    title varchar,
    license varchar,
    publisher varchar,
    hubmap_id varchar,
    doi varchar
);

create table hralit_donor (
    donor_id character varying,
    sex character varying,
    age character varying,
    death_event character varying,
    source character varying,
    age_unit character varying,
    weight character varying,
    weight_unit character varying,
    height character varying,
    height_unit character varying,
    race character varying,
    body_mass_index character varying,
    body_mass_index_unit character varying,
    blood_type character varying,
    rh_blood_group character varying,
    rh_factor character varying,
    kidney_donor_profile_index character varying,
    kidney_donor_profile_index_unit character varying,
    cause_of_death character varying,
    medical_history character varying,
    mechanism_of_injury character varying,
    social_history character varying,
    sex_ontotlogy character varying,
    race_ontotlogy character varying
);

create table hralit_funder_cleaned (
    soa_funder_id varchar,
    funder_name varchar,
    country_code varchar
);

create table hralit_funding (
    funding_id varchar,
    acronym varchar
);

create table hralit_institution (
    soa_institution_id varchar,
    ror varchar,
    institution_name varchar,
    institution_type varchar,
    country_code varchar
);

create table hralit_ontology_anatomical_structures (
    id varchar,
    rdfs_label varchar,
    name varchar
);

create table hralit_ontology_cell_types (
    id varchar,
    rdfs_label varchar,
    name varchar
);

create table hralit_ontology_biomarkers (
    id varchar,
    rdfs_label varchar,
    name varchar,
    b_type varchar
);

create table hralit_publication(
    pmid varchar,
    doi varchar,
    pubyear int8,
    article_title varchar,
    journal_title varchar
);

create table hralit_reviewer (
    orcid varchar,
    full_name varchar,
    first_name varchar,
    last_name varchar,
    version varchar,
    name varchar,
    type varchar,
    organ varchar,
    hubmap_id varchar
);


-- create tables for linking

create table hralit_author_expertise(
    orcid varchar,
    expertise varchar,
    expertise_type varchar
);

create table hralit_author_institution (
    orcid varchar,
    soa_institution_id varchar
);

create table hralit_pub_funding_funder (
    pmid varchar,
    funding_id varchar,
    acronym varchar,
    funder_name_pubmed varchar,
    soa_funder_id varchar,
    country varchar
);

create table hralit_ontology_triangle(
    row_id varchar,
    id varchar,
    rdfs_label varchar,
    name varchar,
    b_type varchar,
    organ varchar,
    ontology_type varchar
);

create table hralit_publication_author (
    pmid varchar,
    orcid varchar
);

create table hralit_publication_subject (
    pmid varchar,
    organ varchar
);


