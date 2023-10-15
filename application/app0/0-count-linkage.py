import pandas as pd
import psycopg2
import configparser

# Read the database configuration from db_config.ini
config = configparser.ConfigParser()
config.read('db_config.ini')

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname=config.get('postgresql', 'dbname'),
    user=config.get('postgresql', 'user'),
    password=config.get('postgresql', 'password'),
    host=config.get('postgresql', 'host'),
    port=config.get('postgresql', 'port')
)

queries = [
    ("Count of linkages between authors and institutions from hralit_author_institution", 
     "select count(distinct(orcid,soa_institution_id))from hralit_author_institution;"),
    
    ("Count of linkages between AS, CT, and B from hralit_ontology_triple",
     "select count(*) from hralit_triple;"),
    
    ("Count of linkages between publications and organs from hralit_publication_subject",
     "select count(distinct(pmid,organ)) from hralit_publication_subject;"),
    
    ("Count of linkages between asctb refs and publication",
     "select count(doi) from hralit_asctb_publication where doi in (select doi from hralit_publication);"),
    
    ("Count of linkages between asctb refs and organ",
     "select count(organ) from hralit_asctb_publication;"),
    
    ("creator & author",
     "select count(*) from hralit_creator;"),
    
    ("reviewer & author",
     "select count(*) from hralit_reviewer;"),
    
    ("dataset & donor",
     "select count(donor_id) from hralit_dataset;"),
    
    ("dataset & publication",
     "select count(publication_doi) from hralit_dataset;"),
    
    ("creator & digital object",
     "select count(hubmap_id) from hralit_creator where hubmap_id in (select hubmap_id from hralit_digital_objects);"),
    
    ("reviewer & digital object",
     "select count(hubmap_id) from hralit_reviewer where hubmap_id in (select hubmap_id from hralit_digital_objects);"),
    
    ("author & organ",
     "select count(*)from hralit_author_expertise;"),
    
    ("publication & funding",
     "select count(distinct(pmid,funding_id))from hralit_pub_funding_funder where pmid is not null and funding_id is not null;"),
    
    ("funding & cleaned funder",
     "select count(distinct(soa_funder_id,funding_id))from hralit_pub_funding_funder where soa_funder_id is not null and funding_id is not null;"),
    
    ("funding & uncleaned funder",
     "select count(distinct(funder_name_pubmed,funding_id))from hralit_pub_funding_funder where funder_name_pubmed is not null and funding_id is not null;"),
    
    ("triple & organ",
     "select count(distinct(row_id,organ)) from hralit_triple;"),
    
    ("CellMarker/CxG refs & publication",
     "select count(pmid) from hralit_other_refs;"),

     ("AS & AS",
      "select count(*) from hralit_asctb_linkage where relationship='part_of';"
     ),

    ("AS & CT",
      "select count(*) from hralit_asctb_linkage where relationship='located_in';"
     ),

    ("CT & CT",
      "select count(*) from hralit_asctb_linkage where relationship='is_a';"
     ),
     
    ("CT & B",
      "select count(*) from hralit_asctb_linkage where relationship='characterizes';"
     )
]

# Collect results
results = []
for annotation, query in queries:
    cursor = conn.cursor()
    cursor.execute(query)
    count = cursor.fetchone()[0]
    results.append((annotation, count))
    cursor.close()

# Convert results to DataFrame
df = pd.DataFrame(results, columns=['Relationships', '#Linkages'])

# Save to CSV
df.to_csv('data/results/app0/linkage-ct.csv', index=False)

# Close the connection
conn.close()
