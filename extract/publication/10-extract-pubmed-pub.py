import pandas as pd
import psycopg2

config = configparser.ConfigParser()
config.read('db_config.ini')

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="pubmed19",
    user=config.get('postgresql', 'user'),
    password=config.get('postgresql', 'password'),
    host=config.get('postgresql', 'host'),
    port=config.get('postgresql', 'port')
)

# Read the list of organs from the CSV
df_organs = pd.read_csv('data/publication/list_of_organs.csv')
organs = df_organs['organ'].tolist()  # Assuming 'organ' is the column name

# DataFrame to store the results
df_results = pd.DataFrame(columns=['pmid', 'organ', 'uid'])

for organ in organs:
    words = organ.split()
    
    descriptor_conditions = " AND ".join([f"descriptor_name ILIKE %s" for _ in words])
    article_title_conditions = " AND ".join([f"article_title ILIKE %s" for _ in words])
    
    cte_query = f"""
    WITH CTE AS (
        SELECT pmid, %s AS organ 
        FROM medline_mesh_heading 
        WHERE {descriptor_conditions}
        UNION 
        SELECT pmid, %s AS organ 
        FROM medline_master 
        WHERE {article_title_conditions}
    )
    SELECT CTE.pmid, organ, wosid_to_pmid.wosid AS uid 
    FROM CTE 
    LEFT JOIN wosid_to_pmid ON CTE.pmid = wosid_to_pmid.pmid
    """
    
    params = [organ] + [f"%{word}%" for word in words] + [organ] + [f"%{word}%" for word in words]
    df_temp = pd.read_sql_query(cte_query, conn, params=params)
    df_results = df_results.append(df_temp)

# Save the results to a CSV file
df_results.to_csv('data/publication/pubmed-pubs.csv', index=False)

# Close the database connection
conn.close()