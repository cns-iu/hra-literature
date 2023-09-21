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

\copy soa_institution from data/institutions/orcid-authors-institution.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

CREATE TABLE soa_institution_metadata (
    soa_institution_id character varying,
    ror character varying,
    institution_name character varying,
    institution_type character varying,
    country_code character varying
);

\copy soa_institution_metadata from data/institutions/soa-institution.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';


insert into hralit_institution_2 (soa_institution_id,ror,institution_name,institution_type,country_code)
select soa_institution_id,ror,institution_name,institution_type,country_code 
from soa_institution
where soa_institution_id in 
    (select soa_institution_id from hralit_author_institution_2 where soa_institution_id is not null)
    and soa_institution_id is not null
group by soa_institution_id,ror,institution_name,institution_type,country_code;

update hralit_institution set institution_name=soa_institution_metadata.institution_name 
from soa_institution_metadata 
where hralit_institution.soa_institution_id=soa_institution_metadata.soa_institution_id;