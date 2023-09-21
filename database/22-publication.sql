-- publication data:

-- publications in asct+b tables
\copy hralit_asct_publication from data/publication/hra-refs-cleaned.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

-- publications for 31 organs
insert into hralit_publication_subject_2(pmid,organ)
select pmid,organ
from pmid_31_organs
group by pmid,organ;

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
    select pmid from pmid_31_organs
    union
    select pmid from hralit_other_refs
),
t3 as (
    SELECT doi from hralit_asct_publication
    union
    SELECT regexp_replace(publication_doi, '^(http://dx\.doi\.org/|doi\.org/|http://doi\.org/|https://doi\.org/|doi:|DOI:)', '', 'gi') as doi from hralit_dataset
)
insert into hralit_publication_2(pmid,doi,pubyear,article_title,journal_title)
select pmid,doi,pub_year,article_title,journal_title 
    from t1
    where pmid in (select pmid from t2 where pmid is not null) 
        or lower(doi) in (select lower(doi) from t3 where doi is not null);


insert into hralit_publication_subject (pmid, organ)
select pmid, organ
from pmid_34_organs
where pmid is not null and organ is not null;

