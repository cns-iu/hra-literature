-- funding data:

insert into hralit_funding (funding_id,acronym)
select grant_id, acronym
from pmid_grant_all
where pmid in (select pmid from hralit_publication where pmid is not null)
    and pmid is not null
    and grant_id is not null
group by grant_id, acronym;
