with aa as (
    select 
        pmid,
        country_code 
    from hralit_pub_funding_funder a 
    join hralit_funder_cleaned b 
    on a.soa_funder_id=b.soa_funder_id
)
select 
    country_code,
    count(distinct(pmid))as funder_count
from aa 
group by country_code 
order by ct desc