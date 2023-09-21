\t on
\a
\pset fieldsep ','
\pset format csv
\pset tuples_only off
\o data/results/app1/funding-ct.csv

select organ,count(distinct(funding_id)) as funding_count, count(distinct(soa_funder_id)) as funder_count
from hralit_publication_subject a left join hralit_pub_funding_funder b
on a.pmid=b.pmid 
where b.pmid is not null and b.funding_id is not null
group by organ;

\o