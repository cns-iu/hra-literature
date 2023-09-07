-- Create the table
CREATE TABLE author_info_lastest_affi (
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

-- import data
COPY author_info FROM data/expert/author_info_lastest_affi.psv WITH DELIMITER '|' CSV HEADER ENCODING 'SQL-ASCII';
