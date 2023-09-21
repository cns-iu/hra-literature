\t on
\a
\pset fieldsep ','
\pset format csv
\pset tuples_only off
\o data/results/app3/ins-ct.csv

select expertise as organ, count(distinct(soa_institution_id))as ins_ct
from hralit_author_expertise a
join hralit_author_institution b on a.orcid=b.orcid
where expertise is not null and soa_institution_id is not null and a.orcid is not null
group by expertise;

\o
