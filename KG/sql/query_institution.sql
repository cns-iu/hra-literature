WITH 
-- Create temporary table named CTE
CTE AS (
    SELECT 
        country, 
        city, 
        state, 
        zip, 
        CASE 
            WHEN organization IS NOT NULL AND suborganization IS NOT NULL THEN 
                organization || '-' || suborganization
            ELSE 
                COALESCE(organization, '') || COALESCE(suborganization, '')
        END AS institution_id,
        
        CASE 
            WHEN organization IS NOT NULL AND suborganization IS NOT NULL THEN 
                organization || ', ' || suborganization
            ELSE 
                COALESCE(organization, '') || COALESCE(suborganization, '')
        END AS institution_name
    FROM author_info_lastest_affi
),

-- Filter out null values and group data
cleaned AS (
    SELECT 
        '#Institution/' || normalize_id(institution_id) as institution_id,
        CASE 
            WHEN institution_name <>'' THEN lower(institution_name)
            ELSE NULL 
        END AS institution_name,
        ARRAY_AGG(DISTINCT country) FILTER (WHERE country IS NOT NULL) AS countries,
        ARRAY_AGG(DISTINCT city) FILTER (WHERE city IS NOT NULL) AS cities,
        ARRAY_AGG(DISTINCT state) FILTER (WHERE state IS NOT NULL) AS states,
        ARRAY_AGG(DISTINCT zip) FILTER (WHERE zip IS NOT NULL) AS zips
    FROM CTE
    WHERE institution_id IS NOT NULL 
        AND institution_name IS NOT NULL 
        AND institution_name !=''
    GROUP BY institution_id, institution_name
)

-- Convert data to JSON and export
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
TO institutions_metadata.json;
