\copy (with aa as (select a.uid,a.name_id,a.first_name,a.last_name,a.full_name,b.addr_id,g.email_addr,h.pubyear from wos_summary_names a join wos_address_names b on a.uid=b.uid and a.name_id=b.name_id left join wos_summary_names_email_addr g on a.uid=g.uid and a.name_id=g.name_id left join wos_summary h on a.uid=h.uid), bb as (select c.uid,c.addr_id,c.country,c.city,c.state,d.organization,e.suborganization,f.zip from wos_addresses c left join wos_address_organizations d on c.uid=d.uid and c.addr_id=d.addr_id left join wos_address_suborganizations e on c.uid=e.uid and c.addr_id=e.addr_id left join wos_address_zip f on c.uid=f.uid and c.addr_id=f.addr_id),cc as (select uid,name_id,first_name,last_name,full_name,addr_id,email_addr,pubyear from aa group by uid,name_id,first_name,last_name,full_name,addr_id,email_addr,pubyear), dd as (select uid,addr_id,country,city,state,organization,suborganization,zip from bb group by uid,addr_id,country,city,state,organization,suborganization,zip) select cc.uid,cc.name_id,first_name,last_name,full_name,email_addr,pubyear,country,city,state,organization,suborganization,zip from cc left join dd on cc.uid=dd.uid and cc.addr_id=dd.addr_id)to '/N/slate/yokong/author_info.psv' Delimiter E'|' CSV HEADER Encoding 'SQL-ASCII'
