\t
\a
\o funders_metadata.json
WITH CTE AS (
  SELECT
    agency,
    country
  FROM
    pmid_grant_all
  WHERE
    pmid_grant_all.agency IS NOT NULL AND
    pmid IS NOT NULL
  -- UNION
  -- SELECT
  --   agency,
  --   NULL AS countries
  -- FROM
  --   uid_grant_all
  -- WHERE
  --   agency IS NOT NULL
  --   AND uid IN (
  --     SELECT
  --       uid
  --     FROM
  --       wosid_to_pmid
  --     WHERE
  --       pmid IS NULL)
),
cleaned AS (
  SELECT
    '#Funder/' || normalize_id(agency) AS agency_id,
  ARRAY_AGG(DISTINCT agency) FILTER (WHERE agency IS NOT NULL) AS agencies,
  ARRAY_AGG(DISTINCT country) FILTER (WHERE country IS NOT NULL) AS countries
FROM
  CTE
GROUP BY
  agency_id
)
SELECT
  jsonb_strip_nulls(ROW_TO_JSON(ROW)::jsonb) AS json_data
FROM (
  SELECT
    agency_id AS "@id",
    'Funder' AS "@type",
    agencies AS identifier,
    'Funder' AS "role",
    countries
  FROM
    cleaned)
  ROW
