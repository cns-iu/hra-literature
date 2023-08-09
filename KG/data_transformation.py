import pandas as pd

# Load the data from the CSV files
hubmap_donor = pd.read_csv('/path/to/hubmap_donor.csv')
cxg_donor = pd.read_csv('/path/to/cxg_donor.csv')
gtex_donor = pd.read_csv('/path/to/gtex_donor.csv')

# Harmonize Hubmap data
hubmap_transformed = hubmap_donor[['HBM_ID', 'Sex_Preferred Term', 'Age_Data Value', 'Race_Preferred Term']].copy()
hubmap_transformed.columns = ['id', 'sex', 'age', 'ethnicity']
hubmap_transformed['source'] = 'hubmap'
hubmap_transformed['age'] = hubmap_transformed['age'].astype(str)

# Harmonize CxG data
cxg_transformed = cxg_donor[['donor_id', 'sex', 'development_stage', 'self_reported_ethnicity']].copy()
cxg_transformed.columns = ['id', 'sex', 'age', 'ethnicity']
cxg_transformed['source'] = 'cxg'
cxg_transformed['age'] = cxg_transformed['age'].str.extract('(\d+)-year-old')[0]

# Harmonize GTEX data
gtex_transformed = gtex_donor[['SUBJID', 'SEX', 'AGE']].copy()
gtex_transformed.columns = ['id', 'sex', 'age']
gtex_transformed['source'] = 'gtex'
gtex_transformed['sex'] = gtex_transformed['sex'].map({1: 'male', 2: 'female'})
gtex_transformed['ethnicity'] = None  # Placeholder since ethnicity is not present

# Combine all datasets
combined_data = pd.concat([hubmap_transformed, cxg_transformed, gtex_transformed], ignore_index=True)

# Save the combined data to CSV (optional)
combined_data.to_csv('/path/to/harmonized_donor_data.csv', index=False)
