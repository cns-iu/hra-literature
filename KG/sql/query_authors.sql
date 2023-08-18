\copy (
  WITH tmp AS (
    SELECT 
        normalize_id(author_id) AS author_id,
        full_name,
        email_addr,
        country,
        city,
        state,
        zip,
        first_pubyear,
        last_pubyear,
        career_age_to_current,
        career_age,
        CASE 
            WHEN organization IS NOT NULL AND suborganization IS NOT NULL 
            THEN normalize_id(organization || '-' || suborganization) 
            ELSE normalize_id(COALESCE(organization, '') || COALESCE(suborganization, ''))
        END AS institution_id 
    FROM author_info_lastest_affi
  ),
  CTE AS (
    SELECT 
        author_id,
        full_name,
        email_addr,
        ARRAY_AGG(DISTINCT(country)) AS countries,
        ARRAY_AGG(DISTINCT(city)) AS cities,
        ARRAY_AGG(DISTINCT(state)) AS states,
        ARRAY_AGG(DISTINCT(zip)) AS zips,
        career_age_to_current,
        ARRAY_AGG(DISTINCT(institution_id)) AS institution_ids 
    FROM tmp 
    GROUP BY author_id, full_name, email_addr, career_age_to_current
  )
  SELECT ROW_TO_JSON(row) AS json_data FROM (
    SELECT 
        author_id,
        full_name,
        email_addr,
        career_age_to_current,
        countries,
        cities,
        states,
        zips,
        institution_ids 
    FROM CTE
  ) row
to /N/slate/yokong/authors_metadata.json


