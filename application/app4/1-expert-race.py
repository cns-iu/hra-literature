import pandas as pd
import psycopg2
import configparser
import gender_guesser.detector as gender
from ethnicolr import pred_fl_reg_name_five_cat

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

# SQL query
sql = """
    SELECT orcid, first_name, last_name
    FROM hralit_creator 
    GROUP BY orcid, first_name, last_name
    
    UNION

    SELECT orcid, first_name, last_name  
    FROM hralit_reviewer 
    GROUP BY orcid, first_name, last_name   

"""

# Fetch data using SQL query
df = pd.read_sql_query(sql, conn)

# Close the connection
conn.close()

#Race statistic
names_with_lastnames = df.dropna(subset=['last_name']).copy()
names_with_lastnames.reset_index(drop=True, inplace=True)
names_with_lastnames = pred_fl_reg_name_five_cat(names_with_lastnames, 'last_name', 'first_name')

# Merge results back to the original dataframe
names_df = pd.merge(df, names_with_lastnames[['first_name', 'last_name', 'asian','hispanic','nh_black','nh_white','other','race']],
                    on=['first_name', 'last_name'], how='left')

# Extract the race with highest probability for each orcid
race_columns = ['nh_white', 'nh_black', 'hispanic', 'asian', 'other']
names_df['max_race'] = names_df[race_columns].idxmax(axis=1)

# # Group by max_race and count unique orcids
# race_counts = names_df.groupby(['max_race'])['orcid'].nunique().reset_index()
# race_counts = race_counts.rename(columns={'orcid': '#unique orcid', 'max_race': 'race'})

# # Calculate average probability for each race
# race_avg_prob = names_df.groupby('max_race')[race_columns].mean().reset_index()
# race_avg_prob = race_avg_prob.melt(id_vars='max_race', value_vars=race_columns, var_name='race', value_name='average_probability')
# race_avg_prob = race_avg_prob[race_avg_prob['max_race'] == race_avg_prob['race']]

# # Merge race_counts and race_avg_prob
# final_race_data = pd.merge(race_counts, race_avg_prob, on='race')[['race', '#unique orcid', 'average_probability']]

# # Save race result to CSV
# final_race_data.to_csv('data/results/app6/expert-race.csv', index=False)

race_counts = names_df.groupby(['max_race'])['orcid'].nunique().reset_index()
race_counts = race_counts.rename(columns={'orcid': '#orcid', 'max_race': 'race'})

# Calculate the average of the maximum probabilities for all orcid values
average_max_probability = names_df[race_columns].max(axis=1).mean()
average_row = pd.DataFrame({
    'race': ['average_probability'],
    '#unique orcid': [None],  # or 0 if you prefer
    'average_probability': [average_max_probability]
})

# Append the average row to the race_counts dataframe
final_race_data = pd.concat([race_counts, average_row], ignore_index=True)

# Save race result to CSV
final_race_data.to_csv('data/results/app6/expert-race.csv', index=False)