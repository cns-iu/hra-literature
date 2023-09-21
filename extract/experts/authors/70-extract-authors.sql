insert into hralit_author_expertise(orcid,organ)
with a as (select     
    'https://orcid.org/' || substring(A.identifier from '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]') AS orcid,
    B.organ
FROM 
    pmid_author A
JOIN 
    pmid_31_organs B ON A.pmid = B.pmid 
where  substring(A.identifier from '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]') IS NOT NULL
GROUP BY orcid , b.organ)
select orcid,organ from a group by orcid,organ;

