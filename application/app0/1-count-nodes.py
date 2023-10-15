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
# List of SQL queries with their annotations
queries = [
    ("anatomical_structures", 
     "select count(distinct(id)) from hralit_anatomical_structures where id is not null;"),

    ("asctb_publication",
     "select count(distinct(id)) from hralit_asctb_publication where id is not null;"),

    ("authors",
     "select count(distinct(orcid)) from hralit_author;"),

    ("biomarker",
     "select count(distinct(id)) from hralit_biomarkers where id is not null;"),

    ("cell types",
     "select count(distinct(id)) from hralit_cell_types where id is not null;"),

    ("CellMarker/CxG/GTEx publication",
     "select count(distinct(doi)) from hralit_other_refs;"),

    ("creator",
     "select count(distinct(orcid)) from hralit_creator;"),

    ("dataset",
     "select count(distinct(dataset_id)) from hralit_dataset;"),

    ("digital objects",
     "select count(distinct(hubmap_id)) from hralit_digital_objects;"),

    ("donor",
     "select count(distinct(donor_id)) from hralit_donor;"),

    ("(cleaned) funder",
     "select count(distinct(soa_funder_id)) from hralit_funder_cleaned;"),

    ("(uncleaned) funder",
     "select count(distinct(funder_name_pubmed)) from hralit_pub_funding_funder;"),

    ("funding",
     "select count(distinct(funding_id)) from hralit_funding;"),

    ("(cleaned) institution",
     "select count(distinct(soa_institution_id)) from hralit_institution;"),

    ("organ",
     "select count(distinct(organ)) from hralit_organ;"),

    ("publication",
     "select count(distinct(pmid)) from hralit_publication;"),

    ("reviewer",
     "select count(distinct(orcid)) from hralit_reviewer;")
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
df = pd.DataFrame(results, columns=['Name', '#Nodes'])

# Save to CSV
df.to_csv('data/results/app0/nodes-ct.csv', index=False)

# Close the connection
conn.close()
