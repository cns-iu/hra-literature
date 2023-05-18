#count the number of publication in each organ
with a as (
  select organ,count(*)as pct from pmid_34_organs group by organ
  ),b as (
  select organ,count(*)as uct from uid_34_organs where uid not in (select uid from pmid_34_organs where uid is not null) group by organ
  ) 
insert into organ_statistic(organ,pub_ct) select a.organ,pct+uct from a join b on a.organ ilike b.organ;

#count the total citations for each organ
with a as (
  select uid,cit_ct from uid_cit_count where uid is not null
  ),b as (
  select organ,uid from uid_34_organs where uid is not null
  ) 
select b.organ,sum(a.cit_ct) from b left join a on b.uid=a.uid group by b.organ; 
