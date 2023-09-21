-- expert data:
\copy hralit_creator from /data/experts/hralit_creators.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

\copy hralit_reviewer from /data/experts/hralit_reviewers.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII';

with t1 as (
    select 
        'https://orcid.org/' || substring(identifier from '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]')AS orcid,
        grant_id
    from pmid_author
    join pmid_grant_all on pmid_author.pmid=pmid_grant_all.pmid
    where substring(identifier from '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]') is not null
    group by orcid,grant_id
),
t2 as (
    select 
        orcid,
        count(*) as involved_funding
    from t1
    group by orcid
),
t3 as (
    select cleaned_author_info_3.orcid,first_name,last_name,first_pubyear,career_age,involved_funding
    from cleaned_author_info_3
    left join t2 on cleaned_author_info_3.orcid=t2.orcid
)
insert into hralit_author(orcid,first_name,last_name,first_pubyear,career_age,involved_funding)
    select orcid,first_name,last_name,first_pubyear :: integer,career_age :: integer,involved_funding from t3
    where orcid in (select orcid from hralit_author_expertise)
        or orcid in (select 'https://orcid.org/' || substring(identifier from '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]') from pmid_author 
                where pmid in (select pmid from hralit_publication))
        or REPLACE(orcid,'https://orcid.org/','') in (select orcid from hralit_creator)
        or REPLACE(orcid,'https://orcid.org/','') in (select orcid from hralit_reviewer);


insert into hralit_author(orcid,first_name,last_name)
    select 
        'https://orcid.org/' || orcid,
        first_name,
        last_name
    from hralit_creator 
    where orcid not in (select REPLACE(orcid,'https://orcid.org/','') from hralit_author where orcid is not null);

insert into hralit_author(orcid,first_name,last_name)
    select 
        'https://orcid.org/' || orcid,
        first_name,
        last_name
    from hralit_reviewer 
    where orcid not in (select REPLACE(orcid,'https://orcid.org/','') from hralit_author where orcid is not null);

