import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('db_config.ini')

# connect to pubmed19
conn_pubmed19 = psycopg2.connect(
    dbname="pubmed19",
    user=config.get('postgresql', 'user'),
    password=config.get('postgresql', 'password'),
    host=config.get('postgresql', 'host'),
    port=config.get('postgresql', 'port')
)

with conn_pubmed19.cursor() as cursor:
    export_query = "COPY (SELECT * FROM medline_grant) TO STDOUT WITH DELIMITER '|' CSV HEADER"
    with open('data/funding/pmid_grant_all.psv', 'w') as f:
        cursor.copy_expert(export_query, f)

conn_pubmed19.close()


conn_yokong = psycopg2.connect(
    dbname=config.get('postgresql', 'dbname'),
    user=config.get('postgresql', 'user'),
    password=config.get('postgresql', 'password'),
    host=config.get('postgresql', 'host'),
    port=config.get('postgresql', 'port')
)

with conn_yokong.cursor() as cursor:
    create_table_query = """
    CREATE TABLE pmid_grant_all (
        pmid INT,
        grant_ctr INT,
        country VARCHAR,
        acronym VARCHAR,
        agency VARCHAR,
        grant_id VARCHAR
    );
    """
    cursor.execute(create_table_query)
    conn_yokong.commit()

    # import data to pmid_grant_all table
    import_query = "COPY pmid_grant_all FROM STDIN WITH DELIMITER '|' CSV HEADER"
    with open('data/funding/pmid_grant_all.psv', 'r') as f:
        cursor.copy_expert(import_query, f)

    conn_yokong.commit()

conn_yokong.close()
