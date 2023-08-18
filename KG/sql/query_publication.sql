\copy (
  WITH tmp AS (
    SELECT 
        pub_34_organns.pmid,
        pub_34_organns.uid,
        normalize_id(doi) AS doi,
        pubyear,
        normalize_id(article_title) AS article_title,
        normalize_id(journal_title) AS journal_title,
        normalize_id(identifier) AS author_id,
        normalize_id(grant_id) AS grant_id,
        normalize_id(organ) AS organ
    FROM pub_34_organns 
    LEFT JOIN pmid_author ON pub_34_organns.pmid = pmid_author.pmid 
    LEFT JOIN pmid_grant_all ON pub_34_organns.pmid = pmid_grant_all.pmid 
    LEFT JOIN pmid_34_organs ON pub_34_organns.pmid = pmid_34_organs.pmid 
    
    UNION 
    
    SELECT 
        pub_34_organns.pmid,
        pub_34_organns.uid,
        normalize_id(doi) AS doi,
        pubyear,
        normalize_id(article_title) AS article_title,
        normalize_id(journal_title) AS journal_title,
        normalize_id(identifier) AS author_id,
        normalize_id(grant_id) AS grant_id,
        normalize_id(organ) AS organ
    FROM pub_34_organns 
    LEFT JOIN pmid_author ON pub_34_organns.pmid = pmid_author.pmid 
    LEFT JOIN uid_grant_all ON pub_34_organns.uid = uid_grant_all.uid 
    LEFT JOIN uid_34_organs ON pub_34_organns.pmid = uid_34_organs.pmid 
    WHERE pub_34_organns.pmid IS NULL
), 

CTE AS (
    SELECT 
        pmid,
        uid,
        doi,
        pubyear,
        article_title,
        journal_title,
        ARRAY_AGG(DISTINCT author_id) AS author_ids,
        ARRAY_AGG(DISTINCT grant_id) AS grant_ids,
        ARRAY_AGG(DISTINCT organ) AS organs 
    FROM tmp 
    GROUP BY pmid, uid, doi, pubyear, article_title, journal_title
)

-- Final Selection
SELECT ROW_TO_JSON(row) AS json_data 
FROM (
    SELECT 
        pmid,
        uid,
        doi,
        pubyear,
        article_title,
        journal_title,
        author_ids,
        grant_ids,
        organs 
    FROM CTE
  ) row 
)TO '/N/slate/yokong/publication_metadata.json
