\t on
\a
\pset fieldsep ','
\pset format csv
\pset tuples_only off
\o data/results/app1/pub-trend.csv

with a as (
    select pubyear,count(distinct(pmid)) as pubmed_pubs
    from hralit_publication 
    where pubyear is not null and pmid is not null 
    group by pubyear
),
b as (
    select pubyear,count(distinct(hralit_other_refs.pmid)) as cxg_pubs
    from hralit_other_refs
    join hralit_publication on hralit_other_refs.pmid=hralit_publication.pmid
    where hralit_publication.pubyear is not null and hralit_publication.pmid is not null and source='cxg'
    group by pubyear
),
c as (
    select pubyear,count(distinct(hralit_other_refs.pmid)) as cellmarker_pubs
    from hralit_other_refs
    join hralit_publication on hralit_other_refs.pmid=hralit_publication.pmid
    where hralit_publication.pubyear is not null and hralit_publication.pmid is not null and source='cellmarker'
    group by pubyear
),
d as (
    select pubyear,count(distinct(hralit_asctb_publication.doi)) as asctb_pubs
    from hralit_asctb_publication
    join hralit_publication on hralit_asctb_publication.doi=hralit_publication.doi
    where hralit_publication.pubyear is not null and hralit_publication.doi is not null
    group by pubyear
)
select a.pubyear,pubmed_pubs,cxg_pubs,cellmarker_pubs,asctb_pubs
from a left join b on a.pubyear=b.pubyear
left join c on a.pubyear=c.pubyear
left join d on a.pubyear=d.pubyear
order by pubyear;

\o