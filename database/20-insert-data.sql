-- ontology data: insert data from data-extraction step
\copy hralit_ontology_anatomical_structures from data/ontology/asct_anatomical_structures.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy hralit_ontology_cell_types from ata/ontology/asct_cell_types.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy hralit_ontology_biomarkers from ata/ontology/asct_biomarkers.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';


-- experimental data:
-- donors, datasets, digital objects 5th release

\copy hralit_donor from data/experimental/harmonized_donor.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy hralit_dataset from data/experimental/merged_datasets.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy hralit_digital_object_5th_release from data/experimental/hra_do_5th_release.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';



-- publication data:

-- publications in asct+b tables
\copy hralit_asct_publication from data/publication/hra-refs-cleaned.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

-- publications for different organs
with t1 as (
    select 
        pmid_pub.pmid,
        regexp_replace(doi, '^(http://dx\.doi\.org/|doi\.org/|http://doi\.org/|https://doi\.org/|doi: |DOI: |doi:|DOI:)', '', 'gi') as doi,
        pub_year :: integer as pub_year,
        article_title,
        journal_title 
    from pmid_pub
    left join pmid_doi on pmid_pub.pmid=pmid_doi.pmid),
t2 as (
    SELECT unnest(regexp_matches(id, 'PMID:\s*([0-9]+)|([0-9]+)', 'i')) as pmid FROM hralit_asct_publication
    union
    select pmid from pmid_34_organs
),
t3 as (
    SELECT doi from hralit_asct_publication
    union
    SELECT regexp_replace(publication_doi, '^(http://dx\.doi\.org/|doi\.org/|http://doi\.org/|https://doi\.org/|doi:|DOI:)', '', 'gi') as doi from hralit_dataset
)
insert into hralit_publication(pmid,doi,pubyear,article_title,journal_title)
select pmid,doi,pub_year,article_title,journal_title 
    from t1
    where pmid in (select pmid from t2 where pmid is not null) 
        or lower(doi) in (select lower(doi) from t3 where doi is not null);



-- expert data:
\copy hralit_creator from /data/experts/hralit_creators.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy hralit_reviewer from /data/experts/hralit_reviewers.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

with t1 as (
    select 
        regexp_replace(identifier, '.*([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]).*', '\1') as orcid,
        grant_id
    from pmid_author
    join pmid_grant_all on pmid_author.pmid=pmid_grant_all.pmid
    group by orcid,grant_id
),
t2 as (
    select orcid,count(*) as involved_funding
    from t1
    where orcid is not null and orcid !=''
    group by orcid
),
t3 as (
    select cleaned_author_info.orcid,first_name,last_name,first_pubyear,career_age,involved_funding
    from cleaned_author_info
    left join t2 on REPLACE(cleaned_author_info.orcid,'https://orcid.org/','')=t2.orcid
)
insert into hralit_author(orcid,first_name,last_name,first_pubyear,career_age,involved_funding)
    select orcid,first_name,last_name,first_pubyear :: integer,career_age ,involved_funding from t3
    where REPLACE(orcid,'https://orcid.org/','') in (select regexp_replace(author_id, '.*([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]).*', '\1')from asct_expert)
        or REPLACE(orcid,'https://orcid.org/','') in (select regexp_replace(identifier, '.*([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]).*', '\1') from pmid_author 
                where pmid in (select pmid from hralit_publication))
        or REPLACE(orcid,'https://orcid.org/','') in (select orcid from hralit_creator)
        or REPLACE(orcid,'https://orcid.org/','') in (select orcid from hralit_reviewer);


insert into hralit_author(orcid,first_name,last_name)
    select 
        'https://orcid.org/' || orcid,
        first_name,
        last_name
    from hralit_creator 
    where orcid not in (select REPLACE(orcid,'https://orcid.org/','') from hralit_author where orcid is not null);

