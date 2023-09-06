SELECT m.identifier, 
       o.organ, 
       COUNT(m.pmid) AS ct 
FROM medline_author_affiliation_identifier AS m 
JOIN Pmid_34_organs AS o ON m.pmid = o.pmid 
GROUP BY m.identifier, o.organ
