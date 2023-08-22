\copy (
  WITH CTE AS (
    SELECT 
        'PMID/' || pub_34_organns.pmid AS identifier_id,
        pub_34_organns.uid,
        doi,
        pubyear,
        article_title,
        journal_title,
        identifier AS author_id,
        grant_id,
        organ,
	asct_ontology.id as ontology
    FROM pub_34_organns 
    LEFT JOIN pmid_author ON pub_34_organns.pmid = pmid_author.pmid 
    LEFT JOIN pmid_grant_all ON pub_34_organns.pmid = pmid_grant_all.pmid 
    LEFT JOIN pmid_34_organs ON pub_34_organns.pmid = pmid_34_organs.pmid 
    LEFT JOIN asct_ontology on lower(pmid_34_organs.organ) = lower(asct_ontology.label)
    
    UNION 
    
    SELECT 
        'WOSID/' || pub_34_organns.uid  AS identifier_id,
        pub_34_organns.uid,
        doi,
        pubyear,
        article_title,
        journal_title,
        identifier AS author_id,
        grant_id,
        organ,
	asct_ontology.id as ontology
    FROM pub_34_organns 
    LEFT JOIN pmid_author ON pub_34_organns.pmid = pmid_author.pmid 
    LEFT JOIN uid_grant_all ON pub_34_organns.uid = uid_grant_all.uid 
    LEFT JOIN uid_34_organs ON pub_34_organns.pmid = uid_34_organs.pmid 
    LEFT JOIN asct_ontology on lower(uid_34_organs.organ) = lower(asct_ontology.label)
    WHERE pub_34_organns.pmid IS NULL
), 

CLEANED AS (
    SELECT 
        'Publication/' || normalize_id(identifier_id) as pub_id,
        ARRAY_AGG(DISTINCT uid) FILTER (WHERE uid IS NOT NULL) AS uids,
        ARRAY_AGG(DISTINCT doi) FILTER (WHERE doi IS NOT NULL) AS dois,
        ARRAY_AGG(DISTINCT pubyear) FILTER (WHERE pubyear IS NOT NULL) AS pubyears,
        ARRAY_AGG(DISTINCT article_title) FILTER (WHERE article_title IS NOT NULL) AS article_titles,
        ARRAY_AGG(DISTINCT journal_title) FILTER (WHERE journal_title IS NOT NULL) AS journal_titles,
        ARRAY_AGG(DISTINCT '#Author/' || normalize_id(author_id)) FILTER (WHERE author_id IS NOT NULL) AS author_ids,
        ARRAY_AGG(DISTINCT '#Funding/' || normalize_id(grant_id)) FILTER (WHERE grant_id IS NOT NULL) AS grant_ids,
        ARRAY_AGG(DISTINCT organ) FILTER (WHERE organ IS NOT NULL) AS organs,
	ARRAY_AGG(DISTINCT '#Ontology/' || normalize_id(ontology)) FILTER (WHERE ontology IS NOT NULL) AS ontologies
    FROM CTE 
    GROUP BY pub_id
)

-- Final Selection
SELECT jsonb_strip_nulls(ROW_TO_JSON(row)::jsonb) AS json_data
FROM (
    SELECT 
        pub_id AS "@id",
        'Publication' AS "@type", 
        dois AS identifier, 
	'Publication' AS "role", 
        article_titles AS name,
	journal_titles AS "journalName",
        uids AS "WOSID",
        pubyears AS "publicationYear",
        author_ids AS "hasAuthor",
        grant_ids AS "hasFunding", 
	organs AS "organLabel",
        ontologies AS "hasOrgan"
    FROM CLEANED
  ) row 
)TO publication_metadata.json
