import pandas as pd

# exchange rate data sources from world bank
# available at https://api.worldbank.org/v2/en/indicator/PA.NUS.FCRF?downloadformat=csv
exchange_rates_df = pd.read_csv('data/funding/API_PA.NUS.FCRF_DS2_en_csv_v2_5839703.csv', skiprows=4)

# Load the cost file
costs_df = pd.read_csv('data/results/app1/funding-cost/merged_results.csv')

# Mapping of the funding sources to their respective country codes
country_code_mapping = {
    'ardc': 'AUS',
    'cihr': 'CAN',
    'ec': 'EMU', 
    'kaken': 'JPN',
    'nih': 'USA',
    'nsf': 'USA'
}

# Filter the exchange rate dataframe for the needed countries
filtered_exchange_rates = exchange_rates_df[exchange_rates_df['Country Code'].isin(country_code_mapping.values())]

# Extract the latest non-null exchange rate for each country
latest_exchange_rates = {}
for source, country_code in country_code_mapping.items():
    country_data = filtered_exchange_rates[filtered_exchange_rates['Country Code'] == country_code].iloc[0]
    latest_year = country_data.last_valid_index()
    latest_exchange_rates[source] = country_data[latest_year]

# # Calculate the total cost in USD for each organ
# costs_df['total_cost'] = 0
# for source, exchange_rate in latest_exchange_rates.items():
#     costs_df['total_cost'] += costs_df[source] / exchange_rate

# output_df = costs_df[['organ', 'total_cost']]

# # Save the resulting dataframe to a CSV file
# output_df.to_csv('data/results/app1/funding-cost.csv', index=False)

for source, exchange_rate in latest_exchange_rates.items():
    costs_df[f'{source}_converted'] = costs_df[source] / exchange_rate

# Selecting the required columns (organ and all converted costs columns)
output_columns = ['organ'] + [f'{source}_converted' for source in latest_exchange_rates.keys()]
output_df = costs_df[output_columns]

# Save the resulting dataframe to a CSV file
output_df.to_csv('data/results/app1/funding-cost-each.csv', index=False)