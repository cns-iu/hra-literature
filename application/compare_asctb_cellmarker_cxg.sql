\t on
\a
\pset fieldsep ','
\pset format csv
\pset tuples_only off
\o /mnt/c/users/yokong/documents/com.csv

with cellmarker_doi as (
    select pmid,doi from pmid_doi where pmid in (select pmid from cellmarker where pmid is not null) and pmid is not null
),
hralit_asct_publication_2 AS (
    SELECT lower(substring(doi from '10\.\d+\/[-._;()<>/+:A-Za-z0-9]+')) AS doi 
    FROM hralit_asct_publication
    WHERE doi ~ '10\.\d+\/[-._;()<>/+:A-Za-z0-9]+'
),
cellmarker_doi_2 AS (
    SELECT lower(substring(doi from '10\.\d+\/[-._;()<>/+:A-Za-z0-9]+')) AS doi 
    FROM cellmarker_doi
    WHERE doi ~ '10\.\d+\/[-._;()<>/+:A-Za-z0-9]+'
),
hralit_dataset_2 as (
    SELECT lower(substring(publication_doi from '10\.\d+\/[-._;()<>/+:A-Za-z0-9]+')) AS doi  FROM hralit_dataset
    WHERE publication_doi ~ '10\.\d+\/[-._;()<>/+:A-Za-z0-9]+'
),
DOI_CTE AS (
    -- Create a unified list of DOIs from all three tables
    SELECT doi FROM hralit_asct_publication_2
    UNION
    SELECT doi FROM cellmarker_doi_2
    UNION
    SELECT doi FROM hralit_dataset_2
),

DOI_Presence_CTE AS (
    -- Check presence of DOIs in each table
    SELECT 
        d.doi,
        CASE WHEN a.doi IS NOT NULL THEN 1 ELSE 0 END AS in_asctb_5th,
        CASE WHEN b.doi IS NOT NULL THEN 1 ELSE 0 END AS in_cellmarker,
        CASE WHEN c.doi IS NOT NULL THEN 1 ELSE 0 END AS in_cxg
    FROM DOI_CTE d
    LEFT JOIN hralit_asct_publication_2 a ON d.doi = a.doi
    LEFT JOIN cellmarker_doi_2 b ON d.doi = b.doi
    LEFT JOIN hralit_dataset_2 c ON d.doi = c.doi
),
Author_Aggregation as (
    select a.doi,d.first_name,d.last_name,c.pub_year,c.article_title
    from DOI_Presence_CTE a
    left join pmid_doi b on a.doi=lower(substring(b.doi from '10\.\d+\/[-._;()<>/+:A-Za-z0-9]+'))
    left join pmid_pub c on b.pmid=c.pmid
    left join author_info_all_affi d on c.orcid=d.author_id
    where b.doi  ~ '10\.\d+\/[-._;()<>/+:A-Za-z0-9]+'
    group by a.doi,d.first_name,d.last_name,c.pub_year,c.article_title
)

-- Combine the results from the above two CTEs
SELECT 
    p.doi,
    p.in_asctb_5th,
    p.in_cellmarker,
    p.in_cxg,
    pub_year,
    article_title,
    STRING_AGG(first_name || ' ' || last_name, ', ') AS authors   
FROM DOI_Presence_CTE p
LEFT JOIN Author_Aggregation a ON p.doi = a.doi
group by p.doi,p.in_asctb_5th,p.in_cellmarker,p.in_cxg,pub_year,article_title;

\o