insert into hralit_author(orcid,first_name,last_name)
    select 
        'https://orcid.org/' || orcid,
        first_name,
        last_name
    from hralit_reviewer 
    where orcid not in (select REPLACE(orcid,'https://orcid.org/','') from hralit_author where orcid is not null);


-- institution data: use SemOpenAlex funder data to clean

CREATE TABLE soa_institution (
    soa_author_id character varying,
    orcid character varying,
    country_code character varying,
    ror character varying,
    soa_institution_id character varying,
    institution_name character varying,
    institution_type character varying
);

\copy data/institutions/soa_institution from orcid-authors-institution.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

insert into hralit_institution (soa_institution_id,ror,institution_name,institution_type,country_code)
select soa_institution_id,ror,institution_name,institution_type,country_code 
from soa_institution
where soa_institution_id in 
    (select soa_institution_id from hralit_author_institution where soa_institution_id is not null)
    and soa_institution_id is not null
group by soa_institution_id,ror,institution_name,institution_type,country_code;




-- funding data:

insert into hralit_funding (funding_id,acronym)
select grant_id, acronym
from pmid_grant_all
where pmid in (select pmid from hralit_publication where pmid is not null)
    and pmid is not null
    and grant_id is not null
group by grant_id, acronym;




-- funder data: use SemOpenAlex funder data to clean
CREATE TABLE funder_meta (
    funder_id character varying,
    funder_name character varying,
    country_code character varying,
    grants_count int8,
    publications_count int8
);

\copy funder_meta from data/funders/funders_soa.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

CREATE TABLE soa_funder (
    iri_id character varying,
    pmid character varying,
    funder character varying,
    funder_name character varying,
    grant_id character varying
);

\copy soa_funder from data/funders/pmid-works-grants.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

create table cleaned_funder (
    pmid varchar,
    grant_id varchar,
    country varchar,
    acronym varchar,
    funder_name_pubmed varchar,
    funder_soa_id varchar
);

insert into cleaned_funder(pmid,grant_id,country,acronym,funder_name_pubmed,funder_soa_id)
SELECT 
    t1.pmid, 
    t1.grant_id,
    country,
    acronym,
    agency,
    funder
FROM pmid_grant_all t1 
left join soa_funder t2
    on lower(t1.grant_id) = lower(t2.grant_id)
       And t1.pmid=REPLACE(t2.pmid,'https://pubmed.ncbi.nlm.nih.gov/','')
group by t1.pmid,t1.grant_id,country,acronym,agency,funder;

insert into hralit_funder_cleaned (soa_funder_id,funder_name,country_code)
select funder_id,funder_name,country_code
from funder_meta
where funder_id in (select funder_soa_id from cleaned_funder where funder_soa_id is not null)
    and funder_id is not null;



--insert data for relationships

\copy hralit_ontology_triangle from data/ontology/hralit_ontology_triangle.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

insert into hralit_pub_funding_funder(
    pmid, funding_id, acronym, funder_name_pubmed, soa_funder_id, country)
select 
    pmid, grant_id, acronym, 
    funder_name_pubmed, funder_soa_id, country
from cleaned_funder
where pmid in (select pmid from hralit_publication where pmid is not null)
    and pmid is not null
    and grant_id is not null;

insert into hralit_publication_author (pmid, orcid)
select 
    pmid, 
    'https://orcid.org/' || regexp_replace(identifier, '.*([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]).*', '\1') AS orcid
from pmid_author
where pmid in (select pmid from hralit_publication where pmid is not null)
    and pmid is not null
    and regexp_replace(identifier, '.*([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]).*', '\1') !='';

insert into hralit_author_expertise (orcid, expertise, expertise_type)
select 
    'https://orcid.org/' || regexp_replace(author_id, '.*([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]).*', '\1') AS orcid,
    name,
    level
from asct_expert
where  regexp_replace(author_id, '.*([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]).*', '\1') !=''
    and name is not null;

insert into hralit_publication_subject (pmid, organ)
select pmid, organ
from pmid_34_organs
where pmid is not null and organ is not null;

