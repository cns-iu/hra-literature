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
results_df = pd.DataFrame(columns=["organ", "dataset_count", "cell_count_count"])

# Group by 'organ' and iterate over groups
for organ, group in lookup_df.groupby('organ'):
    
    total_dataset_count = 0
    total_cell_count_count = 0

    for index, row in group.iterrows():
        cxg_organ = row['cxg_organ']
        
        # Skip the iteration if cxg_organ is NaN
        if pd.isna(cxg_organ):
            continue
        
        query = """
                    SELECT COUNT(dataset_id) AS dataset_count, SUM(dataset_total_cell_count :: INTEGER) AS cell_count_count
                    FROM hralit_dataset
                    WHERE organ = %s;
                """
        
        result = pd.read_sql_query(query, conn, params=(cxg_organ,))
        total_dataset_count += result.iloc[0]['dataset_count'] if result.iloc[0]['dataset_count'] is not None else 0
        total_cell_count_count += result.iloc[0]['cell_count_count'] if result.iloc[0]['cell_count_count'] is not None else 0

    # Append the aggregated result for the organ to the results DataFrame
    new_row = pd.DataFrame({
        "organ": [organ],
        "dataset_count": [total_dataset_count],
        "cell_count_count": [total_cell_count_count]
    })
    results_df = pd.concat([results_df, new_row], ignore_index=True)

# Close the database connection
conn.close()

# Write the results DataFrame to a CSV file
results_df.to_csv('data/results/app1/dataset-ct.csv', index=False)
