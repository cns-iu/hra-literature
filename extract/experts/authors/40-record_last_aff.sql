\t on
\a
\pset fieldsep '|'
\pset format csv
\o data/expert/author_info_lastest_affi.psv

WITH 
CTE1 AS (
    SELECT 
        c.identifier AS author_id,
        first_name,
        last_name,
        full_name,
        email_addr,
        country,
        city,
        state,
        pubyear,
        organization,
        suborganization,
        zip
    FROM 
        author_info a 
    JOIN 
        wosid_to_pmid b ON a.uid = b.uid 
    JOIN 
        pmid_author c ON b.pmid = c.pmid AND a.name_id = c.author_ctr
),
tmp AS (
    SELECT 
        author_id,
        first_name,
        last_name,
        full_name,
        email_addr,
        country,
        city,
        state,
        pubyear,
        organization,
        suborganization,
        zip
    FROM 
        CTE1 
    GROUP BY 
        author_id, first_name, last_name, full_name, email_addr, country, city, state, organization, suborganization, zip, pubyear
),
cte AS (
    SELECT 
        author_id,
        first_name,
        last_name,
        full_name,
        pubyear,
        email_addr,
        country,
        city,
        state,
        organization,
        suborganization,
        zip,
        ROW_NUMBER() OVER (PARTITION BY author_id ORDER BY pubyear DESC) AS rn
    FROM 
        tmp
),

CTE2 AS (
    SELECT 
        author_id,
        first_name,
        last_name,
        full_name,
        email_addr,
        country,
        city,
        state,
        organization,
        suborganization,
        zip
    FROM 
        cte 
    WHERE 
        rn = 1
),

CTE3 AS (
    SELECT DISTINCT(identifier) AS author_id 
    FROM pmid_author
),

CTE4 AS (
    SELECT 
        CTE3.author_id,
        first_name,
        last_name,
        full_name,
        email_addr,
        country,
        city,
        state,
        organization,
        suborganization,
        zip,
        first_pubyear,
        last_pubyear,
        career_age_to_current,
        career_age
    FROM 
        CTE3 
    LEFT JOIN 
        CTE2 ON CTE3.author_id = CTE2.author_id 
    LEFT JOIN 
        author_career_age d ON CTE3.author_id = d.orcid
)

SELECT 
    author_id,
    first_name,
    last_name,
    full_name,
    email_addr,
    country,
    city,
    state,
    organization,
    suborganization,
    zip,
    first_pubyear,
    last_pubyear,
    career_age_to_current,
    career_age
FROM 
    CTE4 
GROUP BY 
    author_id, first_name, last_name, full_name, email_addr, country, city, state, organization, suborganization, zip, first_pubyear, last_pubyear, career_age_to_current, career_age;

\o
