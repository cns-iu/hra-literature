\t on
\a
\pset fieldsep ','
\pset format csv
\pset tuples_only off
\o data/results/app4/author-geo-ct.csv

-- with cte as (select a.orcid,b.country_code
-- from hralit_author_institution a
-- join hralit_institution b 
--     on a.soa_institution_id=b.soa_institution_id
-- group by a.orcid,b.country_code)
-- select country_code,count(*) from cte
-- group by country_code order by country_code;
WITH cte AS (
    SELECT a.orcid, 
           CASE 
               WHEN b.country_code = 'TW' THEN 'CN' 
               ELSE b.country_code 
           END AS country_code
    FROM hralit_author_institution a
    JOIN hralit_institution b 
        ON a.soa_institution_id = b.soa_institution_id
    GROUP BY a.orcid, b.country_code
)

SELECT country_code, COUNT(*) 
FROM cte
WHERE country_code != 'TW'  -- Exclude TW from the final result
GROUP BY country_code 
ORDER BY country_code;

\o
