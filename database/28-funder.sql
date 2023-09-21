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

insert into cleaned_funder_2(pmid,grant_id,country,acronym,funder_name_pubmed,funder_soa_id)
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


insert into hralit_pub_funding_funder_2(
    pmid, funding_id, acronym, funder_name_pubmed, soa_funder_id, country)
select 
    pmid, grant_id, acronym, 
    funder_name_pubmed, funder_soa_id, country
from cleaned_funder_2
where pmid in (select pmid from hralit_publication_2 where pmid is not null)
    and pmid is not null
    and grant_id is not null;


insert into hralit_funder_cleaned_2 (soa_funder_id,funder_name,country_code)
select funder_id,funder_name,country_code
from funder_meta
where funder_id in (select soa_funder_id from hralit_pub_funding_funder_2 where soa_funder_id is not null)
    and funder_id is not null;

