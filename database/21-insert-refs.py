import pandas as pd
import psycopg2
import configparser


def import_from_csv_to_db():
    # Read the .txt file with tab delimiters
    df = pd.read_csv('data/experimental/human_cell_markers.txt', sep='\t')
    # Filter rows where PMID is not null
    df = df[df['PMID'].notna()]

    # Drop duplicate PMIDs and keep only unique PMIDs
    df = df.drop_duplicates(subset='PMID', keep='first')

    for index, row in df.iterrows():
        cur.execute(
            "INSERT INTO hralit_other_publication (pmid, source) VALUES (%s, 'cellmarker')", 
            (row['PMID'],)
        )


def import_from_dataset_to_db():
    cur.execute("""
        INSERT INTO hralit_other_publication (doi, source) 
        SELECT publication_doi, source
        FROM hralit_dataset 
        WHERE publication_doi IS NOT NULL
        GROUP BY publication_doi, source ;
        update hralit_other_publication set doi=pmid_doi.doi from pmid_doi where pmid_doi.pmid=hralit_other_publication.pmid;
        update hralit_other_publication set pmid=pmid_doi.pmid from pmid_doi where lower(pmid_doi.doi)=lower(hralit_other_publication.doi) 
            and hralit_other_publication.pmid is null;
    """)

if __name__ == "__main__":
    # Load configuration
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
    cur = conn.cursor()

    # Import data from CSV
    import_from_csv_to_db()

    # Import data from hralit_dataset
    import_from_dataset_to_db()

    # Commit the transaction and close the connection
    conn.commit()
    cur.close()
    conn.close()
