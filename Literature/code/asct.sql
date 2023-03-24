#asct
with e as (select uid from asct_ref a join uid_identifier b on lower(a.doi)=lower(b.identifier_value)) select count(*) from e join uid_34_organs b on e.uid=b.uid;

