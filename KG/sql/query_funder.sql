\copy (
  WITH CTE AS (
    SELECT 
        '#Funder' || normalize_id(pmid_grant_all.agency) as agency_id,
	ARRAY_AGG(DISTINCT agency) FILTER (WHERE agency IS NOT NULL) AS agencies,
        ARRAY_AGG(DISTINCT country) FILTER (WHERE country IS NOT NULL) AS countries
    FROM pmid_grant_all
	where pmid_grant_all.agency is not null
	GROUP BY agency_id
  )
  SELECT 
	jsonb_strip_nulls(ROW_TO_JSON(row)::jsonb) AS json_data
  FROM (
    SELECT 
        agency_id AS "@id", 
        'Funder' AS "@type", 
        agencies AS identifier
    FROM CTE
) row
)TO funders_metadata.json
