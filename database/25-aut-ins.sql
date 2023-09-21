insert into hralit_author_institution
select orcid, soa_institution_id
from soa_institution
where orcid in (select orcid from hralit_author)
group by orcid, soa_institution_id;