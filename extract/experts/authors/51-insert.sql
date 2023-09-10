-- Create the table
CREATE TABLE author_info_all_affi (
    author_id VARCHAR,
    first_name VARCHAR,
    last_name VARCHAR,
    full_name VARCHAR,
    email_addr VARCHAR,
    country VARCHAR,
    city VARCHAR,
    state VARCHAR,
    organization VARCHAR,
    suborganization VARCHAR,
    zip VARCHAR,
    first_pubyear INTEGER,
    last_pubyear INTEGER,
    career_age_to_current INTEGER,
    career_age INTEGER
);

-- Import data into the table
COPY author_info_all_affi 
FROM data/expert/author_info_all_affi.psv
WITH DELIMITER '|' CSV HEADER ENCODING 'SQL-ASCII';