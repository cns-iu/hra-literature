\t on
\a
\pset fieldsep '|'
\pset format csv
\o data/expert/author_info_all_affi.psv

WITH 
aa AS (
    SELECT 
        c.identifier AS author_id,
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
        author_info a 
    JOIN 
        wosid_to_pmid b ON a.uid = b.uid 
    JOIN 
        pmid_author c ON b.pmid = c.pmid AND a.name_id = c.author_ctr
),

bb AS (
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
        aa 
    GROUP BY 
        author_id, first_name, last_name, full_name, email_addr, country, city, state, organization, suborganization, zip
),

cc AS (
    SELECT DISTINCT(identifier) AS author_id 
    FROM pmid_author
),

dd AS (
    SELECT 
        cc.author_id,
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
        cc 
    LEFT JOIN 
        bb ON cc.author_id = bb.author_id 
    LEFT JOIN 
        author_career_age d ON cc.author_id = d.orcid
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
    dd 
GROUP BY 
    author_id, first_name, last_name, full_name, email_addr, country, city, state, organization, suborganization, zip, first_pubyear, last_pubyear, career_age_to_current, career_age;

\o
