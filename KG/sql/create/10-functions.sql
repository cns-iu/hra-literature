CREATE OR REPLACE FUNCTION normalize_id(str text) RETURNS text
	AS $$ SELECT '#' || regexp_replace(regexp_replace(lower(str), '\W+', '-', 'g'), '[^a-z0-9-]+', '', 'g'); $$
	LANGUAGE SQL
    IMMUTABLE
    RETURNS NULL ON NULL INPUT;

CREATE OR REPLACE FUNCTION normalize_author_id(str text) RETURNS text
	AS $$
		SELECT CASE WHEN trim(str) ~ '^(\d{4}-){3}\d{3}(\d|X)$'
		THEN 'https://orcid.org/' || trim(str)
		ELSE '#Author/' || normalize_id(str) END; $$
	LANGUAGE SQL
    IMMUTABLE
    RETURNS NULL ON NULL INPUT;
