\copy (
  WITH CTE AS (
    SELECT 
	grant_id,
        acronym,
	agency
    FROM pmid_grant_all
	where grant_id is not null
    UNION
    SELECT
	grant_id,
	NULL AS acronym,
	agency
    FROM uid_grant_all
	WHERE grant_id is not null
	AND uid in (select uid from wosid_to_pmid where pmid is null)
  ),
  cleaned AS (
    SELECT 
        '#Funding/' || normalize_id(grant_id) as grant_ids,
	ARRAY_AGG(DISTINCT grant_id ) FILTER (WHERE grant_id IS NOT NULL) as identifier,
	ARRAY_AGG(DISTINCT acronym) FILTER (WHERE acronym IS NOT NULL) AS acronym,
        ARRAY_AGG(DISTINCT '#Funder/' || normalize_id(agency)) FILTER (WHERE agency IS NOT NULL) AS agencies
    FROM CTE
    GROUP BY grant_ids
  )
  SELECT 
	jsonb_strip_nulls(ROW_TO_JSON(row)::jsonb) AS json_data
  FROM (
    SELECT 
        grant_ids AS "@id", 
        'Funding' AS "@type", 
        identifier,
	agencies AS "hasFunder"
    FROM cleaned
    Where grant_id != '#Funding/-' and grant_id != '#Funding/'
) row
)TO fundings_metadata.json
