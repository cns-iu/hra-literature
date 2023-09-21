create table author_h_index(
    orcid varchar,
    h_index int8
);

insert into author_h_index (orcid,h_index)
with clean as (
    select pmid,'https://orcid.org/' || substring(identifier from '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]') AS identifier
    from pmid_author
),
AuthorCitations AS (
    SELECT 
        A.identifier AS orcid,
        B.cit_ct
    FROM 
        clean A
    JOIN 
        uid_cit_count B ON A.pmid = B.pmid
    ORDER BY 
        A.identifier, 
        B.cit_ct DESC
)

, RankedCitations AS (
    SELECT 
        orcid,
        cit_ct,
        ROW_NUMBER() OVER(PARTITION BY orcid ORDER BY cit_ct DESC) AS rnk
    FROM 
        AuthorCitations
)

SELECT 
    orcid,
    MAX(rnk) AS h_index
FROM 
    RankedCitations
WHERE 
    rnk <= cit_ct
GROUP BY 
    orcid;