\t
\a
\o creators_metadata.json
WITH CTE AS (
  SELECT
    creator_info.author_id,
    creator_info.full_name,
    creator_info.first_name,
    creator_info.last_name,
    version,
    creator_info.name,
    type,
    organ_name,
    asct_ontology.id AS ontology,
    predict_info.predicted_gender AS predicted_gender,
    predict_info.predicted_race AS predicted_race,
    author_info_lastest_affi.author_id AS linked_author_id
  FROM
    creator_info
    LEFT JOIN author_info_lastest_affi ON creator_info.author_id = author_info_lastest_affi.author_id
    LEFT JOIN asct_ontology ON lower(creator_info.organ_name) = lower(asct_ontology.label)
    LEFT JOIN predict_info ON creator_info.author_id = predict_info.author_id
  WHERE
    creator_info.author_id IS NOT NULL
),
cleaned AS (
  SELECT
    '#https://orcid.org/' || author_id AS author_id,
    author_id AS identifier,
    full_name,
    first_name,
    last_name,
    predicted_gender,
    predicted_race,
    ARRAY_AGG(DISTINCT version) FILTER (WHERE version IS NOT NULL) AS do_versions,
    ARRAY_AGG(DISTINCT name) FILTER (WHERE name IS NOT NULL) AS do_names,
    ARRAY_AGG(DISTINCT type) FILTER (WHERE type IS NOT NULL) AS do_types,
    ARRAY_AGG(DISTINCT organ_name) FILTER (WHERE organ_name IS NOT NULL) AS organ_names,
    ARRAY_AGG(DISTINCT 'http://purl.obolibrary.org/obo/' || REPLACE(ontology, ':', '_')) FILTER (WHERE ontology IS NOT NULL) AS ontologies
FROM
  CTE
GROUP BY
  author_id,
  identifier,
  full_name,
  first_name,
  last_name,
  predicted_gender,
  predicted_race
)
SELECT
  jsonb_strip_nulls(ROW_TO_JSON(ROW)::jsonb) AS json_data
FROM (
  SELECT
    author_id AS "@id",
    'Creator' AS "@type",
    identifier AS identifier,
    'Creator' AS "role",
    full_name AS name,
    first_name,
    last_name,
    predicted_gender,
    predicted_race,
    do_versions AS "DOVersion",
    do_names AS "DOName",
    do_types AS "DOType",
    organ_names AS "expertiseLabel",
    ontologies AS "expertiseInOrgan"
  FROM
    cleaned)
  ROW
