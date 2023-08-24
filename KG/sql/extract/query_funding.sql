\t
\a
\o fundings_metadata.json
WITH CTE AS (
  SELECT
    grant_id,
    acronym,
    agency
  FROM
    pmid_grant_all
  WHERE
    grant_id IS NOT NULL
  -- UNION
  -- SELECT
  --   grant_id,
  --   NULL AS acronym,
  --   agency
  -- FROM
  --   uid_grant_all
  -- WHERE
  --   grant_id IS NOT NULL
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
    '#Funding/' || normalize_id(grant_id) AS grant_id,
  ARRAY_AGG(DISTINCT grant_id) FILTER (WHERE grant_id IS NOT NULL) AS identifier,
  ARRAY_AGG(DISTINCT acronym) FILTER (WHERE acronym IS NOT NULL) AS acronym,
  ARRAY_AGG(DISTINCT '#Funder/' || normalize_id(agency)) FILTER (WHERE agency IS NOT NULL) AS agencies
FROM
  CTE
GROUP BY
  grant_id
)
SELECT
  jsonb_strip_nulls(ROW_TO_JSON(ROW)::jsonb) AS json_data
FROM (
  SELECT
    grant_id AS "@id",
    'Funding' AS "@type",
    identifier,
    'Funding' AS "role",
    agencies AS "hasFunder"
  FROM
    cleaned
  WHERE
    grant_id != '#Funding/-'
    AND grant_id != '#Funding/')
  ROW
