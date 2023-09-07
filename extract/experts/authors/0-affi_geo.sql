\t on
\a
\pset fieldsep '|'
\pset format csv
\o data/expert/author_info.psv

WITH 
CTE1 AS (
    SELECT 
        a.uid, 
        a.name_id, 
        a.first_name, 
        a.last_name, 
        a.full_name, 
        b.addr_id, 
        g.email_addr, 
        h.pubyear 
    FROM 
        wos_summary_names a 
    JOIN 
        wos_address_names b ON a.uid = b.uid AND a.name_id = b.name_id 
    LEFT JOIN 
        wos_summary_names_email_addr g ON a.uid = g.uid AND a.name_id = g.name_id 
    LEFT JOIN 
        wos_summary h ON a.uid = h.uid
),
CTE2 AS (
    SELECT 
        c.uid, 
        c.addr_id, 
        c.country, 
        c.city, 
        c.state, 
        d.organization, 
        e.suborganization, 
        f.zip 
    FROM 
        wos_addresses c 
    LEFT JOIN 
        wos_address_organizations d ON c.uid = d.uid AND c.addr_id = d.addr_id 
    LEFT JOIN 
        wos_address_suborganizations e ON c.uid = e.uid AND c.addr_id = e.addr_id 
    LEFT JOIN 
        wos_address_zip f ON c.uid = f.uid AND c.addr_id = f.addr_id
),
CTE3 AS (
    SELECT 
        uid, 
        name_id, 
        first_name, 
        last_name, 
        full_name, 
        addr_id, 
        email_addr, 
        pubyear 
    FROM 
        CTE1 
    GROUP BY 
        uid, name_id, first_name, last_name, full_name, addr_id, email_addr, pubyear
),
CTE4 AS (
    SELECT 
        uid, 
        addr_id, 
        country, 
        city, 
        state, 
        organization, 
        suborganization, 
        zip 
    FROM 
        CTE2 
    GROUP BY 
        uid, addr_id, country, city, state, organization, suborganization, zip
)
SELECT 
    CTE3.uid, 
    CTE3.name_id, 
    first_name, 
    last_name, 
    full_name, 
    email_addr, 
    pubyear, 
    country, 
    city, 
    state, 
    organization, 
    suborganization, 
    zip 
FROM 
    CTE3 
LEFT JOIN 
    CTE4 ON CTE3.uid = CTE4.uid AND CTE3.addr_id = CTE4.addr_id;

\o
