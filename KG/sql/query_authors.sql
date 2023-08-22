\copy (
  WITH CTE AS (
    SELECT 
        author_info_lastest_affi.author_id,
        full_name,
	first_name,
	last_name,
        email_addr,
        country,
        city,
        state,
        zip,
        first_pubyear,
        last_pubyear,
        career_age_to_current,
      	asct_expert.name as label,
	asct_expert.level as label_type,
	asct_ontology.id as ontology,
	predict_info.predicted_gender as predicted_gender,
	predict_info.predicted_race as predicted_race,
	CASE 
    		WHEN organization IS NOT NULL AND suborganization IS NOT NULL 
    		THEN organization || '-' || suborganization 
    		WHEN organization IS NULL AND suborganization IS NULL
    		THEN NULL
    		ELSE COALESCE(organization, '') || COALESCE(suborganization, '')
	END AS institution_id
    FROM author_info_lastest_affi 
    left join asct_expert on author_info_lastest_affi.author_id = asct_expert.author_id
    left join asct_ontology on lower(asct_expert.name) = lower(asct_ontology.label)
    left join predict_info on author_info_lastest_affi.author_id = predict_info.author_id
	where author_info_lastest_affi.author_id is not null 
	and author_info_lastest_affi.author_id != ", , , , ," 
	and author_info_lastest_affi.author_id !=  "`"
  and author_info_lastest_affi.author_id !=  "0"
  ),
  cleaned AS (
    SELECT 
	'#Author/' || normalize_id(author_id) as author_id,
	author_id as identifier,
	full_name,
	first_name,
	last_name,
        email_addr,
	predicted_gender,
	predicted_race,
        career_age_to_current as career_age,
        ARRAY_AGG(DISTINCT country) FILTER (WHERE country IS NOT NULL) AS countries,
        ARRAY_AGG(DISTINCT city) FILTER (WHERE city IS NOT NULL) AS cities,
        ARRAY_AGG(DISTINCT state) FILTER (WHERE state IS NOT NULL) AS states,
        ARRAY_AGG(DISTINCT zip) FILTER (WHERE zip IS NOT NULL) AS zips,
        ARRAY_AGG(DISTINCT('#Institution/' || normalize_id(institution_id))) FILTER (WHERE institution_id IS NOT NULL) AS institution_ids,
	ARRAY_AGG(DISTINCT label) FILTER (WHERE label IS NOT NULL) AS labels, 
	ARRAY_AGG(DISTINCT label_type) FILTER (WHERE label_type IS NOT NULL) AS label_types, 
	ARRAY_AGG(DISTINCT '#Ontology/' || normalize_id(ontology)) FILTER (WHERE ontology IS NOT NULL) AS ontologies, 
    FROM CTE 
    GROUP BY author_id, identifier, full_name, first_name, last_name, email_addr, career_age_to_current,predicted_gender,predicted_race
  )
  SELECT 
	jsonb_strip_nulls(ROW_TO_JSON(row)::jsonb) AS json_data
  FROM (
    SELECT 
        author_id AS "@id", 
        'Author' AS "@type", 
        identifier AS identifier,
	'Author' AS "role", 
        full_name AS name,
	first_name,
	last_name,
        email_addr,
	predicted_gender,
	predicted_race,
	career_age,
	institution_ids,
	labels as "expertiseLabel",
	label_types as "expertiseLabelLevel",
	ontologies as "expertiseIn"
    FROM cleaned
) row
TO authors_metadata.json
