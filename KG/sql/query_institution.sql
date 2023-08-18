\COPY (
    WITH tmp AS (
        SELECT
            city,
            state,
            zip,
            CASE 
                WHEN organization IS NOT NULL AND suborganization IS NOT NULL THEN 
                    normalize_id(organization || '-' || suborganization)
                ELSE 
                    normalize_id(COALESCE(organization, '') || COALESCE(suborganization, ''))
            END AS institution_id,
            CASE 
                WHEN organization IS NOT NULL AND suborganization IS NOT NULL THEN 
                    organization || ', ' || suborganization
                ELSE 
                    COALESCE(organization, '') || COALESCE(suborganization, '')
            END AS institution_name 
        FROM author_info_lastest_affi
    ),
    CTE AS (
        SELECT
            institution_id,
            CASE 
                WHEN institution_name <> '' THEN lower(institution_name)
                ELSE NULL
            END AS institution_name,
            ARRAY_AGG(DISTINCT(country)) AS countries,
            ARRAY_AGG(DISTINCT(city)) AS cities,
            ARRAY_AGG(DISTINCT(state)) AS states,
            ARRAY_AGG(DISTINCT(zip)) AS zips
        FROM tmp
        WHERE institution_id IS NOT NULL AND institution_name IS NOT NULL AND institution_name != ''
        GROUP BY institution_id, institution_name
    ),
    expanded AS (
        SELECT
            institution_id,
            institution_name,
            jsonb_array_elements_text(array_to_json(countries)::jsonb) AS country,
            jsonb_array_elements_text(array_to_json(cities)::jsonb) AS city,
            jsonb_array_elements_text(array_to_json(states)::jsonb) AS state,
            jsonb_array_elements_text(array_to_json(zips)::jsonb) AS zip
        FROM CTE
    ),
    cleaned AS (
        SELECT
            institution_id,
            institution_name,
            jsonb_agg(country) FILTER (WHERE country IS NOT NULL) AS countries,
            jsonb_agg(city) FILTER (WHERE city IS NOT NULL) AS cities,
            jsonb_agg(state) FILTER (WHERE state IS NOT NULL) AS states,
            jsonb_agg(zip) FILTER (WHERE zip IS NOT NULL) AS zips
        FROM expanded
        GROUP BY institution_id, institution_name
    )
    SELECT 
        jsonb_strip_nulls(ROW_TO_JSON(row)::jsonb) AS json_data
    FROM (
        SELECT 
            institution_id AS "@id",
            'Institution' AS "@type",
            institution_name AS identifier,
            institution_name AS name,
            countries,
            cities,
            states,
            zips
        FROM cleaned
    ) row
) TO institutions_metadata.json
