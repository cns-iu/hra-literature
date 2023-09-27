\t on
\a
\pset fieldsep ','
\pset format csv
\pset tuples_only off
\o data/results/app0/com.csv

with cm as (
    select pmid,lower(doi)as doi from hralit_other_refs where source='cellmarker' and doi is not null
),
asct_b AS (
    SELECT lower(doi) AS doi 
    FROM hralit_asctb_publication
    WHERE doi is not null
),
cxg as (
    select pmid,lower(doi)as doi from hralit_other_refs where source='cxg' and doi is not null
),
DOI_CTE AS (
    -- Create a unified list of DOIs from all three tables
    SELECT doi FROM asct_b
    UNION
    SELECT doi FROM cm
    UNION
    SELECT doi FROM cxg
),
pd as (
    select pmid,lower(doi)as doi from hralit_publication where lower(doi) in (select doi from DOI_CTE)
),
subjects as (
    select pd.pmid,pd.doi,STRING_AGG(organ, ', ') AS organs from hralit_publication_subject
    join pd on hralit_publication_subject.pmid=pd.pmid
    group by pd.pmid,lower(pd.doi)
),

DOI_Presence_CTE AS (
    -- Check presence of DOIs in each table
    SELECT 
        d.doi,
        CASE WHEN a.doi IS NOT NULL THEN 1 ELSE 0 END AS in_asctb_5th,
        CASE WHEN b.doi IS NOT NULL THEN 1 ELSE 0 END AS in_cellmarker,
        CASE WHEN c.doi IS NOT NULL THEN 1 ELSE 0 END AS in_cxg,
        CASE WHEN subjects.doi IS NOT NULL THEN 1 ELSE 0 END AS in_31_organ_pubmed_pubs
    FROM DOI_CTE d
    LEFT JOIN asct_b a ON d.doi = a.doi
    LEFT JOIN cm b ON d.doi = b.doi
    LEFT JOIN cxg c ON d.doi = c.doi
    LEFT JOIN subjects ON subjects.doi = d.doi
),
Author_Aggregation as (
    select a.doi,d.first_name,d.last_name,c.pub_year,c.article_title
    from DOI_Presence_CTE a
    left join pmid_doi b on a.doi=lower(b.doi)
    left join pmid_pub c on b.pmid=c.pmid
    left join author_info_all_affi d on c.orcid=d.author_id
    where b.doi  is not null
    group by a.doi,d.first_name,d.last_name,c.pub_year,c.article_title
)

-- Combine the results from the above two CTEs
SELECT 
    p.doi,
    p.in_asctb_5th,
    p.in_cellmarker,
    p.in_cxg,
    p.in_31_organ_pubmed_pubs,
    organs,
    pub_year,
    article_title,
    subjects.organs,
    STRING_AGG(first_name || ' ' || last_name, ', ') AS authors   
FROM DOI_Presence_CTE p
left join pd on p.doi=pd.doi
LEFT JOIN subjects on pd.pmid=subjects.pmid
LEFT JOIN Author_Aggregation a ON p.doi = a.doi
group by p.doi,p.in_asctb_5th,p.in_cellmarker,p.in_cxg,p.in_31_organ_pubmed_pubs,organs,pub_year,article_title;

\o
