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

# Read the CSV file using pandas
lookup_df = pd.read_csv('data/experimental/lookup.csv')
# Prepare an empty DataFrame to store the results
results_df = pd.DataFrame(columns=["organ", "hubmap_ct", "gtex_ct", "cxg_ct"])

# Group by 'organ' and iterate over groups
for organ, group in lookup_df.groupby('organ'):
    
    hubmap_ct = 0
    gtex_ct = 0
    cxg_ct = 0

    for index, row in group.iterrows():
        cxg_organ = row['cxg_organ']
        
        # Skip the iteration if cxg_organ is NaN
        if pd.isna(cxg_organ):
            continue
        
        query = """
                    SELECT 
                        COUNT(DISTINCT CASE WHEN source = 'hubmap' THEN dataset_id ELSE NULL END) AS hubmap_ct,
                        COUNT(DISTINCT CASE WHEN source = 'gtex' THEN dataset_id ELSE NULL END) AS gtex_ct,
                        COUNT(DISTINCT CASE WHEN source = 'cxg' THEN dataset_id ELSE NULL END) AS cxg_ct
                    FROM hralit_dataset
                    WHERE organ = %s;
                """
        
        result = pd.read_sql_query(query, conn, params=(cxg_organ,))
        hubmap_ct += result.iloc[0]['hubmap_ct'] if result.iloc[0]['hubmap_ct'] is not None else 0
        gtex_ct += result.iloc[0]['gtex_ct'] if result.iloc[0]['gtex_ct'] is not None else 0
        cxg_ct += result.iloc[0]['cxg_ct'] if result.iloc[0]['cxg_ct'] is not None else 0


    # Append the aggregated result for the organ to the results DataFrame
    new_row = pd.DataFrame({
        "organ": [organ],
        "hubmap_ct": [hubmap_ct],
        "gtex_ct": [gtex_ct],
        "cxg_ct": [cxg_ct]
    })
    results_df = pd.concat([results_df, new_row], ignore_index=True)

# Close the database connection
conn.close()

# Write the results DataFrame to a CSV file
results_df.to_csv('data/results/app3/dataset-ct-each.csv', index=False)