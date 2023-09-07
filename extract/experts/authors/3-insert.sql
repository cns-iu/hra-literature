-- Create the table
CREATE TABLE author_career_age (
    orcid VARCHAR,
    first_pubyear INTEGER,
    last_pubyear INTEGER,
    career_age_to_current INTEGER,
    career_age INTEGER
);

-- insert data
COPY author_career_age FROM data/expert/author_career_age.psv WITH DELIMITER '|' CSV HEADER ENCODING 'SQL-ASCII';
