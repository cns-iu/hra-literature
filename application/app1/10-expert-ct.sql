\t on
\a
\pset fieldsep ','
\pset format csv
\pset tuples_only off
\o data/results/app1/expert-ct.csv

with a as (
    select expertise,count(distinct(orcid))as exp_ct 
    from hralit_author_expertise 
    group by expertise
),
b as (
    select c.expertise,avg(h_index)as h_avg 
    from hralit_author_expertise c 
    left join author_h_index d on c.orcid=d.orcid 
    group by expertise
)
select hralit_organ.organ, a.exp_ct as expert_count, b.h_avg as total_h_index
from hralit_organ left join a on hralit_organ.organ=a.expertise 
left join b on hralit_organ.organ=b.expertise;

\o