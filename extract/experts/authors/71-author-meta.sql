create table cleaned_author_info (
    orcid varchar,
    first_name varchar,
    last_name varchar,
    first_pubyear varchar,
    career_age varchar,
    country_code varchar,
    ror varchar,
    soa_institution_id varchar,
    institution_name varchar,
    institution_type varchar
);

with CTE as (
    SELECT 'https://orcid.org/' || substring(author_id from '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]')AS orcid,
            COALESCE(MAX(first_name), '') AS first_name,
            COALESCE(MAX(last_name), '') AS last_name,
            min(first_pubyear) as first_pubyear,
            max(career_age_to_current) as career_age
    FROM author_info_all_affi
    WHERE substring(author_id from '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]') IS NOT NULL
    GROUP BY orcid
), 
CTE3 AS (
    SELECT t1.orcid,t2.first_name,t3.last_name,t4.first_pubyear,t5.career_age
    FROM (SELECT DISTINCT(orcid) FROM CTE) as t1
    left join (SELECT orcid,first_name FROM CTE WHERE first_name !='') as t2
    on t1.orcid=t2.orcid
    left join (SELECT orcid,last_name FROM CTE WHERE last_name !='') as t3
    on t1.orcid=t3.orcid
    left join (SELECT orcid,first_pubyear FROM CTE WHERE first_pubyear is not null) as t4
    on t1.orcid=t4.orcid
    left join (SELECT orcid,career_age FROM CTE WHERE career_age is not null) as t5  
    on t1.orcid=t5.orcid
)
insert into cleaned_author_info_2 (
    orcid,first_name,last_name,first_pubyear,career_age,country_code,
    ror,soa_institution_id,institution_name,institution_type
)
SELECT t1.orcid,first_name,last_name,first_pubyear,career_age,country_code,
    ror,soa_institution_id,institution_name,institution_type 
FROM CTE3 t1
left join soa_institution t2
on t1.orcid=t2.orcid
GROUP BY t1.orcid,first_name,last_name,first_pubyear,career_age,country_code,
         ror,soa_institution_id,institution_name,institution_type;