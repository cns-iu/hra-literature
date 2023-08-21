\copy (
  WITH CTE AS (
    SELECT 
	agency,
        country
    FROM pmid_grant_all
	where pmid_grant_all.agency is not null
    UNION
    SELECT
	agency,
	NULL
    FROM pmid_grant_all
	WHERE agency is not null
	AND uid in (select uid from wosid_to_pmid where pmid is null)
  ),
  cleaned AS (
    SELECT 
        '#Funder' || normalize_id(agency) as agency_id,
	ARRAY_AGG(DISTINCT agency) FILTER (WHERE agency IS NOT NULL) AS agencies,
        ARRAY_AGG(DISTINCT country) FILTER (WHERE country IS NOT NULL) AS countries
    FROM CTE
    GROUP BY agency_id
  )
  SELECT 
	jsonb_strip_nulls(ROW_TO_JSON(row)::jsonb) AS json_data
  FROM (
    SELECT 
        agency_id AS "@id", 
        'Funder' AS "@type", 
        agencies AS identifier
    FROM cleaned
) row
)TO funders_metadata.json
