#In WoS DB

#extract the affiliation and geolocation info
\copy (with aa as (select a.uid,a.name_id,a.first_name,a.last_name,a.full_name,b.addr_id,g.email_addr,h.pubyear from wos_summary_names a join wos_address_names b on a.uid=b.uid and a.name_id=b.name_id left join wos_summary_names_email_addr g on a.uid=g.uid and a.name_id=g.name_id left join wos_summary h on a.uid=h.uid), bb as (select c.uid,c.addr_id,c.country,c.city,c.state,d.organization,e.suborganization,f.zip from wos_addresses c left join wos_address_organizations d on c.uid=d.uid and c.addr_id=d.addr_id left join wos_address_suborganizations e on c.uid=e.uid and c.addr_id=e.addr_id left join wos_address_zip f on c.uid=f.uid and c.addr_id=f.addr_id),cc as (select uid,name_id,first_name,last_name,full_name,addr_id,email_addr,pubyear from aa group by uid,name_id,first_name,last_name,full_name,addr_id,email_addr,pubyear), dd as (select uid,addr_id,country,city,state,organization,suborganization,zip from bb group by uid,addr_id,country,city,state,organization,suborganization,zip) select cc.uid,cc.name_id,first_name,last_name,full_name,email_addr,pubyear,country,city,state,organization,suborganization,zip from cc left join dd on cc.uid=dd.uid and cc.addr_id=dd.addr_id)to '/N/slate/yokong/author_info.psv' Delimiter E'|' CSV HEADER Encoding 'SQL-ASCII'

#import data
create table author_info(uid varchar,name_id integer,first_name varchar,last_name varchar,full_name varchar,email_addr varchar,pubyear varchar,country varchar,city varchar,state varchar ,organization varchar,suborganization varchar,zip varchar);
\copy author_info from '/N/slate/yokong/author_info.psv' Delimiter E'|' CSV HEADER Encoding 'SQL-ASCII'

#------------
#In PubMed DB

#calculate career age
\copy (with aa as (select a.identifier,article_year :: integer as pubyear from medline_author_identifier a left join medline_article_date b on a.pmid=b.pmid) select identifier,min(pubyear) as first_pubyear,max(pubyear) as last_pubyear,2024-min(pubyear) as career_age_to_current,max(pubyear)-min(pubyear) as career_age from aa group by identifier)to '/N/slate/yokong/author_career_age.csv' Delimiter E',' CSV HEADER Encoding 'SQL-ASCII'

#import data
create table author_career_age(orcid varchar, first_pubyear integer,last_pubyear integer, career_age_to_current integer, career_age integer);
\copy author_career_age from '/N/slate/yokong/author_career_age.csv' Delimiter E',' CSV HEADER Encoding 'SQL-ASCII'

