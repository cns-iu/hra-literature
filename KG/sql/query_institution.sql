\copy (
  WITH tmp AS (
    SELECT 
        country,
        city,
        state,
        zip,
        CASE 
            WHEN organization IS NOT NULL AND suborganization IS NOT NULL 
            THEN normalize_id(organization || '-' || suborganization) 
            ELSE normalize_id(COALESCE(organization, '') || COALESCE(suborganization, ''))
        END AS institution_id,
        CASE 
            WHEN organization IS NOT NULL AND suborganization IS NOT NULL 
            THEN organization || ', ' || suborganization 
            ELSE COALESCE(organization, '') || COALESCE(suborganization, '')
        END AS institution_name 
    FROM author_info_lastest_affi
  ),
  CTE AS (
    SELECT 
        institution_id, 
        LOWER(institution_name) AS institution_name,
        ARRAY_AGG(DISTINCT(country)) AS countries,
        ARRAY_AGG(DISTINCT(city)) AS cities,
        ARRAY_AGG(DISTINCT(state)) AS states,
        ARRAY_AGG(DISTINCT(zip)) AS zips 
    FROM tmp 
    WHERE institution_id IS NOT NULL AND institution_name IS NOT NULL 
    GROUP BY institution_id, institution_name
  )
  SELECT ROW_TO_JSON(row) AS json_data FROM (
    SELECT 
        institution_id,
        institution_name,
        countries,
        cities,
        states,
        zips 
    FROM CTE
  ) row
to /N/slate/yokong/institutions_metadata.json


