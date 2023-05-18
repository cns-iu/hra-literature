#count the number of publication in each organ
with a as (
  select organ,count(*)as pct from pmid_34_organs group by organ
  ),b as (
  select organ,count(*)as uct from uid_34_organs where uid not in (select uid from pmid_34_organs where uid is not null) group by organ) 
insert into organ_statistic(organ,pub_ct) select a.organ,pct+uct from a join b on a.organ ilike b.organ;
