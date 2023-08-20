\copy (
  WITH CTE AS (
    SELECT 
        creator_info.author_id,
        full_name,
	first_name,
	last_name,
        version,
        creator_info.name,
        type,
	organ_name,
	asct_ontology.id as ontology,
	predict_info.predicted_gender as predicted_gender,
	predict_info.predicted_race as predicted_race,

    FROM creator_info
    left join asct_expert on creator_info.author_id = asct_expert.author_id
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
	ARRAY_AGG(DISTINCT '#Ontology/' || normalize_id(ontology)) FILTER (WHERE ontology IS NOT NULL) AS ontologies
    FROM CTE 
    GROUP BY author_id, identifier, full_name, first_name, last_name, predicted_gender,predicted_race
  )
  SELECT 
	jsonb_strip_nulls(ROW_TO_JSON(row)::jsonb) AS json_data
  FROM (
    SELECT 
        author_id AS "@id", 
        'Creator' AS "@type", 
        identifier AS identifier, 
        full_name AS name,
	first_name,
	last_name,
	predicted_gender,
	predicted_race,
	versions as "DOVersion",
	names as "DOName",
	types as "DOType",
	organ_names as "expertiseOrganLabel",
	ontologies as "expertiseInOrgan"
    FROM cleaned
) row
)TO creators_metadata.json
