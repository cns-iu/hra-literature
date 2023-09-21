\t on
\a
\pset fieldsep ','
\pset format csv
\pset tuples_only off
\o data/results/app1/pub-ct.csv

with a as (
    select organ,count(distinct(pmid))as pub_ct 
    from hralit_publication_subject group by organ
),
b as (
    select organ,sum(cit_ct)as cit_ct 
    from hralit_publication_subject a 
    left join uid_cit_count b on a.pmid=b.pmid 
    group by organ
)
select hralit_organ.organ,a.pub_ct,b.cit_ct 
from hralit_organ 
left join a on hralit_organ.organ=a.organ 
left join b on hralit_organ.organ=b.organ;

\o