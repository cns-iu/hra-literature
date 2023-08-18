\copy(
  
  WITH tmp AS (
    SELECT 
        normalize_id(grant_id) AS grant_id,
        normalize_id(agency) AS funder_id
    FROM pmid_grant_all
  ),
  CTE AS (
    SELECT 
        grant_id,
        ARRAY_AGG(DISTINCT(funder_id)) AS funder_ids
    FROM tmp 
    GROUP BY grant_id
  )

  SELECT ROW_TO_JSON(row) AS json_data FROM (
    SELECT 
        grant_id,
        funder_ids
    FROM CTE
  ) row 

TO '/N/slate/yokong/fundings_metadata.json'
