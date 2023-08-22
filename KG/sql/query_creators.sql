\copy (
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
	asct_ontology.id as ontology,
	predict_info.predicted_gender as predicted_gender,
	predict_info.predicted_race as predicted_race,
	author_info_lastest_affi.author_id as linked_author_id
    FROM creator_info
    left join author_info_lastest_affi on creator_info.author_id = author_info_lastest_affi.author_id
    left join asct_ontology on lower(creator_info.organ_name) = lower(asct_ontology.label)
    left join predict_info on creator_info.author_id = predict_info.author_id
	where creator_info.author_id is not null
  ),
  cleaned AS (
    SELECT 
        '#Creator/' || normalize_id(author_id) as author_id,
	author_id as identifier,
        full_name,
	first_name,
	last_name,
	predicted_gender,
	predicted_race,
        ARRAY_AGG(DISTINCT version) FILTER (WHERE version IS NOT NULL) AS versions,
        ARRAY_AGG(DISTINCT name) FILTER (WHERE name IS NOT NULL) AS names,
        ARRAY_AGG(DISTINCT type) FILTER (WHERE type IS NOT NULL) AS types,
        ARRAY_AGG(DISTINCT organ_name) FILTER (WHERE organ_name IS NOT NULL) AS organ_names,
	ARRAY_AGG(DISTINCT '#Ontology/' || normalize_id(ontology)) FILTER (WHERE ontology IS NOT NULL) AS ontologies,
	CASE
		WHEN linked_author_id IS NOT NULL THEN '#Author/' || normalize_id(linked_author_id)
		ELSE NULL
	END AS linked_author_id
    FROM CTE 
    GROUP BY author_id, identifier, full_name, first_name, last_name, predicted_gender,predicted_race,linked_author_id
  )
  SELECT 
	jsonb_strip_nulls(ROW_TO_JSON(row)::jsonb) AS json_data
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
	versions as "DOVersion",
	names as "DOName",
	types as "DOType",
	organ_names as "expertiseOrganLabel",
	ontologies as "expertiseInOrgan",
	linked_author_id as "linkedToAuthor"
    FROM cleaned
) row
)TO creators_metadata.json
