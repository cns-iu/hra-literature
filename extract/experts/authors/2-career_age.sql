\t on
\a
\pset fieldsep '|'
\pset format csv
\o data/expert/author_career_age.psv

WITH aa AS (
    SELECT 
        a.identifier, 
        article_year::INTEGER AS pubyear 
    FROM 
        medline_author_identifier a 
    LEFT JOIN 
        medline_article_date b ON a.pmid = b.pmid
)

SELECT 
    identifier, 
    MIN(pubyear) AS first_pubyear, 
    MAX(pubyear) AS last_pubyear, 
    2024 - MIN(pubyear) AS career_age_to_current, 
    MAX(pubyear) - MIN(pubyear) AS career_age 
FROM 
    aa 
GROUP BY 
    identifier;

\o
