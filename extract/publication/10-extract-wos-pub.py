import pandas as pd
import psycopg2

# Connect to the PostgreSQL database named wos_2018
conn = psycopg2.connect(
    dbname="wos_2018",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

# Read the list of organs from the CSV
df_organs = pd.read_csv('data/publication/list_of_organs.csv')
organs = df_organs['organ'].tolist()  # Assuming 'organ' is the column name

# DataFrame to store the results
df_results = pd.DataFrame(columns=['uid', 'organ'])

for organ in organs:
    words = organ.split()
    
    title_conditions = " AND ".join([f"title ILIKE %s" for _ in words])
    keyword_conditions = " AND ".join([f"keyword ILIKE %s" for _ in words])
    keyword_plus_conditions = " AND ".join([f"keyword_plus ILIKE %s" for _ in words])
    
    query = f"""
    (SELECT uid, %s AS organ
    FROM wos_titles 
    WHERE title_type='item' AND {title_conditions})
    UNION
    (SELECT uid, %s AS organ
    FROM wos_keywords 
    WHERE {keyword_conditions})
    UNION
    (SELECT uid, %s AS organ
    FROM wos_keywords_plus 
    WHERE {keyword_plus_conditions})
    """
    
    params = [organ] + [f"%{word}%" for word in words] + [organ] + [f"%{word}%" for word in words] + [organ] + [f"%{word}%" for word in words]
    df_temp = pd.read_sql_query(query, conn, params=params)
    df_results = df_results.append(df_temp)

# Save the results to a CSV file
df_results.to_csv('data/publication/wos-pubs.csv', index=False)

# Close the database connection
conn.close()