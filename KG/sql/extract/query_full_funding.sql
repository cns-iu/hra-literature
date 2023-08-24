\t
\a
\o full_fundings_metadata.json
WITH CTE AS (
  SELECT
    grant_id,
    acronym,
    agency,
    country,
    pmid
  FROM
    medline_grant
  WHERE
    medline_grant.grant_id IS NOT NULL AND
    pmid IS NOT NULL
),
cleaned AS (
  SELECT
    '#Funding/' || normalize_id(grant_id) AS grant_id,
    ARRAY_AGG(DISTINCT grant_id) FILTER (WHERE grant_id IS NOT NULL) AS identifiers,
    ARRAY_AGG(DISTINCT acronym) FILTER (WHERE acronym IS NOT NULL) AS acronyms,
    ARRAY_AGG(DISTINCT agency) FILTER (WHERE agency IS NOT NULL) AS agencies,
    ARRAY_AGG(DISTINCT country) FILTER (WHERE country IS NOT NULL) AS countries,
    ARRAY_AGG(DISTINCT 'https://pubmed.ncbi.nlm.nih.gov/'|| normalize_id(pmid)) AS publications
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
    identifiers AS identifier,
    'Funding' AS "role",
    agencies,
    countries,
    publications
  FROM
    cleaned)
  ROW;
