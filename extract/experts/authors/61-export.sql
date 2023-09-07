-- Set up the environment for command output
\t on
\a
\pset fieldsep ','
\pset format csv
\o data/expert/asct_author_info_all_affi.csv

-- Execute the select command and direct the output to the specified file
SELECT 
    name,
    level,
    a.author_id,
    citation,
    fund_ct,
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
    asct_expert a 
LEFT JOIN 
    author_info_all_affi b ON a.author_id = b.author_id;

-- Reset the output settings
\o
