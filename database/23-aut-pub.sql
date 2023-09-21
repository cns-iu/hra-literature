insert into hralit_publication_author (pmid, orcid)
select 
    pmid, 
    'https://orcid.org/' || substring(identifier from '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]')AS orcid
from pmid_author
where pmid in (select pmid from hralit_publication where pmid is not null)
    and pmid is not null
    and substring(identifier from '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]') is not NULL
group by pmid,orcid;