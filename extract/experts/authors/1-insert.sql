CREATE TABLE author_info (
    uid VARCHAR,
    name_id INTEGER,
    first_name VARCHAR,
    last_name VARCHAR,
    full_name VARCHAR,
    email_addr VARCHAR,
    pubyear VARCHAR,
    country VARCHAR,
    city VARCHAR,
    state VARCHAR,
    organization VARCHAR,
    suborganization VARCHAR,
    zip VARCHAR
);


-- Import data into the table using the COPY command
COPY author_info FROM data/expert/author_info.psv WITH DELIMITER '|' CSV HEADER ENCODING 'SQL-ASCII';