import pandas as pd
from ethnicolr import pred_fl_reg_name_five_cat

# Load the data
names_df = pd.read_csv("creators_information.csv")

# Reset the index to ensure unique indices
names_df.reset_index(drop=True, inplace=True)

# Filter rows that have last names and reset their index
names_with_lastnames = names_df.dropna(subset=['lastName']).copy()
names_with_lastnames.reset_index(drop=True, inplace=True)

# Predict ethnicity using last names
names_with_lastnames = pred_fl_reg_name_five_cat(names_with_lastnames, 'lastName','firstName')

names_df = pd.merge(names_df, names_with_lastnames[['firstName', 'lastName', 'asian','hispanic','nh_black','nh_white','other','race']],
                    on=['firstName', 'lastName'], how='left')
print(names_with_lastnames.head())

# Save the results to a new Excel file
names_df.to_excel("output_with_ethnicity.xlsx", index=False)