#integrate data - cover all affiliation
\copy (with aa as(select c.identifier as author_id,first_name,last_name,full_name,email_addr,country,city,state ,organization,suborganization,zip from author_info a join wosid_to_pmid b on a.uid=b.uid join pmid_author c on b.pmid=c.pmid and a.name_id=c.author_ctr), bb as (select author_id,first_name,last_name,full_name,email_addr,country,city,state ,organization,suborganization,zip from aa group by author_id,first_name,last_name,full_name,email_addr,country,city,state ,organization,suborganization,zip),cc as (select distinct(identifier) as author_id from pmid_author), dd as(select cc.author_id,first_name,last_name,full_name,email_addr,country,city,state ,organization,suborganization,zip,first_pubyear,last_pubyear,career_age_to_current,career_age from cc left join bb on cc.author_id=bb.author_id left join author_career_age d on cc.author_id=d.orcid) select author_id,first_name,last_name,full_name,email_addr,country,city,state ,organization,suborganization,zip,first_pubyear,last_pubyear,career_age_to_current,career_age from dd group by author_id,first_name,last_name,full_name,email_addr,country,city,state ,organization,suborganization,zip,first_pubyear,last_pubyear,career_age_to_current,career_age)to '/N/slate/yokong/author_info_all_affi.psv' Delimiter E'|' CSV HEADER Encoding 'SQL-ASCII'
#integrate data - record the lastest affiliation info
\copy (with aa as(select c.identifier as author_id,first_name,last_name,full_name,email_addr,country,city,state ,pubyear,organization,suborganization,zip from author_info a join wosid_to_pmid b on a.uid=b.uid join pmid_author c on b.pmid=c.pmid and a.name_id=c.author_ctr), tmp as (select author_id,first_name,last_name,full_name,email_addr,country,city,state,pubyear,organization,suborganization,zip from aa group by author_id,first_name,last_name,full_name,email_addr,country,city,state ,organization,suborganization,zip,pubyear),cte as (select author_id,first_name,last_name,full_name,pubyear,email_addr,country,city,state ,organization,suborganization,zip,ROW_NUMBER() OVER (PARTITION BY author_id ORDER BY pubyear DESC) AS rn from tmp),bb as (select author_id,first_name,last_name,full_name,email_addr,country,city,state ,organization,suborganization,zip from cte where rn=1),cc as (select distinct(identifier) as author_id from pmid_author), dd as(select cc.author_id,first_name,last_name,full_name,email_addr,country,city,state ,organization,suborganization,zip,first_pubyear,last_pubyear,career_age_to_current,career_age from cc left join bb on cc.author_id=bb.author_id left join author_career_age d on cc.author_id=d.orcid) select author_id,first_name,last_name,full_name,email_addr,country,city,state ,organization,suborganization,zip,first_pubyear,last_pubyear,career_age_to_current,career_age from dd group by author_id,first_name,last_name,full_name,email_addr,country,city,state ,organization,suborganization,zip,first_pubyear,last_pubyear,career_age_to_current,career_age)to '/N/slate/yokong/author_info_lastest_affi.psv' Delimiter E'|' CSV HEADER Encoding 'SQL-ASCII'

#import data
create table author_info_lastest_affi(author_id varchar,first_name varchar,last_name varchar,full_name varchar,email_addr varchar,country varchar,city varchar,state varchar,organization varchar,suborganization varchar,zip varchar,first_pubyear integer,last_pubyear integer,career_age_to_current integer,career_age integer)
\copy author_info_lastest_affi from '/N/slate/yokong/author_info_lastest_affi.psv' Delimiter E'|' CSV HEADER Encoding 'SQL-ASCII'
create table author_info_all_affi(author_id varchar,first_name varchar,last_name varchar,full_name varchar,email_addr varchar,country varchar,city varchar,state varchar,organization varchar,suborganization varchar,zip varchar,first_pubyear integer,last_pubyear integer,career_age_to_current integer,career_age integer);
\copy author_info_all_affi from '/N/slate/yokong/author_info_all_affi.psv' Delimiter E'|' CSV HEADER Encoding 'SQL-ASCII'

#output data - cover all affiliation
\copy (select name,level,a.author_id,citation,fund_ct,first_name,last_name,full_name,email_addr,country,city,state,organization,suborganization,zip,first_pubyear,last_pubyear,career_age_to_current,career_age from asct_expert a left join author_info_lastest_affi b on a.author_id=b.author_id) to '/N/slate/yokong/asct_author_info_lastest_affi.csv' Delimiter E',' CSV HEADER Encoding 'SQL-ASCII'
#output data - record the lastest affiliation info
\copy (select name,level,a.author_id,citation,fund_ct,first_name,last_name,full_name,email_addr,country,city,state,organization,suborganization,zip,first_pubyear,last_pubyear,career_age_to_current,career_age from asct_expert a left join author_info_all_affi b on a.author_id=b.author_id) to '/N/slate/yokong/asct_author_info_all_affi.csv' Delimiter E',' CSV HEADER Encoding 'SQL-ASCII'

#------------
#user DB
create table reviewers(type varchar,name varchar,version varchar,full_name varchar,first_name varchar,last_name varchar,orcid varchar,gender varchar);
\copy table reviewers from reviewers.csv Delimiter E',' CSV HEADER Encoding 'SQL-ASCII'

#query the reviewers' info and output
\copy (select * from reviewers a left join author_info_lastest_affi b on a.orcid=b.author_id)to '/N/slate/yokong/reviewers_info.csv' Delimiter E',' CSV HEADER Encoding 'SQL-ASCII'
\copy (select * from reviewers a left join author_info_all_affi b on a.orcid=b.author_id)to '/N/slate/yokong/reviewers_info_all.csv' Delimiter E',' CSV HEADER Encoding 'SQL-ASCII'
